#!/usr/bin/python3
"""
This script distributes an archive to your web servers.
"""

from fabric.api import put, run, env
from os.path import exists
import sys

env.hosts = ['54.83.130.102', '52.3.253.102']


def do_deploy(archive_path):
    """
    Distributes an archive to your web servers.

    Args:
        archive_path (str): Path to the archive file to deploy.

    Returns:
        bool: True if all operations have been done correctly, otherwise False.
    """
    if not exists(archive_path):
        print(f"Error: Archive {archive_path} not found.", file=sys.stderr)
        return False

    try:
        # Extract archive filename and folder name
        file_name = archive_path.split("/")[-1]
        folder_name = file_name.split(".")[0]
        dest_path = "/data/web_static/releases/{}".format(folder_name)

        # Upload archive to /tmp/ directory
        put(archive_path, "/tmp/")

        # Create folder for new release
        run("mkdir -p {}".format(dest_path))

        # Extract archive contents
        run("tar -xzf /tmp/{} -C {}".format(file_name, dest_path))

        # Remove uploaded archive from /tmp/
        run("rm /tmp/{}".format(file_name))

        # Move contents to release folder and clean up
        run("mv {}/web_static/* {}/".format(dest_path, dest_path))
        run("rm -rf {}/web_static".format(dest_path))

        # Update symbolic link to new release
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(dest_path))

        print("New version deployed!")
        return True

    except Exception as e:
        print(f"Error deploying: {e}", file=sys.stderr)
        return False
