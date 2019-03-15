#!/usr/bin/env python
import os
import shutil

profile_path = os.environ.get("HOME")
if profile_path is None:
    profile_path = os.environ.get('USERPROFILE')

if profile_path is None:
    print("Can't get home directory: HOME or USERPROFILE must be set"
          " in your environment")
    exit(1)

def copyIfDest(path1, path2, recursive=True):
    folder_path = path1
    if os.path.isdir(path2):
        if os.path.isdir(folder_path):
            for sub_name in os.listdir(folder_path):
                sub_path = os.path.join(folder_path, sub_name)
                sub_path2 = os.path.join(path2, sub_name)
                if sub_name[:1]!=".":
                    if os.path.isfile(sub_path):
                        shutil.copyfile(sub_path, sub_path2)
                        print("cp '" + sub_path + "' '" + sub_path2
                              + "'")
                    elif recursive:
                        copyIfDest(sub_path, sub_path2,
                                   recursive=recursive)
    else:
        print("ERROR: Not copying '" + path1 + "' for safety, since"
              + " no '" + path2 + "'")


def deploy(path):
    copyIfDest(".", path)


deploy(os.path.join(
    profile_path,
    "git/EnlivenMinetest/webapp/linux-minetest-kit/minetest/games"
    "/ENLIVEN/mods/mobs_sky")
)
deploy(os.path.join(profile_path, ".minetest/mods/mobs_sky"))
