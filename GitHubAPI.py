############################################################
# Name:Kobe Dawes
# Pledge:I pledge my honor that I have abided by the Stevens honor system. Kobe Dawes
# SSW567 hw4
############################################################

import requests
import json

#richkempinski


def listSort(id, list):
    """takes in github ID and json list,
    then prints the repo name key alongside the amount of commits in the commit list """
    if list == [] or list == '':
        return []
    else:
        commitList = requests.get(f'https://api.github.com/repos/{id}/{list[0]["name"]}/commits')
        y2 = json.loads(commitList.text)
        return [[list[0]['name'], len(y2)]] + listSort(id, list[1:])


def getProjects(id):
    """takes in a github ID and spits out a list of repositories and their
     associated commits. e.g. [['csp', 2], ['hellogitworld', 30]]"""
    repoList = requests.get(f'https://api.github.com/users/{str(id)}/repos')
    z = json.loads(repoList.text)

    if id == '':
        return []
    else:

        return listSort(id, z)


#print(getProjects('richkempinski'))