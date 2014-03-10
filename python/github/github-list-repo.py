from github import Github
import getpass

uname = input("username: ")
password = getpass.getpass("password: ")
g = Github(uname, password)
for repo in g.get_user().get_repos():
    print(repo.name)
