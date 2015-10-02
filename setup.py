#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup
import os

setup(
    name='opmate',
    version='1.0.0',
    url='https://github.com/girish946/op-mate',
    author='girish joshi',
    author_email='girish946@gmail.com',
    description=('the android application written using kivy framework to operate mate desktop.'),
    license='GPLV2',
    packages=['opmate'],
    test_suite='',
    install_requires=['pyautogui' , 'clipboard'],
    keywords="operate mate-desktop remote-controller android application",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications',
        'Intended Audience :: Developers',
        'Intended Audience :: Education',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    #scripts=['r-controller']
)
