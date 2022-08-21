import Bs4Scraper
import globalVars
import SendWebhook
import CreateSession
import ChangeUser
import re
import time

# if tweet fails, refresh token and run sendwebhook again

def pullData():
    myList = Bs4Scraper.main2()  # should return a list
    # if no new data, return null, which should skip to time.sleep(delay)
    # if new data, process data
    processData(myList)


def processData(myList):
    for row in myList:
        date = row.find_all('td')[1].text
        state = row.find_all('td')[2].text
        city = row.find_all('td')[3].text
        numKilled = row.find_all('td')[5].text
        numInjured = row.find_all('td')[6].text
        totalCasualties = int(numKilled) + int(numInjured)
        sourceVar = row.find_all('a', attrs={'href': re.compile("^https://")})
        index1 = str(sourceVar).find("\"")
        index2 = str(sourceVar).find('\"', str(sourceVar).find('\"') + 1)

        sourceLink = (str(sourceVar)[index1 + 1:index2])
        print(sourceLink)

        incidentArray = [date, state, city, numKilled, numInjured, sourceLink]

        SendWebhook.main3(incidentArray, globalVars.twitterSession)
        print("Sent Tweet:", date, city, "| Total_Casualties =", totalCasualties)

        ChangeUser.main5(globalVars.twitterSession)
        time.sleep(1)

    print("success")


def main():
    delay = int(input("What is the time delay in seconds?: "))
    globalVars.twitterSession = CreateSession.main4()
    while True:
        pullData()

        time.sleep(delay)

    # last ID: 2372152
    # API Key: IJjKb8eBLssG5WyfaiqqfQzL7
    # Secret Key tSnvnV3hsbb7IYCcgzkvHvhBRggwm504ZQL2Gd0YilDGMfvLrH
    # Bearer Token AAAAAAAAAAAAAAAAAAAAAIBVfQEAAAAALNdEHj2Y%2BYtDoZHdszPnTLOZ%2F10%3DtMa5lk111rnSoX3q2rdxEUpOUFD5nbQThad2KtuZEZMXS9KkFw


if __name__ == '__main__':
    main()