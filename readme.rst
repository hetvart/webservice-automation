=============
Main concept:
=============
The main goal of this library is to implement functional automation testing framework on the webservice_.

.. _webservice: http://www.webservicex.net/country.asmx

Test Runner:
------------

Use *test_runner.py* file to run your tests. It takes as an argument *.json* config file
with a list of test modules names your are going to run.

*.json* file looks like the below one:


.. code-block:: json

    {
      "test suites": ["tests.test_country_service"]
    }

See the below example of how to run tests:
.. code-block:: sh

    $ python test_runner.py configs/config.json

