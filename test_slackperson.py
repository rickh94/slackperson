"""Test for slackperson."""
import unittest
from unittest import mock
from slackperson import SlackPerson
from slackperson import SlackDataError

USERLIST = {"members": [
    {
        "color": "ffffff",
        "id": "U00000001",
        "name": "jbiden",
        "profile": {
            "email": "jbiden@whitehouse.gov",
            "first_name": "Joe",
            "last_name": "Biden",
            "real_name": "Joe Biden",
            "real_name_normalized": "Joe Biden",
            "team": "T00000001",
            "title": ""
        },
        "real_name": "Joe Biden",
        "team_id": "T00000001",
        "tz": "America/New_York",
        "tz_label": "Eastern Daylight Time",
        "tz_offset": -14400,
    },
    {
        "color": "000000",
        "id": "U00000002",
        "name": "bobama",
        "profile": {
            "email": "bobama@whitehouse.gov",
            "first_name": "Barack",
            "last_name": "Obama",
            "real_name": "Barack Obama",
            "real_name_normalized": "Barack Obama",
            "team": "T00000001"
        },
        "real_name": "Barack Obama",
        "team_id": "T00000001",
        "tz": "America/New_York",
        "tz_label": "Eastern Daylight Time",
        "tz_offset": -14400,
    },
],
}


class TestSlackPerson(unittest.TestCase):
    """Tests the SlackPerson class."""
    def test_user_info(self):
        """Test that the SlackPerson has all the right attributes."""
        test_person = SlackPerson(
            username='bobama',
            team_user_list=USERLIST
        )
        self.assertEqual(
            str(test_person),
            'SlackPerson(userid=U00000002, username=bobama)'
        )
        assert test_person.userid == 'U00000002'
        assert test_person.email == 'bobama@whitehouse.gov'
        assert test_person.fname == 'Barack'
        assert test_person.lname == 'Obama'
        assert test_person.team == 'T00000001'
        # test that usernames with @s work
        test_person2 = SlackPerson(
            username='jbiden',
            team_user_list=USERLIST
        )
        assert test_person2.userid == 'U00000001'
        assert test_person2.email == 'jbiden@whitehouse.gov'
        assert test_person2.fname == "Joe"
        assert test_person2.lname == "Biden"
        assert test_person2.team == 'T00000001'

    def test_raise_exceptions(self):
        """Test data validation and exceptions."""
        # User is not in list
        self.assertRaises(
            SlackDataError,
            SlackPerson,
            username='dtrump',
            team_user_list=USERLIST
        )

        # team_user_list is wrong type
        self.assertRaises(
            SlackDataError,
            SlackPerson,
            username='bobama',
            team_user_list='wrongtype'
        )

        # team_user_list doesn't have members
        self.assertRaises(
            SlackDataError,
            SlackPerson,
            username='jbiden',
            team_user_list={'ok': False, 'error': 'could not get data'}
        )
