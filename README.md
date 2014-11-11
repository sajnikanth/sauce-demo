Introduction
============

This is a demo for running selenium and [holmium](http://holmiumcore.readthedocs.org) tests on [Saucelabs](https://saucelabs.com)

Pre-Requisites
==============
* Account on [Saucelabs](https://saucelabs.com) with available minutes
    * Keep username and Access Key (found on [accounts page](https://saucelabs.com/account)) handy
* firefox
* On OSX

        sudo easy_install pip && \
        sudo pip install nose selenium sauceclient holmium.core
* On Ubuntu

        sudo apt-get install python-pip -y && \
        sudo pip install nose selenium sauceclient holmium.core

* On Windows
    * Download and install [python 2.7](https://www.python.org/download/releases/2.7.7/)
    * Install [pip](http://stackoverflow.com/questions/4750806/how-to-install-pip-on-windows)
    * Using `pip`, install the following

            pip install nose selenium sauceclient holmium.core

Run
===

Run test using selenium locally using firefox:

    nosetests tests/selenium_vistaprint_test.py -v --nologcapture

Run test using selenium on windows 8 - chrome with sauce:

    nosetests tests/selenium_vistaprint_test.py -v --nologcapture\
     -cred=<ENTER SAUCE USERNAME>:<ENTER SAUCE ACCESS KEY>

Run test using holmium plugin on OSX - safari with sauce:

    nosetests tests/holmium_vistaprint_test.py -v --nologcapture\
     --with-holmium --holmium-browser=firefox --holmium-environment=http://vistaprint.com\
     --holmium-remote=http://<ENTER SAUCE USERNAME>:<ENTER SAUCE ACCESS KEY>@ondemand.saucelabs.com:80/wd/hub\
     --holmium-capabilities='{"platform":"OS X 10.10", "name":"vistaprint_login"}'
