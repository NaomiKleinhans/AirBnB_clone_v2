#!/usr/bin/python3
"""
<<<<<<< HEAD
This script generates a .tgz archive.
=======
This script generates a .tgz archive
>>>>>>> 06c2e13cae15003c491aeda7f789f45b7aa905b7
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns:
<<<<<<< HEAD
        The archive path otherwise none.
=======
        The archive path. Otherwise, None.
>>>>>>> 06c2e13cae15003c491aeda7f789f45b7aa905b7
    """
    # Create versions directory if it doesn't exist
    local("mkdir -p versions")

    now = datetime.now()
    # Construct archive name based on current timestamp
    archive_name = "versions/web_static_{}.tgz".format(now.strftime("%Y%m%d%H%M%S"))

    # Construct tar command to compress web_static folder
    command = "tar -cvzf {} web_static".format(archive_name)

    # Execute tar command locally
    result = local(command)

    # Check if command execution failed
    if result.failed:
        return None

    # Return path to generated archive
    return archive_name