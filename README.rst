slackperson
===========
.. image:: https://travis-ci.org/rickh94/slackperson.svg?branch=master
    :target: https://travis-ci.org/rickh94/slackperson

.. image:: https://codecov.io/gh/rickh94/slackperson/branch/master/graph/badge.svg
  :target: https://codecov.io/gh/rickh94/slackperson


A simple class \(``SlackPerson``\) for retrieving and storing information about a
person in your slack channel from the slack api.

Installation
============
``$ pip install slackperson``

You will also need the `slackclient
<https://github.com/slackapi/python-slackclient>`_ package.

Usage
=====
The ``SlackPerson`` class can be initialized with the from_userlist method
that allows you to supply a username or userid and the output of the
users.list method to get data about a user.

After initialization, an instance of ``SlackPerson`` will have these
attributes:

* username: the username supplied at instantiation (if username was supplied
  with preceeding '@', it will be stripped off.)

* userid: the internal id of the user (this is useful for tagging in api
  generated messages.

* email: the user's account email address in slack

* fname: the user's first name

* lname: the user's last name

* team: the user's team id


Import and use the ``SlackPerson`` class:

.. code::

  from slackperson import SlackPerson
  from slackclient import SlackClient

  sc = SlackClient(os.environ['SLACK_API_TOKEN'])
  userlist = sc.api_call('users.list')
  me = SlackPerson.from_userlist('myusername', userlist)

If ``myusername`` is a member of your channel (i.e. on the userlist), the
object ``me`` will now have all of the SlackPerson attributes. If not, it
will raise ``SlackDataError``. It will also raise ``SlackDataError`` if the
userlist is malformed in any way.


Tests
=====
There is a test case for a successful creation of a SlackPerson object and
for the cases where exceptions should be raised. They are unittests so they
can be run with unittest discovery or ``pytest``.

