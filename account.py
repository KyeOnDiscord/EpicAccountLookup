import urllib.parse

# xbl, psn, nintendo, steam
class ExternalAuth:
    def __init__(self, key,value) -> None:
        self.ServiceName = key
        self.displayName = "None"
        self.externalAuthId = "None"
        self.profileURL = "None"
        if key in ["xbl", "psn", "steam"]:
            if value.get("externalDisplayName") != None:
                self.displayName = value["externalDisplayName"]
        if key in ["psn", "nintendo", "steam"]:
            if value.get("externalAuthId") != None:
                self.externalAuthId = value["externalAuthId"]
        if key == "steam":
            self.profileURL = "http://steamcommunity.com/profiles/" + urllib.parse.quote(self.externalAuthId)
        if key == "xbl":
            self.profileURL = "https://account.xbox.com/en-us/profile?gamertag=" + urllib.parse.quote(self.displayName)
        if key == "psn":
            self.profileURL = "https://psnprofiles.com/" + urllib.parse.quote(self.displayName)
    def ToString(self) -> str:
        return "Service:" + self.ServiceName + " | " + self.profileURL
            
        
                

class Account:
    def __init__(self, EpicDisplayName, EpicID, externalAuths) -> None:
        self.EpicDisplayName = EpicDisplayName
        self.EpicID = EpicID
        self.externalAuths = externalAuths