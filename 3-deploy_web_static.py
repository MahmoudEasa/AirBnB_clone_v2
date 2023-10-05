#!/usr/bin/python3

"""Script (based on the file 2-do_deploy_web_static.py) that creates
    and distributes an archive to your web servers, using the function deploy
"""

from fabric.api import env, put, run, local
from datetime import datetime
import os

env.hosts = [
            '54.160.79.52',
            '52.86.196.120'
        ]

env.user = "ubuntu"
env.key_filename = "~/.ssh/id_rsa"


def do_pack():
    """Function to generate a .tgz archive
    """
    date_time = datetime.now().strftime("%Y%m%d%H%M%S")
    archive_path = f"versions/web_static_{date_time}.tgz"
    cmd = f"tar -cvzf {archive_path} web_static"

    if not os.path.exists("versions"):
        os.makedirs("versions")

    if local(cmd).failed is True:
        return (None)
    return (archive_path)


def do_deploy(archive_path):
    """Function to distribute an archive to web servers
    """
    if not os.path.exists(archive_path):
        return (False)

    archive_name = archive_path.split('/')[-1]
    name = archive_name.split('.')[0]
    uncompress_path = f"/data/web_static/releases/{name}"
    uncompress_cmd = f"tar -xzf /tmp/{archive_name} -C {uncompress_path}"
    create_path = f"mkdir -p {uncompress_path}"
    remove_archive = f"rm -rf /tmp/{archive_name}"
    move = f"mv {uncompress_path}/web_static/* {uncompress_path}"
    remove_web_static = f"rm -rf {uncompress_path}/web_static"
    link_archive = f"ln -s {uncompress_path} /data/web_static/current"

    if put(archive_path, '/tmp/').failed is True:
        return (False)
    if run(create_path).failed is True:
        return (False)
    if run(uncompress_cmd).failed is True:
        return (False)
    if run(remove_archive).failed is True:
        return (False)
    if run(move).failed is True:
        return (False)
    if run(remove_web_static).failed is True:
        return (False)
    if run("rm -rf /data/web_static/current").failed is True:
        return (False)
    if run(link_archive).failed is True:
        return (False)
    return (True)


def deploy():
    """Function to create and distributes an archive to your web servers
    """
    path = do_pack()
    if path is None:
        return (False)

    return (do_deploy(path))
