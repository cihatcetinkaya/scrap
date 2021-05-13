import requests
from bs4 import BeautifulSoup
import json
import sys

def startScraping(url, page_num):
    entries = []
    authors = []
    dates = []

    for i in range(1,page_num):
        r = requests.get(url + "?p=" + str(i), headers={'User-Agent': 'Mozilla/5.0 (Platform; Security; OS-or-CPU; Localization; rv:1.4) Gecko/20030624 Netscape/7.1 (ax)'})
        source = BeautifulSoup(r.content,"lxml")
        entry = source.find_all("div",attrs={"class":"content"})
        author = source.find_all("a",attrs={"class":"entry-author"})
        date = source.find_all("a",attrs={"class":"entry-date permalink"})
        print(date)
        for e in entry:
            entries.append(str(e.text).lstrip().rstrip())
        
        for a in author:
            authors.append(str(a.text).lstrip().rstrip())
        
        for d in date:
            dates.append(str(d.text).split()[0])

    data = {}
    print("cinnu")

    f = open('out.txt','w') 

    idx = 0
    for i in range(len(entries)):
        data[str(idx + 1)] = {"entry":entries[i], "author":authors[i], "date":dates[i]}
        idx += 1
        f.write(str(idx) + "," + dates[i] + "," + authors[i] + "," + entries[i] + "\n")

    with open('out.json', 'w') as json_file:
        json.dump(data, json_file, ensure_ascii=False)
        
        
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please check the inputs.")
        exit()
    startScraping(str(sys.argv[1]), int(sys.argv[2]))
