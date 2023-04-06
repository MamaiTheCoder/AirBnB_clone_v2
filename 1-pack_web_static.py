#!/usr/bin/python3
"""A function that generates a .tgz archive contents"""
import os
from fabric.api import runs_once, local
from datetime import datetime


@runs_once
def do_pack():
    """Archives the static files."""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    current_time = datetime.now()
    output = "versions/web_static_{}{}{}{}{}{}.tgz".format(
             current_time.year,
             current_time.month,
             current_time.day,
             current_time.hour,
             current_time.minute,
             current_time.second
             )
    try:
        print("Packing web_static to {}".format(output))
        local("tar -cvzf {} web_static".format(output))
        archize_size = os.stat(output).st_size
        print("web_static packed: {} -> {}Bytes".format(output, archize_size))
    except Exception:
        output = None
    return output
