#!/usr/bin/python3
"""
This script generates a .tgz archive.
"""

from fabric.api import local
from datetime import datetime
import os


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns:
        The archive path otherwise none.
    """
    try:
        # Create the folder if it doesn't exist
        if not os.path.exists("versions"):
            os.makedirs("versions")

        # Current timestamp for the archive name
        now = datetime.now()
        timestamp = now.strftime("%Y%m%d%H%M%S")

        # Create the archive file name
        archive_path = "versions/web_static_{}.tgz".format(timestamp)

        # Create the .tgz file using tar
        local("tar -cvzf {} web_static".format(archive_path))

        return archive_path

    except Exception as e:
        return None