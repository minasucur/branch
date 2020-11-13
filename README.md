# Github Client API for Branch

## Overview

The purpose of this API is to get user data from the Github API and display the data in a format that is useful for the client. If the client accesses the designated endpoint with an existing Github username, the API will return a JSON with select descriptive information about that user as well as a list of repos under that username. If the username does not exist in Github, the API will return a JSON object with a message that says "User Not Found." Additional information on how to use the API and design choices will be discussed below.

## Steps to run API locally

*These steps will only work if python3 and git are installed on your machine. If they are not, please refer to this [documentation on installing python3](https://realpython.com/installing-python/) and this [page to download git](https://git-scm.com/downloads).*

*These are bash instructions. If you do not have bash on your system, you may need to install Linux shell or look up further instructions.*

1. Create a python3 virtual environment and activate it

	```
	$ python3 -m venv <path-to-virtual-env>
	$ source <path-to-virtual-env>/bin/activate
	```
	
	*Note: When the virutal envrionment is activated properly, it should appear on your command line prompt in paranthesis before the command prompt like this: `(venv)<path-and-user-info>$`*

2. Install flask in the virtualenv

	```
	$ pip install flask
	```

3. Install requests library in the virtualenv

	```
	$ pip install requests
	```

4. Clone the repository

	```
	$ git clone https://github.com/minasucur/branch.git
	```
	
5. Run the API with flask

	First go into the branch folder in the repo then run:

	```
	$ export FLASK_APP=branch_api.py
	$ flask run
	```
	
	This should give you a message that looks something like this:
	
	```
	 * Serving Flask app "branch_api.py"
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
Flask is a Python micro-framework used to build APIs. It is a good choice for the base of this API because it's simple to use and gives complete flexibility on how to build an application. A lot can be accomplished with Flask with little code, so it makes the code very easy to understand and use. Routing to specific endpoints within the app takes only one line of code and allows one to work with variables very easily. Also, running the code itself is super quick and simple.

### Requests library
The python requests libary is a great choice for gathering data from an existing API. I decided to use this library to access the Github API and get the user JSONs needed to create this application for Branch. The requests library allows you to access a JSON response like a dictionary structure, making it very easy to manipulate.

### Disabling JSON\_SORT_KEYS in Flask configuration
I decided to disable JSON key sorting in this app to maintain the ordering of the JSON keys that the client is requesting in the example. Without this line, keys in the final JSON will be in alphabetical order.

### Replacing backslashes
After testing the code in a Windows environment, I noticed that os.path.join added backslashes instead of forward slashes. Instead of doing string concatenation, I stuck with the os.path.join and added the replacing of backslashes with forward slashes to mitigate this issue.

### Check for existing user
I added two checks for bad input within the API code. One is checking for a successful HTTP request to the Github API. This check is just for extra precaution in case of any request errors. However, when a user does not exist, it seems that the Github API returns a JSON with a message element stating "Not Found." So to account for this, I added a simple conditional statement to check whether either of the python requests returns a "Not Found" message.

### Formatting the creation date
To correct the formatting of the `created_at` date to match what the client is requesting in the example, I simply got rid of the `Z` and `T` elements in the date string. I chose to do it this way instead of using the datetime library, because it only requires getting rid of characters and not changing format, so it was the most simple way to accomplish this.

### Jsonify
Jsonify is a function that is part of the Flask framework. It simply creates a JSON object out of the elements passed to it with the proper headers.

### Unit Tests
I decided the python builtin unittest library was the best choice to test the API. Although there is one function in the API, it needs to be tested for existing and non-existing users, so there are two unit tests. The requests mock library is also used so that the tests do not make real calls to the Github API. To run the unittests, you should have `pytest` installed and run `pytest tests/test_branch_api.py` from the root directory of the repo.
