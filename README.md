# Github Client API for Branch

## Overview

The purpose of this API is to get user data from the Github API and display that data in a format that is useful for the client. If the client accesses the designated endpoint with an existing Github username, the API will return a JSON with select descriptive information about that user as well as a list of repos under that username. If the username does not exist in Github, the API will return a JSON object with a message key that says "User Not Found." Further information on how to use the API and design choices will be discussed below.

## Steps to run API locally

*These steps will only work if python3 is installed on your machine. If it is not, please refer to this [documentation on installing python3](https://realpython.com/installing-python/).*

1. Create a python3 virtual environment and activate it

	```
	$ python3 -m venv /path/to/new/virtual/environment
	$ source <venv-path>/bin/activate
	```
	
	*Note: When the virutal envrionment is activated properly, it should appear on your command line prompt in paranthesis at the beginning.*

2. Install flask in the virtualenv

	```
	$ pip install flask
	```

3. Install requests library in the virtualenv:

	```
	$ pip install requests
	```

4. Clone the repository

	```
	$ git clone https://github.com/minasucur/branch.git
	```
	
5. Run the API with flask

	First go into the repo folder then run:

	```
	$ export FLASK_APP=github_api.py
	$ flask run
	```
	
	This should give you a message that looks something like this:
	
	```
	 * Serving Flask app "github_api.py"
	 * Environment: production
	   WARNING: This is a development server. Do not use it in a production deployment.
	   Use a production WSGI server instead.
	 * Debug mode: off
	 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
	```

6. 	Open a browser of your choice and navigate to `http://127.0.0.1:5000/users/<username>` with the username of your choice. At this point, you should see the returned JSON.

7. When you are done using the API, you can press `CTRL+C` to quit. And to deactivate the virtual environment just type `deactivate`.

## Design Choices

### Python
Python is a high-level and flexible coding language that can be used for many purposes such as this API and there are extensive libraries and frameworks. However, I ultimately chose python because it is the language I am most comfortable with at this time.

### Flask
Flask is a Python micro-framework used to build APIs. It is a good choice for the base of this API because it's simple to use and gives you complete flexibility on how to build your application. Alot can be accomplished with Flask with not many lines of code, so it makes the code very easy to understand and use. Routing to specific endpoints within the app takes only one line of code and you can work with variables very easily as well. Also, running the code itself is super quick and simple.

### Requests library
The python requests libary is a great choice for gathering data from an existing API. I decided to use this library to access the Github API and get the user JSONs needed to create this application for Branch. The requests library allows you to access a JSON response like a dictionary structure, making it very easy to manipulate.

### Disabling JSON\_SORT_KEYS in Flask configuration
I decided to disable JSON key sorting in this app to maintain the ordering of the JSON keys that the client is requesting in the example. Without this line, keys in the final JSON will be in alphabetical order.

### Check for existing user
I added two checks for bad input within the API code. One is checking for a successful HTTP request to the Github API. This check is just for extra precaution in case of any HTTP Errors. However, when a user does not exist, it seems that the Github API returns a JSON with a message element stating "Not Found." So to account for this, I added a simple conditional to check whether either python request returns a message of "Not Found." 

### Formatting the creation date
To correct the formatting of the `created_at` date to match what the client is requesting in the example, I simply got rid of the `Z` and `T` elements in the date string. I chose to do it this way instead of using the datetime library, because it only requires getting rid of characters and not rearranging or adding characters, so it was the most simple way to accomplish this.

### Jsonify
Jsonify is a function that is part of the Flask framework. It simply creates a JSON object out of the elements passed to it with the proper headers.
