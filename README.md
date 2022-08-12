# Bechdel Code Tester
About this project.

## Getting started:

1. Create a clone of this repository: _(only do 1st time)_
```
git@github.com:coriography/bechdel_tester.git
```
2. Set current working directory to repository:
```
cd bechdel_tester
```
3. create a virtual environment _(only do 1st time)_
```
python3 -m venv venv
```
4. activate the virtual environment
```
source venv/bin/activate
```
5. install requirements _(only do 1st time)_
```
pip install -r requirements.txt
```
6. Generate a github access token:
* Follow steps 1-9 on this guide: [Creating a personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)
* For scopes (Step 8), select the following:
  * `public_repo`
  * `read_user`

> Note: Keep the value of this token a secret! Definitely make sure that it
is never included in a commit anywhere.

7. Save that access token as an environment variable `AUTH_TOKEN`:
```
# secrets.sh
export AUTH_TOKEN='the_code_just_generated'
```

8. Go and run the code!
```
python3 main.py
```
