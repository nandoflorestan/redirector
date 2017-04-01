==========
redirector
==========

This is a (very small) Pyramid application that does one thing only:

It redirects any incoming GET requests to another domain. Or actually,
to another combination of protocol, domain and port.

For more details, please see the redirector/ subdirectory.


Deploying on Webfaction
=======================

Here is how I deploy this on http://www.webfaction.com.

First I go into Webfaction's control panel and create an application of type
"Custom app (listening on port)".

Then::

    cd webapps/redirector      # Go into the directory of our application.
    pyvenv-3.5 venv            # Create a virtual environment with Python 3.5
    source venv/bin/activate   # Enter our new virtual environment

    # Install some Python packages:
    venv/bin/easy_install pyramid ipdb

    # Install redirector
    venv/bin/pip install git+https://github.com/nandoflorestan/redirector.git

