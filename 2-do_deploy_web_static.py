#!/usr/bin/python3
"""A function that generates a .tgz archive contents"""
import os
from fabric.api import runs_once, local
from datetime import datetime

env.hosts = ["100.25.14.197", "100.25.221.118"]
env.user = "ubuntu"

def do_deploy(archive_path):
    """Deploy the static files to the servers."""
    if not os.path.exists(archive_path):
        return False

    name_of_file = os.path.basename(archive_path)
    name_of_folder = name_of_file.replace(".tgz", "")
    path_of_folder = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(name_of_file))
        run("mkdir -p {}".format(path_of_folder))
        run("tar -xzf /tmp/{} -C {}".format(name_of_file, path_of_folder))
        run("rm -rf /tmp/{}".format(name_of_file))
        run("mv {}web_static/* {}".format(path_of_folder, path_of_folder))
        run("rm -rf {}web_static".format(path_of_folder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(path_of_folder))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success
