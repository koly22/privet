import sqlite3
import datetime
import time

import requests
from bs4 import BeautifulSoup
while True:
    response - requests.get("https://sinoptik.ua/%D0%BF%D0%BE%D0%B3%D0%BE%D0%B4%D0%B0-%D0%BE%D1%81%D0%BB%D0%BE")
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, features-"html.parser")
        soup_list = soup.find_alL("div", {"class":"LSide"})
        res = soup_list[0].find("p", {"class":"today-temp"})
    print(res.text)

    connection = sqlite3.connect("itstep_DB.sl3", 5)
    cur - connection.cursor ()
    # cour execute ("CREATE TABLE weather (date TEXT, temp TEXT) ")
    connection.commit()
    cur.execute(f"INSERT into weather VALUES ('{datetime.datetime.now()}` , `{res.text}`);")

    connection.commit()

    connection.close()
    time.sleep(2)
