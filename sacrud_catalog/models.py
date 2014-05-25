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
from sqlalchemy import Boolean, Column, Integer, String, ForeignKey
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm import relationship

Base = declarative_base()


class Visible(object):
    visible = Column(Boolean)


class Category2Group(object):
    __tablename__ = 'sacrud_catalog_category2group'

    @declared_attr
    def group_id(cls):
        return Column(Integer, ForeignKey('sacrud_catalog_group.id'),
                      primary_key=True)

    @declared_attr
    def category_id(cls):
        return Column(Integer, ForeignKey('sacrud_catalog_category.id'),
                      primary_key=True)

    @declared_attr
    def category(cls):
        return relationship("CatalogCategory", backref="category")


class BaseProduct(Visible):
    """ JSON parameters

        format:
            {"size": {"type": "list",
                      "value": (39, 40, 41, 42, 43, 44)
                     },
             "color": {"type": "choice",
                       "value": ("red", "green", "blue", "black", "white")
                       },
             "weight": {"type": "number",
                        "value": "",
                        "metric": "kg"
                        },
            }
    """
    __tablename__ = 'sacrud_catalog_product'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    params = Column(JSON)

    def __repr__(self):
        return self.name


class BaseCategory(object):
    __tablename__ = 'sacrud_catalog_category'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    abstract = Column(Boolean)

    # m2m to Group
    @declared_attr
    def group(cls):
        return relationship("CatalogGroup",
                            secondary="sacrud_catalog_category2group",
                            backref="category")


class BaseGroup(Visible):
    __tablename__ = 'sacrud_catalog_group'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # JSON parameters
    params = Column(JSON)

    # m2m to Product


class BaseStock(Visible):
    __tablename__ = 'sacrud_catalog_stock'

    id = Column(Integer, primary_key=True)
    qty = Column(Integer)

    # JSON parameters
    params = Column(JSON)
