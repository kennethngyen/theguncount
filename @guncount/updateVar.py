from bs4 import BeautifulSoup
import requests
import globalVars
import lxml


def main7():
    url = "https://www.gunviolencearchive.org/mass-shooting"
    headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:66.0) Gecko/20100101 Firefox/66.0",
    "Accept-Encoding": "*",
    "Connection": "keep-alive"
    }

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.text, "lxml")

    shooting_table = soup.find('table', attrs={"class", 'responsive sticky-enabled'})

    myList = []


    for tbody in shooting_table.find_all(
            'tbody'):  # find table tag, then body tag, then row class and td which is a cell
        tr = tbody.find_all("tr")
        for row in tr:
            globalVars.storedVariable = int(tr[0].find_all('td')[0].text)

    print(globalVars.storedVariable)

if(__name__ == '__main__'):
    main7()