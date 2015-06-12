#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" A script to manage development tasks """

from os import path as p
from manager import Manager
from subprocess import call

manager = Manager()
_basedir = p.dirname(__file__)


@manager.command
def clean():
    """Remove all artifacts"""
    clean_build()
    clean_pyc()


@manager.command
def check():
    """Check staged changes for lint errors"""
    return call(p.join(_basedir, 'helpers', 'check-stage'), shell=True)


@manager.command
def lint():
    """Check style with flake8"""
    return call('flake8 ckan-utils test', shell=True)


@manager.command
def pipme():
    """Install requirements.txt"""
    call('pip install -r requirements.txt', shell=True)


@manager.command
def require():
    """Create requirements.txt"""
    cmd = 'pip freeze -l | grep -vxFf dev-requirements.txt > requirements.txt'
    call(cmd, shell=True)


@manager.command
def test():
    """Run nose and script tests"""
    return call(p.join(_basedir, 'helpers', 'test'), shell=True)


@manager.command
def release():
    """Package and upload a release"""
    return call(p.join(_basedir, 'helpers', 'release'), shell=True)


@manager.command
def sdist():
    """Create a source distribution package"""
    return call(p.join(_basedir, 'helpers', 'sdist'), shell=True)


@manager.command
def wheel():
    """Create a wheel package"""
    return call(p.join(_basedir, 'helpers', 'wheel'), shell=True)


if __name__ == '__main__':
    manager.main()
