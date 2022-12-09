from scripts.common_util.constants import *


class API_OPERATIONS:

    def __init__(self):
        self.request_url = api_request_url

    # example request URL: https://api.github.com/search/repositories?q=test&per_page=10&page=1&sort=stars&order=desc
    # input params
    #       str  : q / keyword    
    #       int  : per_page     
    #       int  : page  ( current page in ui )
    def get_repo_details(self, keyword, per_page=10, page=0):
        url = self.request_url + 'search/repositories?q=' + str(keyword) + '&per_page=' + str(
            per_page) + '&page=' + str(page) + '&sort=stars&order=desc'
        response = requests.get(url)
        data = response.json()
        return data

    # example request URL: https://api.github.com/repos/storybookjs/storybook/commits?per_page=3&page=0
    # input params
    #       str  : git_op ( commits or forks)
    #       str  : repo_name
    #       str  : owner_name
    #       int  : per_page     
    #       int  : page  ( current page in ui )
    def get_commits_details(self, git_op, repo_name, owner_name, per_page=3, page=0):
        url = self.request_url + 'repos/' + str(repo_name) + '/' + str(owner_name) + '/' + str(
            git_op) + '?per_page=' + str(per_page) + '&page=' + str(page)
        response = requests.get(url)
        data = response.json()
        print("url")
        print(url)
        return data

    # example request URL: https://api.github.com/users/Rippyblogger
    # input params
    #       str  : name ( commits or forks)
    def get_github_bio_details(self, name):
        url = self.request_url + 'users/' + str(name)
        response = requests.get(url)
        data = response.json()
        return data

    #  function to form the json to verify for ui
    def get_configured_api_details(self, keyword, limit):

        repo_data = self.get_repo_details(keyword)
        json_data = []

        for repo in repo_data['items']:
            data = {}
            data["name"] = repo['name']
            data["owner"] = repo['owner']['login']
            data["stars"] = str(repo['stargazers_count'])
            data["link"] = repo['html_url'].replace("https://github.com/", '')

            json_data.append(data)
        return json_data

    def get_configured_repo_api_details(self, keyword, per_page, limit):
        git_repo_data = self.get_repo_details(keyword)
        json_data = []

        for i in range(limit):
            data = {}
            commit_data = self.get_commits_details("commits", git_repo_data['items'][i]['owner']['login'],
                                                   git_repo_data['items'][i]['name'])

            data['commit_details'] = ''
            for repo_data in commit_data:
                data['commit_details'] = data['commit_details'] + repo_data['committer']['login'] + ', '

            if data['commit_details'] != '':
                data['commit_details'] = data['commit_details'][:-2]

            fork_data = self.get_commits_details("forks", git_repo_data['items'][i]['owner']['login'],
                                                 git_repo_data['items'][i]['name'])
            if fork_data != []:
                data['fork_details'] = fork_data[0]['owner']['login']

                fork_bio_data = self.get_github_bio_details(data['fork_details'])
                data['fork_bio_details'] = fork_bio_data['bio']
                if data['fork_bio_details'] == None:
                    data['fork_bio_details'] = ''
            else:
                data['fork_details'] = ''
                data['fork_bio_details'] = ''

            json_data.append(data)
        return json_data
