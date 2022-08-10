import requests

# url = 'https://api.github.com/repos/coriography/cello_tree/collaborators'

# headers = {'Authorization': 'token ' + ''}  # cello tree token
# headers = {'Authorization': 'token ' + ''}
# collaborators = requests.get(url, headers=headers).json()
# print(collaborators)


class RepoData:

    def __init__(self, owner, repo, auth_token=''):
        self.owner = owner
        self.repo = repo
        self.headers = {'Authorization': 'token ' + auth_token}

    def __repr__(self):
        return f'Instance of RepoData created where owner={self.owner} and repo={self.repo}'

    def get_collaborator_usernames(self):
        url = f'https://api.github.com/repos/{self.owner}/{self.repo}/collaborators'
        collaborators = requests.get(url, headers=self.headers).json()
        usernames = []
        for collaborator in collaborators:
            usernames.append(collaborator['login'])
        return usernames

    def get_collaborator_names(self):
        usernames = self.get_collaborator_usernames()
        names = []
        for username in usernames:
            url = f'https://api.github.com/users/{username}'
            user_info = requests.get(url, headers=self.headers).json()
            names.append(user_info['name'])
        return names


