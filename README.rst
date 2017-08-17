slackperson
===========
.. image:: https://travis-ci.org/rickh94/slackperson.svg?branch=master
    :target: https://travis-ci.org/rickh94/slackperson

A simple class \(SlackPerson\) for retrieving and storing information about a
person in your slack channel from the slack api.

Installation
============
``$ python setup.py install``

You will also need the `slackclient
<https://github.com/slackapi/python-slackclient>`_ package.

Usage
=====
The ``SlackPerson`` class initializes with a username (as you would user in
an @mention) and a list of users on the channel to pull the user's info out
of.

After initialization, an instance of ``SlackPerson`` will have these
attributes:

* username: the username supplied at instantiation (if username was supplied
  with preceeding '@', it will be stripped off.)

* userid: the internal id of the user (this is useful for tagging in api
  generated messages.

* email: the user's account email address in slack

* fname: the user's first name

* lname: the user's last name


Import and use the ``SlackPerson`` class:

.. code::

  from slackperson import SlackPerson
  from slackclient import SlackClient

  sc = SlackClient(os.environ['SLACK_API_TOKEN'])
  userlist = sc.api_call('users.list')
  me = SlackPerson('myusername', userlist)

If ``myusername`` is a member of your channel (i.e. on the userlist), the
object ``me`` will now have all of the SlackPerson attributes. If not, it
will raise ``SlackDataError``.



# Tests
TBD

# Exceptions
If data passed to any SlackPerson methods are not valid, SlackDataError will
be raised.
