# CS361 Microservice

## How to run the program:
1. The program will ask the user if they want to get the json information.
2. Then the user types `YES` and then it will show that it is getting the data. Then print in the books.txt that its getting the request.
3. Then it will get the information from the json file and then the microservice will send the information from the json file to the HTML file.
4. Then the `getJson.txt` will print request received.
5. All of the information will be printed in the html page called `results.html`

The `results.html` is the final product of the microservice. It will be in the same directory as the `microservice.py` will be in. 

## This is my UML sequence diagram: 

<img width="575" alt="Screen Shot 2023-02-12 at 6 14 33 PM" src="https://user-images.githubusercontent.com/91424770/218355459-ff9db7fd-0c1c-4116-8e38-9d061a9f02ce.png">


Files needed to run in order for the microservice to run: 
1. `microserviceUI.py`
2. `microservice.py`
3. `recieved.py`

You will also need to have `books.txt` & `getjson.txt` open.
