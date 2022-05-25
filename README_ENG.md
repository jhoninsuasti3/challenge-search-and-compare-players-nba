# Explanation of the project worked and carried out

The following routes were taken to address the development of the project
* Analysis of the requirement and its complexity
* Find the differences between algorithmic complexities
* Consume the resources and apply an optimal solution
* Deliver the result in two alternatives, a simple solution and another with an additional proposal to the challenge:
    {
        "alternativa1 " : "The simple execution of the request with a single python file, using the request library and json, where a value is entered by the console and the expected result is delivered",

        "alternativa2" : "It is proposed to deliver the data in an API, for the ease of viewing the data, resources such as fastapi import, routes, JSONResponse uvicorn are used",

        "both": "The test library is used"
    }

# Data and requirements for algorithmic solution

In the sent repository you will find a folder with the name of algorithmic_solution.
You must execute the file in the terminal or with the python interpreter, you just have to run it by executing:
    py nba-main.py
        - There in the console the numerical value is requested to enter and deliver the result

# Data for API

Important, an api is made with the fast api resource with the aim of facilitating the verification of the information set, taking into account the comments and recommendations and notes that will be delivered in this documentation.

The api was deployed on heroku, AND IT IS AVAILABLE SO THAT IT CAN BE CONSUMED FROM ANYWHERE

1. In the url that is consumed in the api, the following must be taken into account: https://nba-api-challenge.herokuapp.com/api/v1/find_heights_nba/
    a. You can test the data through any client for example POSTMAN
    b. Enter the following url ->
    c. The method type is POST
    d. The body is type (raw) and must be sent with example json type format
        {
            "height_target": 154
        }
    and. The result will be delivered in json type of the results found

# data for test

In the test directory of the project there is a test_nba_api.py file. Tests are created to validate AND/OR PERFORM the tests of the data that must be searched and those that the user would type.


# IMPLEMENTATION - Requirements to deploy the entire solution locally with API
1. To test only the algorithmic solution -> PYTHON 3 or higher
2. To deploy the project locally you must have docker installed

    - Raise the project -> docker-compose up
    - Then go to http://localhost:8000/docs
    - Run tests, to run the following command you must be in the project directory at the same level as the docker-compose.yml file
    - docker-compose run api_nba_service pytest tests