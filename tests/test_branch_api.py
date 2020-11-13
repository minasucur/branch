import json
import requests_mock
import unittest

from branch.branch_api import user, app

USER_DATA = {
              "login": "minasucur",
              "id": 74272713,
              "node_id": "MDQ6VXNlcjc0MjcyNzEz",
              "avatar_url": "https://avatars3.githubusercontent.com/u/74272713?v=4",
              "gravatar_id": "",
              "url": "https://api.github.com/users/minasucur",
              "html_url": "https://github.com/minasucur",
              "followers_url": "https://api.github.com/users/minasucur/followers",
              "following_url": "https://api.github.com/users/minasucur/following{/other_user}",
              "gists_url": "https://api.github.com/users/minasucur/gists{/gist_id}",
              "starred_url": "https://api.github.com/users/minasucur/starred{/owner}{/repo}",
              "subscriptions_url": "https://api.github.com/users/minasucur/subscriptions",
              "organizations_url": "https://api.github.com/users/minasucur/orgs",
              "repos_url": "https://api.github.com/users/minasucur/repos",
              "events_url": "https://api.github.com/users/minasucur/events{/privacy}",
              "received_events_url": "https://api.github.com/users/minasucur/received_events",
              "type": "User",
              "site_admin": "false",
              "name": "null",
              "company": "null",
              "blog": "",
              "location": "null",
              "email": "null",
              "hireable": "null",
              "bio": "null",
              "twitter_username": "null",
              "public_repos": 1,
              "public_gists": 0,
              "followers": 0,
              "following": 0,
              "created_at": "2020-11-10T22:17:49Z",
              "updated_at": "2020-11-12T17:06:38Z"
            }
REPOS_DATA = [
              {
                "id": 311799000,
                "node_id": "MDEwOlJlcG9zaXRvcnkzMTE3OTkwMDA=",
                "name": "branch",
                "full_name": "minasucur/branch",
                "private": "false",
                "owner": {
                  "login": "minasucur",
                  "id": 74272713,
                  "node_id": "MDQ6VXNlcjc0MjcyNzEz",
                  "avatar_url": "https://avatars3.githubusercontent.com/u/74272713?v=4",
                  "gravatar_id": "",
                  "url": "https://api.github.com/users/minasucur",
                  "html_url": "https://github.com/minasucur",
                  "followers_url": "https://api.github.com/users/minasucur/followers",
                  "following_url": "https://api.github.com/users/minasucur/following{/other_user}",
                  "gists_url": "https://api.github.com/users/minasucur/gists{/gist_id}",
                  "starred_url": "https://api.github.com/users/minasucur/starred{/owner}{/repo}",
                  "subscriptions_url": "https://api.github.com/users/minasucur/subscriptions",
                  "organizations_url": "https://api.github.com/users/minasucur/orgs",
                  "repos_url": "https://api.github.com/users/minasucur/repos",
                  "events_url": "https://api.github.com/users/minasucur/events{/privacy}",
                  "received_events_url": "https://api.github.com/users/minasucur/received_events",
                  "type": "User",
                  "site_admin": "false"
                },
                "html_url": "https://github.com/minasucur/branch",
                "description": "null",
                "fork": "false",
                "url": "https://api.github.com/repos/minasucur/branch",
                "forks_url": "https://api.github.com/repos/minasucur/branch/forks",
                "keys_url": "https://api.github.com/repos/minasucur/branch/keys{/key_id}",
                "collaborators_url": "https://api.github.com/repos/minasucur/branch/collaborators{/collaborator}",
                "teams_url": "https://api.github.com/repos/minasucur/branch/teams",
                "hooks_url": "https://api.github.com/repos/minasucur/branch/hooks",
                "issue_events_url": "https://api.github.com/repos/minasucur/branch/issues/events{/number}",
                "events_url": "https://api.github.com/repos/minasucur/branch/events",
                "assignees_url": "https://api.github.com/repos/minasucur/branch/assignees{/user}",
                "branches_url": "https://api.github.com/repos/minasucur/branch/branches{/branch}",
                "tags_url": "https://api.github.com/repos/minasucur/branch/tags",
                "blobs_url": "https://api.github.com/repos/minasucur/branch/git/blobs{/sha}",
                "git_tags_url": "https://api.github.com/repos/minasucur/branch/git/tags{/sha}",
                "git_refs_url": "https://api.github.com/repos/minasucur/branch/git/refs{/sha}",
                "trees_url": "https://api.github.com/repos/minasucur/branch/git/trees{/sha}",
                "statuses_url": "https://api.github.com/repos/minasucur/branch/statuses/{sha}",
                "languages_url": "https://api.github.com/repos/minasucur/branch/languages",
                "stargazers_url": "https://api.github.com/repos/minasucur/branch/stargazers",
                "contributors_url": "https://api.github.com/repos/minasucur/branch/contributors",
                "subscribers_url": "https://api.github.com/repos/minasucur/branch/subscribers",
                "subscription_url": "https://api.github.com/repos/minasucur/branch/subscription",
                "commits_url": "https://api.github.com/repos/minasucur/branch/commits{/sha}",
                "git_commits_url": "https://api.github.com/repos/minasucur/branch/git/commits{/sha}",
                "comments_url": "https://api.github.com/repos/minasucur/branch/comments{/number}",
                "issue_comment_url": "https://api.github.com/repos/minasucur/branch/issues/comments{/number}",
                "contents_url": "https://api.github.com/repos/minasucur/branch/contents/{+path}",
                "compare_url": "https://api.github.com/repos/minasucur/branch/compare/{base}...{head}",
                "merges_url": "https://api.github.com/repos/minasucur/branch/merges",
                "archive_url": "https://api.github.com/repos/minasucur/branch/{archive_format}{/ref}",
                "downloads_url": "https://api.github.com/repos/minasucur/branch/downloads",
                "issues_url": "https://api.github.com/repos/minasucur/branch/issues{/number}",
                "pulls_url": "https://api.github.com/repos/minasucur/branch/pulls{/number}",
                "milestones_url": "https://api.github.com/repos/minasucur/branch/milestones{/number}",
                "notifications_url": "https://api.github.com/repos/minasucur/branch/notifications{?since,all,participating}",
                "labels_url": "https://api.github.com/repos/minasucur/branch/labels{/name}",
                "releases_url": "https://api.github.com/repos/minasucur/branch/releases{/id}",
                "deployments_url": "https://api.github.com/repos/minasucur/branch/deployments",
                "created_at": "2020-11-10T22:22:45Z",
                "updated_at": "2020-11-12T20:39:28Z",
                "pushed_at": "2020-11-12T20:39:25Z",
                "git_url": "git://github.com/minasucur/branch.git",
                "ssh_url": "git@github.com:minasucur/branch.git",
                "clone_url": "https://github.com/minasucur/branch.git",
                "svn_url": "https://github.com/minasucur/branch",
                "homepage": "null",
                "size": 7,
                "stargazers_count": 0,
                "watchers_count": 0,
                "language": "Python",
                "has_issues": "true",
                "has_projects": "true",
                "has_downloads": "true",
                "has_wiki": "true",
                "has_pages": "false",
                "forks_count": 0,
                "mirror_url": "null",
                "archived": "false",
                "disabled": "false",
                "open_issues_count": 0,
                "license": "null",
                "forks": 0,
                "open_issues": 0,
                "watchers": 0,
                "default_branch": "main"
              }
            ]
