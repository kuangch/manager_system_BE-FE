#!/usr/bin/env python2.7
# encoding: utf-8
# Copyright (c) 2016 Dilusense Inc. All Rights Reserved.

"""a file for deployment automatically"""

import os
import re
import compileall
import shutil
import subprocess
import sys
import getopt

import time
from utils.my_constant import MyConstant


class globals():
    PROJECT_NAME = 'cooperate_web'
    GIT_REPOS_PATH = '/project/' + PROJECT_NAME + '/backend'

    curr_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))

    VERSION_INFO_V = 'v0.1'
    VERSION_INFO_T = time.strftime('%Y-%m-%d %H:%M', time.localtime(time.time()))



def get_src_path():
    user_dir = os.environ['HOME']
    git_path = user_dir + globals.GIT_REPOS_PATH
    return git_path

def get_output_path():
    user_dir = os.environ['HOME']
    p = subprocess.Popen(['git', 'describe', '--tags'], stdout=subprocess.PIPE)
    tag = p.stdout.readline()
    p.wait()
    if tag == '':
        globals.VERSION_INFO_V = 'develop'
    else:
        if len(tag) > 10:
            globals.VERSION_INFO_V = tag[:-10]
        else:
            globals.VERSION_INFO_V = tag[:-1]
    return user_dir + '/build/' + globals.PROJECT_NAME + '/R' + globals.curr_time + '_' + globals.VERSION_INFO_V + '/release/'


def update_git():
    src_path = get_src_path()
    os.chdir(src_path)

    # p = subprocess.Popen(['git', 'checkout', 'master'], stdout=subprocess.PIPE)
    # print p.stdout.readline()
    # p.wait()

    p = subprocess.Popen(['git', 'pull'], stdout=subprocess.PIPE)
    print p.stdout.readline()
    p.wait()


def build_local(src_path, dst_path, remove_conf):
    # 1.copy local
    local_path_src = src_path + '/src/app'
    readme_file_path = src_path + '/doc/readme.md'
    local_path_dst = dst_path + '/' + globals.PROJECT_NAME
    log_path = local_path_dst + '/log'

    # delete project path
    remove_dir(local_path_dst)

    # copy project path
    shutil.copytree(local_path_src, local_path_dst)

    if os.path.exists(readme_file_path):
        shutil.copy(readme_file_path, local_path_dst)

    # delete log path
    remove_dir(log_path)

    # if path.exists(log_path) is False:
    #     print('create path %s ...' % (str(log_path)))
    #     os.makedirs(log_path)

    # 删除本地调试用的rawdata
    remove_dir(local_path_dst + '/static/rawdata')

    # change version of project
    change_version(local_path_dst + os.sep + 'version_info.py')

    # 4.compile file and delete .py file
    compileall.compile_dir(local_path_dst)

    # modify config file
    modify_config_file(local_path_dst + '/config/app_config.conf')

    # deleted all .py files
    print 'remove .py file...'
    delete_py_file(local_path_dst)
    print 'remove .py file completed'

    if remove_conf:
        delete_config_file(local_path_dst + '/config/app_config.conf')


def change_version(version_file_path):
    version_file = open(version_file_path, 'r')
    file_object_save = None
    try:
        stringsave = "VERSION_INFO = '" + globals().VERSION_INFO_V + "@" + globals().VERSION_INFO_T + "'"
        file_object_save = open(version_file_path, 'w')
        file_object_save.write(stringsave)
        print('modify version file success')
    finally:
        version_file.close()
        if file_object_save:
            file_object_save.close()


