====================
Django Ebay Accounts
====================

A Django app for managing Ebay accounts

Quick start
-----------

1. Add "ebay_accounts" to your INSTALLED_APPS setting::

    INSTALLED_APPS = (
        ...
        'ebay_accounts',
    )

2. Include the 'ebay_accounts' URLconf in your project urls.py::

    ...
    url(r'^ebay_accounts/', include('ebay_accounts.urls')),
    ...

3. At the `Ebay developer site`_, login, go to the `application settings` tab,
   select an environment and key and click 'Customize the eBay User Consent
   Form, Generate a RuName

 - Set the 'Accept Redirect URL' to 'https://www.example.com/ebay_accounts/finish_create' (must be https)
 - Set the 'Reject Redirect URL' to 'https://www.example.com/ebay_accounts/reject_create' (must be https)
 - Set the 'Privacy Policy URL' to 'https://www.example.com/ebay_accounts/privacy_policy' or to wherever your privacy policy is

4. Add some settings to your settings file

 - ``EBAY_SANDBOX_DEVID``, ``EBAY_SANDBOX_APPID``,
   ``EBAY_SANDBOX_CERTID`` - provided by Ebay

 - ``EBAY_PRODUCTION_DEVID``, ``EBAY_PRODUCTION_APPID``,
   ``EBAY_PRODUCTION_CERTID`` - provided by Ebay

  - set these to an empty string if you don't have them, just don't expect
    creating a production token to work

 - ``EBAY_SANDBOX_RU_NAME`` - provided by Ebay in the previous step

 - ``EBAY_PRODUCTION_RU_NAME`` - provided by Ebay in the previous step

  - again, set this to an empty string if you don't have these yet

5. Run `python manage.py migrate` (using south) to create the models.

6. Run your server and visit 'https://www.example.com/ebay_accounts/'

.. _`Ebay developer site`: http://developer.ebay.com


Running Tests
-------------

To run the tests first install some requirements::

    pip install -r requirements.txt
    python setup.py develop

Then run the tests::

    PYTHONPATH=. django-admin.py test --settings=ebay_accounts.test_settings ebay_accounts

Or alternatively, just use tox::

    pip install tox
    tox
