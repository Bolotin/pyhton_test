import yaml
from os import path


def create_env_list(listname, data, directory='env_lists/'):
    """Expect name of new yaml file (directory is optional)
    and dictionaty of dictionaries as network devices data"""
    listname = directory + listname
    if path.exists(listname):
        answer = input('The list with the name exists. Do you want rewrite it (Y/N)')
        if answer not in ['Y', 'y', 'yes']:
            return False
    with open(listname, 'w+') as file:
        yaml.dump(data, file, default_flow_style=False)
    return True


def get_env_list(listname, directory='env_lists/'):
    """Expect name of existing yaml file (directory is optional)
    and return the dictionary of dictionaries (for netmiko)"""
    listname = directory + listname
    if not path.exists(listname):
        print('LOG: get_env_list: This listname is not exists.')
        return False
    with open(listname) as file:
        return(yaml.load(file))
