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

    def get_slack_id(self, team_user_list):
        """Get a person's slack_id for tagging in messages.

        Arguments:
        team_user_list: json object returned by users.list.

        NOTE: users.list could be called internally but for multiple people
        that would be inefficient. Call it once externally and pass in the
        value.
        """
        try:
            # it's silly to do the search over and over, so after the first
            # run this attribute with be set.
            return self._userid
        except AttributeError:
            pass
        # if it's the first run, actually do the search
        try:
            for user in team_user_list['members']:
                if self.username == user['name']:
                    self._userid = user['id']
                    return self._userid
        except AttributeError:
            raise SlackDataError("team_user_list has no members element.")


class SlackDataError(Exception):
    """Exception raised if input data is invalid in some way."""
    pass
