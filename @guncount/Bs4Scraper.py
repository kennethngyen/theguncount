from bs4 import BeautifulSoup
import requests
import globalVars
import time
import lxml



def main2():
    url = "https://www.gunviolencearchive.org/mass-shooting"
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
    }

    try: #in case of errors
        r = requests.get(url, headers=headers)

    except (ConnectionError, TimeoutError, TimeoutError) as e:
        print("Lost Connection: retrying...")
        time.sleep(30)
        r = requests.get(url, headers=headers)
    except:
        print("Trying general exception...")
        time.sleep(30)
        r = requests.get(url, headers=headers)

    soup = BeautifulSoup(r.text, "lxml")

    shooting_table = soup.find('table', attrs={"class", 'responsive sticky-enabled'})

    myList = []
    counter = 0


    for tbody in shooting_table.find_all(
            'tbody'):  # find table tag, then body tag, then row class and td which is a cell
        tr = tbody.find_all("tr")
        for row in tr:
            # this iterates each piece of data downwards (newest to oldest) piece by piece, so we can BREAK the loop when it finds an old piece of data
            # if first variable = old stored variable; storedVariable needs to survive past the method and be GLOBAL
            print("ID:",(int(tr[counter].find_all('td')[0].text)))
            if (int(tr[counter].find_all('td')[0].text) == globalVars.storedVariable) or (int(tr[counter].find_all('td')[0].text) in globalVars.idList):
                return(myList)
            myList.insert(0, row)
            #append ID to global idList
            globalVars.idList.append(int(tr[counter].find_all('td')[0].text))
            counter += 1
            # now, we just have to update whichever ones are the oldest
        return(myList)

    # now, we just have to update whichever ones are the oldest
    # this iterates each piece of data downwards (newest to oldest) piece by piece, so we can BREAK the loop when it finds an old piece of data

if (__name__ == "__main__"):
    main2()