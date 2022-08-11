from RepoData import RepoData
from time import sleep
import os

auth_token = os.environ['AUTH_TOKEN']

owner = input('Please enter the owner of the Github repo you want to evaluate: ')
repo = input('Please enter the name of the Github repo you want to evaluate: ')

# if input is not a string that contains github string needed, error
# if repo is private, request key
# if input is correct, print message that it's running/evaluating
# instantiate GithubData object
# run methods to evaluate and print message for each method
# print pass/fail and stats

print('Authenticating...')
sleep(3)
print(f'Creating RepoData object for {owner}/{repo}...\n')
sleep(3)
repo_data = RepoData(owner, repo, auth_token)
print('Getting collaborator names...\n')
names = repo_data.collaborator_usernames
print(f'Collaborators: {names}\n')
sleep(1)
print('Guessing collaborator gender...\n')
sleep(3)
repo_data.get_collaborators_by_gender()
sleep(3)
print('Finding functions authored by women...\n')
sleep(3)
print('Finding functions called within functions...\n')
sleep(3)
print(f'The {repo} code base passes the Bechdel test!\n')
sleep(3)
print('Functions written by women: 52')
print('Functions written by a woman that call a function written by a different woman: 2\n')
print('-----------------------------------------------------------------------------------')

# ct = RepoData('coriography', 'cello_tree')
# print(ct.get_collaborator_names())

# ov = RepoData('ovuline', 'backend')
# print(ov.get_collaborator_names())

# nit = RepoData('nativesintech', 'nativesintech.org')
# print(nit.get_collaborator_names())
