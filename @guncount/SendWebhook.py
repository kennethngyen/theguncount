from requests_oauthlib import OAuth1Session
import os
import json


# In your terminal please set your environment variables by running the following lines of code.
# export 'CONSUMER_KEY'='<your_consumer_key>'
# export 'CONSUMER_SECRET'='<your_consumer_secret>'


# Be sure to add replace the text of the with the text you wish to Tweet. You can also add parameters to post polls, quote Tweets, Tweet with reply settings, and Tweet to Super Followers in addition to other features.
def main3(incidentInfo, twitterSession):
    oauth = twitterSession

    date = incidentInfo[0]
    state = incidentInfo[1]
    city = incidentInfo[2]
    numKilled = incidentInfo[3]
    numInjured = incidentInfo[4]
    sourceLink = incidentInfo[5]

    # payload = {"text": "On " + date + ", " + numInjured + " were injured and " + numKilled + " were killed in " + city + ", " + state}
    payload = {"text": "On {}, {} people were injured and {} people were killed in {}, {}.\n\n Source: {}".format(date,
                                                                                                                  numInjured,
                                                                                                                  numKilled,
                                                                                                                  city,
                                                                                                                  state,
                                                                                                                  sourceLink)}
    # On July 4, 2 people were shot and 0 people were killed

    # With OAuth from CreateSession, everything else should work
    # Making the request

    response = oauth.post(
        "https://api.twitter.com/2/tweets",
        json=payload,
    )

    if response.status_code != 201:
        raise Exception(
            "Request returned an error: {} {}".format(response.status_code, response.text)
        )

    print("Response code: {}".format(response.status_code))

    # Saving the response as JSON
    json_response = response.json()
    print(json.dumps(json_response, indent=4, sort_keys=True))
    print(json.dumps(json_response, indent=4, sort_keys=True))

    return