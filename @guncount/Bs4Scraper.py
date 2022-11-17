from bs4 import BeautifulSoup
import requests
import globalVars
import time
import lxml



def main2():
    try:
        url = "https://www.gunviolencearchive.org/mass-shooting"
        headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
        "Accept-Encoding": "*",
        "Connection": "keep-alive"
        }

        #grab url and HTML data
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")

        #grab HTML table and store into parsable data
        shooting_table = soup.find('table', attrs={"class", 'responsive sticky-enabled'})


        myList = []
        counter = 0

        #try in case shooting_table was not grabbed
        #finds tbody tag in HTML and parses through data
        try:
            for tbody in shooting_table.find_all(
                    'tbody'):  # find table tag, then body tag, then row class and td which is a cell
                tr = tbody.find_all("tr")
                for row in tr:
                    #grab the ID of the incident at hand
                    currentIncidentID = int(tr[counter].find_all('td')[0].text)

                    # iterates downwards the table (newest to oldest) piece by piece; BREAK the loop and return new
                    # variables when it finds an old piece of data
                    # if first variable == old stored variable;
                    print("Bs4Scraper grabbed ID:",(currentIncidentID))
                    if (currentIncidentID in globalVars.idList):
                        return(myList)
                    myList.insert(0, row)
                    #append ID to global idList; storedVariable survives past the method call and is GLOBAL
                    globalVars.idList.append(currentIncidentID)

                    counter += 1
                    # now, we just have to update whichever ones are the oldest
                return(myList)
            # now, we just have to update whichever ones are the oldest
            # this iterates each piece of data downwards (newest to oldest) piece by piece, so we can BREAK the loop when it finds an old piece of data

        #if fail, try again in 1 minute
        except:
            #re-do block
            print("Failed to get table, trying again...\n\n\n")
            time.sleep(60)
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.text, "lxml")
            shooting_table = soup.find('table', attrs={"class", 'responsive sticky-enabled'})

            #re-do grab each incident
            for tbody in shooting_table.find_all(
                    'tbody'):  # find table tag, then body tag, then row class and td which is a cell
                tr = tbody.find_all("tr")
                for row in tr:
                    # grab the ID of the incident at hand
                    currentIncidentID = int(tr[counter].find_all('td')[0].text)

                    # iterates downwards the table (newest to oldest) piece by piece; BREAK the loop and return new
                    # variables when it finds an old piece of data
                    # if first variable == old stored variable;
                    print("Bs4Scraper grabbed ID:", (currentIncidentID))
                    if (currentIncidentID == globalVars.storedVariable) or (currentIncidentID in globalVars.idList):
                        return (myList)
                    myList.insert(0, row)
                    # append ID to global idList; storedVariable survives past the method call and is GLOBAL
                    globalVars.idList.append(currentIncidentID)

                    counter += 1
                    # now, we just have to update whichever ones are the oldest
                return (myList)
    except:
        print("Failed to get table, trying again...\n\n\n\n\n")
        time.sleep(60)
        url = "https://www.gunviolencearchive.org/mass-shooting"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
            "Accept-Encoding": "*",
            "Connection": "keep-alive"
        }

        # grab url and HTML data
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, "lxml")

        # grab HTML table and store into parsable data
        shooting_table = soup.find('table', attrs={"class", 'responsive sticky-enabled'})

        myList = []
        counter = 0

        # try in case shooting_table was not grabbed
        # finds tbody tag in HTML and parses through data
        try:
            for tbody in shooting_table.find_all(
                    'tbody'):  # find table tag, then body tag, then row class and td which is a cell
                tr = tbody.find_all("tr")
                for row in tr:
                    # grab the ID of the incident at hand
                    currentIncidentID = int(tr[counter].find_all('td')[0].text)

                    # iterates downwards the table (newest to oldest) piece by piece; BREAK the loop and return new
                    # variables when it finds an old piece of data
                    # if first variable == old stored variable;
                    print("Bs4Scraper grabbed ID:", (currentIncidentID))
                    if (currentIncidentID in globalVars.idList):
                        return (myList)
                    myList.insert(0, row)
                    # append ID to global idList; storedVariable survives past the method call and is GLOBAL
                    globalVars.idList.append(currentIncidentID)

                    counter += 1
                    # now, we just have to update whichever ones are the oldest
                return (myList)

            # now, we just have to update whichever ones are the oldest
            # this iterates each piece of data downwards (newest to oldest) piece by piece, so we can BREAK the loop when it finds an old piece of data

        # if fail, try again in 1 minute
        except:
            # re-do block
            print("Failed to get table, trying again...\n\n\n")
            time.sleep(60)
            r = requests.get(url, headers=headers)
            soup = BeautifulSoup(r.text, "lxml")
            shooting_table = soup.find('table', attrs={"class", 'responsive sticky-enabled'})

            # re-do grab each incident
            for tbody in shooting_table.find_all(
                    'tbody'):  # find table tag, then body tag, then row class and td which is a cell
                tr = tbody.find_all("tr")
                for row in tr:
                    # grab the ID of the incident at hand
                    currentIncidentID = int(tr[counter].find_all('td')[0].text)

                    # iterates downwards the table (newest to oldest) piece by piece; BREAK the loop and return new
                    # variables when it finds an old piece of data
                    # if first variable == old stored variable;
                    print("Bs4Scraper grabbed ID:", (currentIncidentID))
                    if (currentIncidentID == globalVars.storedVariable) or (currentIncidentID in globalVars.idList):
                        return (myList)
                    myList.insert(0, row)
                    # append ID to global idList; storedVariable survives past the method call and is GLOBAL
                    globalVars.idList.append(currentIncidentID)

                    counter += 1
                    # now, we just have to update whichever ones are the oldest
                return (myList)
    finally:
        print("\n\nScraper failed\n\n")

if (__name__ == "__main__"):
    main2()