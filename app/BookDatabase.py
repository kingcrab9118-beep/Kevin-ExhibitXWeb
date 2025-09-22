r"""BookDatabase class and interface support functions.

The BookDatabase module contains the BookDatabase class and support
functions to interface with the BookDatabase class. Public interface
functions are limited to user interface related operations associated
with the database."""

import re
import os
import sqlite3
import shutil
from contextlib import closing

__version__ = "2.3.11"
__author__ = "August Frisk <https://github.com/users/4N0NYM0U5MY7H>"

# --------------------------------------------------------------------
# Public database interface functions
def enter_book_title():
    while True:
        print(
            "Enter a BOOK TITLE.\n"
            + "Must only use A(a)-Z(z). Can include spaces.\n"
            + "Must be less than 200 characters."
        )
        book_title = input("BOOK TITLE: ").title()
        if re.search("^[a-zA-Z\s]+$", book_title):
            if len(book_title) < 201:
                return book_title


def enter_author_name():
    while True:
        print(
            "Enter an AUTHOR's NAME.\n"
            + "Must only use A(a)-Z(z). Can include spaces.\n"
            + "Must be less than 100 characters."
        )
        author_name = input("AUTHOR NAME: ").title()
        if re.search("^[a-zA-Z\s]+$", author_name):
            if len(author_name) < 100:
                return author_name


def enter_date_completed():
    while True:
        print(
            "Enter a DATE the book was completed.\n"
            + "Must use this format: MM/DD/YYYY."
        )
        date_completed = input("DATE COMPLETED: ")
        if re.match("(\d{2})[/](\d{2})[/](\d{4})$", date_completed):
            return date_completed


def enter_book_id():
    print("Enter a BOOK ID to delete.")
    print("Input a number and press ENTER to select an option.")
    while True:
        try:
            user_input = int(input("BOOK ID: "))
            if re.search("[0-9]+", str(user_input)) is None:
                raise ValueError
        except ValueError:
            continue
        else:
            return user_input


def enter_filename():
    while True:
        print(
            "Enter a FILE NAME.\n"
            + "Must only use A(a)-Z(z).\n"
            + "Must be less than 25 characters."
        )
        filename = input("FILE NAME: ")
        if re.search("^[a-zA-Z]+$", filename):
            if len(filename) < 26:
                return filename


# --------------------------------------------------------------------
# Private database interface functions
def _return_query_by_row(query):
    results = ""
    for row in query:
        results += f"{row}\n"
    return results


def _create_database(filename):
    try:
        with open(filename, "r"):
            pass
    except FileNotFoundError:
        with open(filename, "w"):
            pass


