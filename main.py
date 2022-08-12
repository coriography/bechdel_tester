"""
Entry point for the application
"""
from repo_data import RepoData
from time import sleep
from pydantic import BaseModel, Field, validator

# Our custom stuff
from logger import LOGGER, console

# Import fancy stuff
from rich.console import Console, Group
from rich.panel import Panel
from rich.prompt import Prompt, Confirm, IntPrompt
from rich.progress import Progress, track


class RepoInfo(BaseModel):
    """
    Entry point into the program

    ToDo:
        * if input is not a string that contains github string needed, error
        * if repo is private, request key
        * if input is correct, print message that it's running/evaluating
        * instantiate GithubData object
        * run methods to evaluate and print message for each method
        * print pass/fail and stats
    """
    owner: str = Field(..., min_length=1, strip_whitespace=True, to_lower=True, description='owner of the Github repo you want to evaluate')
    repo: str = Field(..., min_length=1, strip_whitespace=True, to_lower=True, description='name of the Github repo you want to evaluate')


# --------------------------------------------

# Create a welcome banner with a welcome message
banner_message = "Bechtel Code Tester\n\nMagic Mode Activated"
console.print(Panel(banner_message), style="bold green")

# --------------------------------------------


owner = Prompt.ask("Please enter the [magenta]owner[/magenta] of the Github repo you want to evaluate")
repo = Prompt.ask('Please enter the [magenta]repo-name[/magenta] of the Github repo you want to evaluate: ')
my_repo_info = RepoInfo(owner=owner, repo=repo)

console.print(Panel(f"Proceeding to evaluate the following: {my_repo_info}"), style="bold blue")


with Progress(console=console) as progress:
    n_steps = 100
    task = progress.add_task(f"Doing a thing once", total=n_steps)
    i = 0
    while True:
        progress.advance(task)
        sleep(1/n_steps)
        i += 1

        if i > n_steps:
            break

print(f'Creating RepoData object for {my_repo_info.owner}/{my_repo_info.repo}...\n')
sleep(3)
repo_data = RepoData(my_repo_info.owner, my_repo_info.repo)
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
