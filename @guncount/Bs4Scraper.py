from bs4 import BeautifulSoup
import requests
import globalVars


def main2():
    url = "https://www.gunviolencearchive.org/mass-shooting"

    r = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
    soup = BeautifulSoup(r.text, "lxml")

    shooting_table = soup.find('table', attrs={"class", 'responsive sticky-enabled'})

    myList = []

    for tbody in shooting_table.find_all(
            'tbody'):  # find table tag, then body tag, then row class and td which is a cell
        tr = tbody.find_all("tr")
        for row in tr:
            # if first variable = old stored variable; storedVariable needs to survive past the method and be GLOBAL
            if (int(row.find_all('td')[0].text) == globalVars.storedVariable):
                return myList
            myList.insert(0, row)
            # now, we just have to update whichever ones are the oldest
            # this iterates each piece of data downwards (newest to oldest) piece by piece, so we can BREAK the loop when it finds an old piece of data
        globalVars.storedVariable = int(tr[0].find_all('td')[0].text)
        return myList

    # now, we just have to update whichever ones are the oldest
    # this iterates each piece of data downwards (newest to oldest) piece by piece, so we can BREAK the loop when it finds an old piece of data
    globalVars.storedVariable = int(tr[0].find_all('td')[0].text)