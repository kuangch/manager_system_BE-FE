#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

"""a file for deployment automatically"""

import os
from build_release import globals,get_output_path ,remove_dir


def release_to(dist):
    project_dir = get_output_path() + globals.PROJECT_NAME
    dist_dir = dist
    if os.path.exists(dist_dir):
        remove_dir(dist_dir)
    os.system('cp -r %s %s' % (project_dir, dist_dir))

    print('copy local dir to : %s' % (dist_dir))
    print '----------------------------------------------------------'


if __name__ == '__main__':

    # os.system('python build_release.py --rm-conf=true')
    os.system('python build_release.py')

    release_to(os.environ['HOME'] + '/build/'+globals.PROJECT_NAME+'/' + globals.PROJECT_NAME)