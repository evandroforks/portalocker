#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

try:
    import sublime_api

except ImportError:
    from installer.setup import install
    install()
