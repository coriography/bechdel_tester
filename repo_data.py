import os
from enum import Enum
from collections import defaultdict
from typing import List
import requests


class GenderIdentity(str, Enum):
    """String enum representing several gender identities"""
    man = 'man'
    woman = 'woman'
    non_binary = 'non_binary'
    unknown = 'unknown'

known_contributors = {
    'Adam': GenderIdentity.man,
    'Akira': GenderIdentity.non_binary,
    'Cori': GenderIdentity.woman,
    'Cyril': GenderIdentity.man,
    'Erica': GenderIdentity.woman,
    'Lauren': GenderIdentity.woman,
    'Yaakov': GenderIdentity.man
}


class RepoData:

    def __init__(self, owner: str, repo: str) -> None:
        self.owner = owner
        self.repo = repo
        self.headers = {'Authorization': 'token ' + os.environ['AUTH_TOKEN']}
        self._collaborator_usernames = []
        self._first_names = []
        self.collaborators_by_gender = None

    def __repr__(self):
        return f'Instance of RepoData created where owner={self.owner} and repo={self.repo}'

    @property
    def collaborator_usernames(self) -> List[str]:
        if self._collaborator_usernames:
            return self._collaborator_usernames

        # Define the url which to make the request
        url = f'https://api.github.com/repos/{self.owner}/{self.repo}/collaborators'
        collaborators = requests.get(url, headers=self.headers).json()

        # Extract values from list
        result = [x['login'] for x in collaborators]

        # Save values for next time
        self._collaborator_usernames = result
        return self._collaborator_usernames

    @property
    def first_names(self) -> List[str]:

        if self._first_names:
            return self._first_names

        result = []
        for username in self.collaborator_usernames:
            url = f'https://api.github.com/users/{username}'
            user_info = requests.get(url, headers=self.headers).json()
            result.append((user_info['name'].split())[0])  # Note: This line of code is brittle

        # Override default (save values)
        self._first_names = result
        return self._first_names


    def get_collaborators_by_gender(self):
        """
        Returns dictionary of collaborators by gender.
        Hard-coded known collaborators dict for MVP - should update this to
        use Baby Names API to determine gender.

        Written as a CLI program for MVP - update print statements
        with addition of web interface.
        """

        self.collaborators_by_gender = defaultdict(list)

        for name in self.first_names:
            gender = known_contributors.get(name, GenderIdentity.unknown)
            self.collaborators_by_gender[gender].append(name)

        for key, value in self.collaborators_by_gender.items():
            print(f'{key}: {len(value)}')


    def get_functions_by_author_gender(self):
        """For MVP, get functions that appear in author's commits - i.e. last edited"""
        pass

    def get_functions_called_by_functions(self):
        pass
