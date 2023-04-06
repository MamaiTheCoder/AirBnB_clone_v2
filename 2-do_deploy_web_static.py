#!/usr/bin/python3
"""Distributes an archive to the web servers.
"""
import os
from fabric.api import run_once, run, local, put, env
from datetime import datetime

env.hosts = ["100.25.14.197", "100.25.221.118"]

@run_once
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


def do_deploy(archive_path):
    # Deploy the static files to the servers.
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
