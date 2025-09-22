import time
from json2html import *

txt_file = "../data/request.txt"
json_file = "../data/books.json"
html_file = "../data/response.html"

print("Listening for requests ...")

while True:
    time.sleep(1)

    try:
        with open(txt_file, "r") as f:
            line = f.readline()
    except FileNotFoundError:
        continue

    if line == "request":

        print("Request received ...")
        with open(txt_file, "w") as f:
            f.write("received")

        with open(json_file) as f:
            d = f.read()
            scanOutput = json2html.convert(json=d)

        with open(html_file, "w") as htmlFile:
            htmlFile.write(str(scanOutput))

        print("Json file is converted into html successfully")

    elif line == "exit":
        with open(txt_file, "w") as f:
            f.write("")
        print("Shutting down ...")
        exit()