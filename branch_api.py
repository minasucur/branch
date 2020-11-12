import flask
import os
import requests

from flask import Flask
from flask import jsonify

app = flask.Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

@app.route('/users/<username>', methods=['GET'])
def user(username):
    """Pull user data from github api and return JSON with client data

    :param username: str - client username
    :return: JSON object with client data

    """
    github_user_api = os.path.join("https://api.github.com/users", username)
    github_repo_api = os.path.join(github_user_api, "repos")
    try:
        user_data = requests.get(github_user_api).json()
        repos_data = requests.get(github_repo_api).json()
    except HTTPError:
        return jsonify(message="User Not Found")
    if user_data["message"] == "Not Found" or repos_data["message"] == "Not Found":
        return jsonify(message="User Not Found")
    repos = []
    for repo in repos_data:
        repos.append({"name": repo["name"], "url": repo["html_url"]})
    formatted_date = user_data["created_at"].replace("T", " ").replace("Z", "")
    client_data = jsonify(
                    user_name=user_data["login"],
                    display_name=user_data["name"],
                    avatar=user_data["avatar_url"],
                    geo_location=user_data["location"],
                    email=user_data["email"],
                    url=user_data["html_url"],
                    created_at=formatted_date,
                    repos=repos
                   )
    return client_data
