import requests
import globalVars
import json


def main5(twitterSession):  # if you wanna know whether or not our status is volid, get the verify_credentials and print the value out w/o json conversion
    oauth = twitterSession
    response = oauth.get("https://api.twitter.com/1.1/account/verify_credentials.json")
    twitterJson = response.json()
    keyVal = "name"
    name = ""
    if keyVal in twitterJson:
        name = twitterJson[keyVal]  # The Gun Count: 0
    index = str(name).find(":") + 2
    substringGunCount = (str(name))[index:]
    newCount = int(substringGunCount) + 1
    newUserName = "The Gun Count: " + str(newCount)
    params = {'name': newUserName}
    r = oauth.post("https://api.twitter.com/1.1/account/update_profile.json", params=params)
    print(r.status_code)

    return


