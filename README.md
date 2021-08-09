# python-hafb

## Instructor project
https://github.com/hugo-wsu/python-hafb

## Local installations

Login to system using: 
- Username: **txx** (xx is terminal number)
- Password: **Hello123**

Need to open `git bash` and run the following command: 
```bash
pip install pytest
```
Reload `Pycharm`

## Setup pytest to run in `Powershell`
Run the following command:
```bash
# username is your login to your session
$Env:PATH += ";C:\users\t23\appdata\roaming\python\python39\Scripts"
```
Then, run your test script
```bash
pytest -xv test_hello.py