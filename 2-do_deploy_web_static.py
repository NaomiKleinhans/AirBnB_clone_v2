#!/usr/bin/python3
"""
This script distributes an archive to your web servers, using the function do_deploy.
"""

from fabric.api import put, run, env
from os.path import exists

env.hosts = ['54.83.130.102', '52.3.253.102']


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.
    Returns:
        True if all operations have been done correctly, otherwise False.
    """
    if not exists(archive_path):
        return False

    file_name = archive_path.split("/")[-1]
    folder_name = file_name.split(".")[0]
    dest_path = "/data/web_static/releases/{}".format(folder_name)

    try:
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(dest_path))
        run("tar -xzf /tmp/{} -C {}".format(file_name, dest_path))
        run("rm /tmp/{}".format(file_name))
        run("mv {}/web_static/* {}/".format(dest_path, dest_path))
        run("rm -rf {}/web_static".format(dest_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dest_path))
        return True
    except:
        return False
