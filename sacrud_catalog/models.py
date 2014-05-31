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
    def m2m_category(cls):
        return relationship("CatalogCategory", backref="m2m_category2group")


class Product2Category(object):
    __tablename__ = 'sacrud_catalog_product2category'

    @declared_attr
    def product_id(cls):
        return Column(Integer, ForeignKey('sacrud_catalog_product.id'),
                      primary_key=True)

    @declared_attr
    def category_id(cls):
        return Column(Integer, ForeignKey('sacrud_catalog_category.id'),
                      primary_key=True)

    @declared_attr
    def m2m_product(cls):
        return relationship("CatalogProduct", backref="m2m_product2category")


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

    # m2m to Category
    @declared_attr
    def category(cls):
        return relationship("CatalogCategory",
                            secondary="sacrud_catalog_product2category",
                            backref="product")

    def __repr__(self):
        return self.name


class BaseCategory(Visible):
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

    def __repr__(self):
        return self.name


class BaseGroup(Visible):
    __tablename__ = 'sacrud_catalog_group'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)

    # JSON parameters
    params = Column(JSON)

    # m2m to Product

    def __repr__(self):
        return self.name


class BaseStock(Visible):
    __tablename__ = 'sacrud_catalog_stock'

    id = Column(Integer, primary_key=True)
    qty = Column(Integer)

    # JSON parameters
    params = Column(JSON)
