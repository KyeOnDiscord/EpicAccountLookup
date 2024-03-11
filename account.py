"""External auth module"""
import urllib.parse

# xbl, psn, nintendo, steam


class ExternalAuth:  # pylint: disable=too-few-public-methods
    """ExternalAuth class"""

    def __init__(self, key, value):
        self.service_name = key
        self.display_name = None
        self.external_auth_id = None
        self.profile_url = None
        if key in ["xbl", "psn", "steam"]:
            if value.get("externalDisplayName") is not None:
                self.display_name = value["externalDisplayName"]
        if key in ["psn", "nintendo", "steam"]:
            if value.get("externalAuthId") is not None:
                self.external_auth_id = value["externalAuthId"]
        if key == "steam":
            self.profile_url = "http://steamcommunity.com/profiles/" + \
                urllib.parse.quote(self.external_auth_id)
        if key == "xbl":
            self.profile_url = "https://account.xbox.com/en-us/profile?gamertag=" + \
                urllib.parse.quote(self.display_name)
        if key == "psn":
            self.profile_url = "https://psnprofiles.com/" + \
                urllib.parse.quote(self.display_name)

    def to_string(self) -> str:
        """Returns a string representation of the ExternalAuth object"""
        return "Service:" + self.service_name + " | " + self.profile_url
