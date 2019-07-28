import re

def parse_cfg(fiilename):
    regex = '^interface (?P<interface>\S+)'
