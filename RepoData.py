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

    def evaluate_collaborator_gender(self):
        """Currently hard-coded for MVP - should update this to use Babynames API to determine gender"""
        known_contributors = {
            'man': ['Adam'],
            'woman': ['Cori'],
            'non-binary/gender non-conforming': [],
            'genderqueer or gender-fluid': [],
        }
        pass

    def get_first_name_from_name(self):
        pass

    def get_functions_by_author_gender(self):
        """For MVP, get functions that appear in author's commits - i.e. last edited"""
        pass

    def get_functions_called_by_functions(self):
        pass



