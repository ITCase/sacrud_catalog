#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2014 uralbash <root@uralbash.ru>
#
# Distributed under terms of the MIT license.
__version__ = "0.0.1a"

package = "pyramid_sacrud_catalog"


def includeme(config):
    config.include('pyramid_jinja2')
    config.add_jinja2_extension('jinja2.ext.with_')
    config.add_jinja2_search_path("%s:templates" % package)
    config.add_static_view('/static_%s' % package,
                           '%(package)s:static/%(package)s/' % {'package': package})

    config.include('%s.routes' % package)
    config.scan()
