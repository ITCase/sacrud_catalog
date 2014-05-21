#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.

"""
Model of Pages
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class BaseProduct(object):
    __tablename__ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    def __repr__(self):
        return self.name


class BaseCategory(object):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True)


class BaseGroup(object):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)


class BaseStock(object):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
