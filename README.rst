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
    venv/bin/easy_install -UZ pyramid waitress ipdb

    # Install redirector
    venv/bin/pip install git+https://github.com/nandoflorestan/redirector.git

    # Paste a production.ini configuration file
    wget https://github.com/nandoflorestan/redirector/raw/master/production.ini

    # Edit your `production.ini`
    nano production.ini
    # Set the port to the number provided by Webfaction.

Now you can run the server temporarily, just to test it::

    venv/bin/pserve production.ini

If that works, you can quit the server with CTRL+C.

Now you need to set up cron to run the server when the machine boots::

    crontab -e  # Open the crontab file in your favorite text editor.

    # Add a line similar to this one:
    @reboot exec ~/webapps/redirector/venv/bin/pserve ~/webapps/redirector/production.ini >> ~/webapps/redirector/redirector.log 2>&1 &

This page explains some of the things we do in the above line:
http://www.somacon.com/p38.php
