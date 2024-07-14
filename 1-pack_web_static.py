#!/usr/bin/python3
"""
This script generates a .tgz archive.
"""

from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.
    Returns:
        The archive path otherwise none.
    """
    local("mkdir -p versions")
    now = datetime.now()
    archive_name = "versions/web_static_{}.tgz".format(
        now.strftime("%Y%m%d%H%M%S"))
    command = "tar -cvzf {} web_static".format(archive_name)

    result = local(command)
    if result.failed:
        return None
    return archive_name
