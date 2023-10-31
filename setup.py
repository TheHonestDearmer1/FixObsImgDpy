#! /usr/bin/env python
# -*- coding: utf-8 -*-
import re

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

    version = "1.0"

with open("README.md", "r", encoding='utf-8') as fh:
    long_description = fh.read()

setup(
    name='FixObsImgDpy',  # 包的名字
    author='TheHonestDreamer',  # 作者
    version='0.1.0',  # 版本号
    license='MIT',

    description='Fix "<img>" display issues in obsidian ',  # 描述
    long_description='''long description''',
    author_email='2356371636@qq.com',  # 你的邮箱**
    url='https://github.com/TheHonestDearmer1',  # 可以写github上的地址，或者其他地址
    # 包内需要引用的文件夹
    # packages=setuptools.find_packages(exclude=['url2io',]),
    # keywords='NLP,tokenizing,Chinese word segementation',
    # package_dir={'jieba':'jieba'},
    # package_data={'jieba':['*.*','finalseg/*','analyse/*','posseg/*']},

    classifiers=[
        # 'Development Status :: 4 - Beta',
        # 'Operating System :: Microsoft'  # 你的操作系统  OS Independent      Microsoft
        'Intended Audience :: Developers',
        # 'License :: OSI Approved :: MIT License',
        # 'License :: OSI Approved :: BSD License',  # BSD认证
        'Programming Language :: Python',  # 支持的语言
        'Programming Language :: Python :: 3',  # python版本 。。。
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python',  # 支持的语言
        'Programming Language :: Python :: 3.7',  # python版本 。。。
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Topic :: Software Development :: Libraries'
    ],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'FixObsImgDpy = FixObsImgDpy:run',
        ],
    }
)