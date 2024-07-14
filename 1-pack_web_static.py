#!/usr/bin/python3
"""
This script generates a .tgz archive from the contents of the web_static folder.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns:
        The archive path if the archive has been correctly generated. Otherwise, None.
    """
    # Create versions directory if it doesn't exist
    local("mkdir -p versions")

    now = datetime.now()
    # Construct archive name based on current timestamp
    archive_name = "versions/web_static_{}.tgz".format(
        now.strftime("%Y%m%d%H%M%S"))

    # Construct tar command to compress web_static folder
    command = "tar -cvzf {} web_static".format(archive_name)

    # Execute tar command locally
    result = local(command)

    # Check if command execution failed
    if result.failed:
        return None

    # Return path to generated archive
    return archive_name
