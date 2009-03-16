#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'TracGoogleWebmasterVerifyPlugin',
    version = '0.1',
    packages = ['tracgooglewebmasterverify'],
    author = 'Martin Scharrer',
    author_email = 'martin@scharrer-online.de',
    description = "GoogleWebmasterVerify Plugin for Trac",
    url = 'http://www.trac-hacks.org/wiki/GoogleWebmasterVerifyPlugin',
    license = 'BSD',
    keywords = 'trac google webmaster verify wiki plugin',
    classifiers = ['Framework :: Trac'],
    entry_points = {'trac.plugins': ['tracgooglewebmasterverify.plugin = tracgooglewebmasterverify.plugin']}
)
