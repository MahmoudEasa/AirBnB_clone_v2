#!/usr/bin/python3

"""Script (based on the file 3-deploy_web_static.py) that deletes
    out-of-date archives, using the function do_clean
"""


env.hosts = [
            '54.160.79.52',
            '52.86.196.120'
        ]

env.user = "ubuntu"

def do_clean():
    """Function to delete out-of-date archives
    """

