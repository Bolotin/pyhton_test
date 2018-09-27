import yaml
import os


def create_env_list(listname, data):
    """Expect name of new yaml file
    And dictionaty of dictionaries as network devices data"""
    if os.path.exists(listname):
        answer = input('The list with the name exists. Do you want rewrite it (Y/N)')

    with open()
