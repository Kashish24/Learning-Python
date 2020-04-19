# -*- coding: utf-8 -*-
"""
Created on Sat Apr 18 01:18:56 2020

@author: KING
"""

from instapy import InstaPy

session = InstaPy(username="<username>", password="<Password>")

session.login()

session.like_by_tags(["bmw", "mercedes"], amount=5)
