#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Pyramid application that redirects any GET request to another domain.

In your configuration file add a line such as this::

    scheme_domain_port = http://dev.nando.audio

"""

from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from pyramid.config import Configurator
from pyramid.httpexceptions import HTTPMovedPermanently


def redirect_to_other_domain(request):
    """View that redirects to another domain, keeping the rest of the URL."""
    scheme_domain_port = request.registry.settings['scheme_domain_port']
    return HTTPMovedPermanently(scheme_domain_port + request.path_qs)


def main(global_config, **settings):
    """Return the WSGI application at startup."""
    config = Configurator(settings=settings)
    config.add_route('catchall', '/*subpath')
    config.add_view(redirect_to_other_domain, route_name='catchall')
    return config.make_wsgi_app()
