"""Defines a class for storing a person's slack profile information."""


class SlackPerson(object):
    """Class for storing/getting slack profile information."""
    def __init__(self, username):
        """Initializes SlackPerson.

        Arguments:
        username: the handle with or without @ used to mention someone
        """
        if username[0] == '@':
            username = username[1:]
        self.username = username

    # perhaps reimplement to be called by __init__
    def get_slack_id(self, team_user_list):
        """Get a person's slack_id for tagging in messages.

        Arguments:
        team_user_list: json object returned by users.list.

        NOTE: users.list could be called internally but for multiple people
        that would be inefficient. Call it once externally and pass in the
        value.
        """
        # it's silly to do the search over and over, so after the first run
        # this attribute with be set.
        if hasattr(self, '_userid'):
            return self._userid
        # if it's the first run, actually do the search
        try:
            for user in team_user_list['members']:
                if self.username == user['name']:
                    self._userid = user['id']
                    return self._userid
        except AttributeError:
            raise SlackDataError("team_user_list has no members element.")

    def get_info(self, slackclient):
        """Gets all the info about a user from slack.

        Arguments:
        slackclient: An already logged in SlackClient object for getting user
        info.
        """
        try:
            user_info = slackclient.api_call('users.info', user=self._userid)
        except AttributeError:
            raise SlackDataError("You need to run SlackPerson.get_slack_id"
                                 " before running get info.")
        if not user_info['ok']:
            raise SlackDataError(("There's been a problem with {username},"
                                  " {user_id}: {err}").format(
                                      username=self.username,
                                      user_id=self._userid,
                                      err=user_info['error']))

        self.fname = user_info['user']['profile']['first_name']
        self.lname = user_info['user']['profile']['last_name']
        self.email = user_info['user']['profile']['email']
        self.team = user_info['user']['profile']['team']


class SlackDataError(Exception):
    """Exception raised if input data is invalid in some way."""
    pass