USER_NOT_FOUND_DATA = {
                        "message": "Not Found",
                        "documentation_url": "https://docs.github.com/rest/reference/users#get-a-user"
                      }
REPOS_NOT_FOUND_DATA = {
                        "message": "Not Found",
                        "documentation_url": "https://docs.github.com/rest/reference/repos#list-repositories-for-a-user"
                      }


class TestBranchApi(unittest.TestCase):

    def setUp(self):
        """Runs before every unit test"""

        app.config['TESTING'] = True
        self.client = app.test_client()

    def tearDown(self):
        """Runs after every unit test"""

        pass

    def test_user(self):
        """Tests user endpoint for an existing Github user"""

        with requests_mock.Mocker() as m:
            m.get("https://api.github.com/users/minasucur", status_code=200, text=json.dumps(USER_DATA))
            m.get("https://api.github.com/users/minasucur/repos", status_code=200, text=json.dumps(REPOS_DATA))

            expected_data = {
                           "user_name":"minasucur",
                           "display_name":"null",
                           "avatar":"https://avatars3.githubusercontent.com/u/74272713?v=4",
                           "geo_location":"null",
                           "email":"null",
                           "url":"https://github.com/minasucur",
                           "created_at":"2020-11-10 22:17:49",
                           "repos":[
                              {
                                 "name":"branch",
                                 "url":"https://github.com/minasucur/branch"
                              }
                           ]
                        }

            response = self.client.get("/users/minasucur")
            client_data = json.loads(response.get_data(as_text=True))
            self.assertEqual(client_data, expected_data)

    def test_user_not_found(self):
        """Tests user endpoint for a user that does not exist in Github"""

        with requests_mock.Mocker() as m:
            m.get("https://api.github.com/users/this-is-a-non-existent-user", status_code=200, text=json.dumps(USER_NOT_FOUND_DATA))
            m.get("https://api.github.com/users/this-is-a-non-existent-user/repos", status_code=200, text=json.dumps(REPOS_NOT_FOUND_DATA))

            expected_data = {
                                "message": "User Not Found"
                            }

            response = self.client.get("/users/this-is-a-non-existent-user")
            client_data = json.loads(response.get_data(as_text=True))
            self.assertEqual(client_data, expected_data)


if __name__ == '__main__':
    unittest.main()
