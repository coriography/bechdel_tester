import requests

# url = 'https://api.github.com/repos/coriography/cello_tree/collaborators'

# headers = {'Authorization': 'token ' + ''}  # cello tree token
# headers = {'Authorization': 'token ' + ''}
# collaborators = requests.get(url, headers=headers).json()
# print(collaborators)

man = 'man'
woman = 'woman'
non_binary = 'non_binary'
unknown = 'unknown'
known_contributors = {
    'Adam': man,
    'Akira': non_binary,
    'Cori': woman,
    'Cyril': man,
    'Erica': woman,
    'Lauren': woman,
    'Yaakov': man
}


class RepoData:

    def __init__(self, owner, repo, auth_token=''):
        self.owner = owner
        self.repo = repo
        self.headers = {'Authorization': 'token ' + auth_token}
        self.collaborator_usernames = None
        self.first_names = None
        self.collaborators_by_gender = None

    def __repr__(self):
        return f'Instance of RepoData created where owner={self.owner} and repo={self.repo}'

    def get_collaborator_usernames(self):
        url = f'https://api.github.com/repos/{self.owner}/{self.repo}/collaborators'
        collaborators = requests.get(url, headers=self.headers).json()
        self.collaborator_usernames = []
        for collaborator in collaborators:
            self.collaborator_usernames.append(collaborator['login'])
        return self.collaborator_usernames

    def get_collaborator_first_names(self):
        if self.collaborator_usernames is None:
            self.get_collaborator_usernames()
        self.first_names = []
        for username in self.collaborator_usernames:
            url = f'https://api.github.com/users/{username}'
            user_info = requests.get(url, headers=self.headers).json()
            self.first_names.append((user_info['name'].split())[0])
        return self.first_names

    def get_collaborators_by_gender(self):
        """
        Returns dictionary of collaborators by gender.
        Hard-coded known collaborators dict for MVP - should update this to use Baby Names API to determine gender.
        Written as a CLI program for MVP - update print statements with addition of web interface.
        """
        if self.first_names is None:
            self.get_collaborator_first_names()

        self.collaborators_by_gender = {
            woman: [],
            non_binary: [],
            man: [],
            unknown: []
        }

        for name in self.first_names:
            if name in known_contributors:
                gender = known_contributors[name]
                self.collaborators_by_gender[gender].append(name)
            else:
                self.collaborators_by_gender[unknown].append(name)

        print(f'women: {len(self.collaborators_by_gender[woman])}')
        print(f'men: {len(self.collaborators_by_gender[man])}')
        print(f'non-binary: {len(self.collaborators_by_gender[non_binary])}')
        print(f'unknown: {len(self.collaborators_by_gender[unknown])}')
        print('\n')

    def get_functions_by_author_gender(self):
        """For MVP, get functions that appear in author's commits - i.e. last edited"""
        pass

    def get_functions_called_by_functions(self):
        pass
