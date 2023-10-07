#!/usr/bin/python3

"""Script (based on the file 2-do_deploy_web_static.py) that creates
    and distributes an archive to your web servers, using the function deploy
"""

from fabric.api import env, put, run, local
from datetime import datetime
import os

do_pack = __import__("1-pack_web_static").do_pack
do_deploy = __import__("2-do_deploy_web_static").do_deploy

env.hosts = [
            '54.160.79.52',
            '52.86.196.120'
        ]

env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def deploy():
    """Function to create and distributes an archive to your web servers
    """
    path = do_pack()
    if path is None:
        return (False)

    return (do_deploy(path))