class BookDatabase:
    """Represents a database with CRUD opertaions for the CS361 book tracking program."""

    instance = None

    def __new__(cls, *args, **kwargs):
        """Implement the singleton design pattern."""
        if cls.instance is None:
            cls.instance = super().__new__(BookDatabase)
            return cls.instance
        return cls.instance

    def __init__(self, filename):
        self._sqlite_file = filename
        _create_database(self._sqlite_file)
        self._connection = self._create_connection()
        self._create_table()
        self._previous_query = None
        self._queries = {
            "id": "SELECT * FROM books WHERE book_id = ?",
            "title": "SELECT * FROM books WHERE title = ?",
            "author": "SELECT * FROM books WHERE author = ?",
            "date": "SELECT * FROM books WHERE date = ?",
            "view all": "SELECT * FROM books ORDER BY book_id",
            "add new": "INSERT INTO books(title, author, date) VALUES (?,?,?)",
            "delete by id": "DELETE FROM books WHERE book_id = ?",
            "update": "",
        }

    def __del__(self):
        try:
            self._create_connection().close()
        except sqlite3.Error as error:
            print(f"__del__: {error}")

    def _create_connection(self):
        try:
            return sqlite3.connect(self._sqlite_file)
        except sqlite3.Error as error:
            print(f"create_connection: {error}")

    def _dictionary_factory(self, cursor, row):
        """Returns rows as a dict with column names mapped to values."""
        # source: https://docs.python.org/3/library/sqlite3.html#how-to-create-and-use-row-factories
        fields = [column[0] for column in cursor.description]
        return {key: value for key, value in zip(fields, row)}

    def _create_table(self):
        sql_string = """CREATE TABLE IF NOT EXISTS books(
                        book_id INTEGER PRIMARY KEY,
                        title VARCHAR(200) NOT NULL,
                        author VARCHAR(100) NOT NULL,
                        date VARCHAR(10))"""
        try:
            with closing(self._create_connection()) as connection:
                with closing(connection.cursor()) as cursor:
                    cursor.execute(sql_string)
        except sqlite3.Error as error:
            print(f"create_table: {error}")

    def _get_query_key(self, n=0):
        if n < 0:
            n += len(self._queries)
        for i, key in enumerate(self._queries.keys()):
            if i == n:
                return key
        raise IndexError("dictionary index out of range.")

    def _set_sqlite_file(self, filename):
        self._sqlite_file = filename

    def save_backup(self, filename, directory):
        try:
            shutil.copy2(self._sqlite_file, f"{directory}/{filename}")
            print(f"Successfully saved {filename} to {directory}!")
        except shutil.SameFileError as error:
            print(f"save_backup: {error}")

    def load_backup(self, filename, directory):
        if filename in os.listdir(directory):
            self._set_sqlite_file(f"{dirctory}/{filename}")
            print(f"Successfully loaded backup {filename} from {directory}")
        else:
            print(f"No file named {filename} in {directory}/!")

    def add_new_entry(self, args):
        sql_string = self._queries["add new"]
        try:
            with closing(self._create_connection()) as connection:
                with closing(connection.cursor()) as cursor:
                    cursor.execute(sql_string, args)
                connection.commit()
            success_string = f"{args[0]} by {args[1]} completed on {args[2]}."
            print(f"Book successfully added!\n{success_string}")
        except sqlite3.Error as error:
            print(f"add_new_entry: {error}")

    def delete_by_id(self, id):
        sql_select_string = self._queries["id"]
        sql_delete_string = self._queries["delete by id"]
        args = (id,)
        try:
            with closing(self._create_connection()) as connection:
                with closing(connection.cursor()) as cursor:
                    query = cursor.execute(sql_select_string, args)
                    query_string = query.fetchone()
                    if query_string:
                        print("Are you sure you want to delete this from your records?")
                        print(query_string)
                        while True:
                            print("Type 'YES' to continue or press ENTER to cancel.")
                            continue_prompt = input("Your input: ")
                            if continue_prompt.upper() == "YES":
                                cursor.execute(sql_delete_string, args)
                                print("Book successfully deleted!")
                                connection.commit()
                                return
                            else:
                                print("Canceling delete request...")
                                return
                    else:
                        print(f"No records found with Book ID {id}.")
        except sqlite3.Error as error:
            print(f"delete_by_id: {error}")

    def view_all_entries(self):
        sql_string = """SELECT * FROM books ORDER BY title DESC"""
        self._previous_query = sql_string
        try:
            with closing(self._create_connection()) as connection:
                with closing(connection.cursor()) as cursor:
                    query = cursor.execute(sql_string).fetchall()
                    results = ""
                    for row in query:
                        results += f"{row}\n"
            return results
        except sqlite3.Error as error:
            print(f"view_all_entries: {error}")

    def search(self, key, value):
        sql_string = self._queries[self._get_query_key(key)]
        args = (value,)
        self._previous_query = (sql_string, args)
        try:
            with closing(self._create_connection()) as connection:
                with closing(connection.cursor()) as cursor:
                    query = cursor.execute(sql_string, args).fetchall()
                    return (
                        _return_query_by_row(query)
                        if query
                        else f"No results found with {self._get_query_key(key)} {value}"
                    )
        except sqlite3.Error as error:
            print(f"search: {error}")

    def generate_json_data(self):
        """Returns search reslts in a JSON ready dictionary."""
        try:
            with closing(self._create_connection()) as connection:
                connection.row_factory = self._dictionary_factory
                with closing(connection.cursor()):
                    results = []
                    if type(self._previous_query) is str:
                        for row in connection.execute(self._previous_query):
                            results.append(row)
                    if type(self._previous_query) is tuple:
                        for row in connection.execute(
                            str(self._previous_query[0]), self._previous_query[1]
                        ):
                            results.append(row)
                    return dict({"books": results})
        except sqlite3.Error as error:
            print(f"generate_json: {error}")