def modify_config_file(path):

    rawdata_path = "/var/data"
    cfg_file = open(path, 'r')
    file_object_save = None
    try:
        stringsave=""
        stringread=cfg_file.readline()
        while stringread:
            if re.findall("logger_level = (.*?)", stringread):
                print('change logger level to INFO')
                stringread='logger_level = INFO' + os.linesep
            if re.findall("is_debug = (.*?)", stringread):
                print('change project form debug to release')
                stringread='is_debug = false' + os.linesep
            if re.findall("rawdata_path = (.*?)", stringread):
                print('change rawdata_path to ' + rawdata_path)
                stringread='rawdata_path = ' + rawdata_path + os.linesep
            if re.findall("login_status_lifetime = (.*?)", stringread):
                print('change login_status_lifetime to ' + str(MyConstant.web_config_login_status_lifetime_default))
                stringread='login_status_lifetime = ' + str(MyConstant.web_config_login_status_lifetime_default) + os.linesep


            stringsave=stringsave+stringread
            stringread=cfg_file.readline()

        file_object_save = open(path, 'w')
        file_object_save.write(stringsave)
        print('modify config file success')
    finally:
        cfg_file.close()
        if file_object_save:
            file_object_save.close()


def remove_dir(path):
    if os.path.exists(path) is True:
        print('exist path %s deleting...' % (str(path)))
        shutil.rmtree(path)
        print('deleted path %s success' % (str(path)))


def delete_config_file(file_path):
    print('delete config file: %s' % (str(file_path)))
    if os.path.exists(file_path):
        os.remove(file_path)

def delete_py_file(root_dir):
    """ deleted file end with .py
    Returns:
        False if failed
        True if success
    """

    dirs = os.listdir(root_dir)
    for path in dirs:

        if path == 'test':
            print 'remove dir : %s/%s' % (str(root_dir), str(path))
            shutil.rmtree(root_dir + '/' + path)
            continue
        path = root_dir + '/' + path
        if os.path.isfile(path):
            if path.endswith('.py'):
                os.remove(path)
        else:
            delete_py_file(path)


def build(src_path, dst_path, remove_conf=False):
    print '--------------------------------------------------------------------'
    print '| build release begin!'
    print('| src build dir : ' + src_path)
    print '--------------------------------------------------------------------'

    build_local(src_path, dst_path, remove_conf)

    print '--------------------------------------------------------------------'
    print('| project file all build to dir : ' + dst_path)
    print '| build release finish!'
    print '--------------------------------------------------------------------'


def Usage(src, dst):
    print 'usage:'
    print '-h,--help: print help message.'
    print '--src: The source directory.default is : ' + src
    print '--dst: The Destination directory.default is : ' + dst
    print '--pull: The if pull code from repos .default is : false'
    print '--rm-conf: if remove config file of project .default is : false'


def main(argv):

    src = get_src_path()
    dst = get_output_path()
    is_pull_code = 'false'
    is_remove_conf = 'false'

    try:
        opts, args = getopt.getopt(argv[1:], 'h:', ['output=', 'src=', 'dst=', 'pull=', 'local=', 'rm-conf='])

    except getopt.GetoptError, err:
        print str(err)
        Usage(src, dst)
        sys.exit(2)
    for o, a in opts:
        if o in ('-h', '--help'):
            Usage(src, dst)
            sys.exit(1)
        elif o in ('-s', '--src'):
            src = a
        elif o in ('-d', '--dst'):
            dst = a
        elif o in ('-p', '--pull'):
            is_pull_code = a
        elif o in ('-r', '--rm-conf'):
            is_remove_conf = a
        else:
            print 'unhandled option'
            sys.exit(3)
    if os.path.exists(src) is False:
        print "src path does not exist!"
    else:
        if is_pull_code == 'true':
            update_git()

        if is_remove_conf == 'true':
            build(src, dst, True)
        else:
            build(src, dst, False)


if __name__ == '__main__':

    main(argv=sys.argv)

    # os.system('cp -r %s /mnt/public/3d_info_portal/build/' % (globals.OUT_PATH + '/release/local'))
    #
    # print('| copy local dir to : /mnt/public/3d_info_portal/build/')
    # print '----------------------------------------------------------'
    #
    # p = subprocess.Popen(['git', 'checkout', 'dev'], stdout=subprocess.PIPE)
    # print p.stdout.readline()
    # p.wait()
