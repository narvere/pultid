from bs4 import BeautifulSoup
import requests, os

# random, time

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

LINK = "https://pulty.tv"
append = "product/category"

respond = requests.get(url=LINK, headers=headers)
soup = BeautifulSoup(respond.text, "lxml")

# shit_number = soup.find(text="ÐÐ»Ñ Ð´Ð¾Ð¼Ð°ÑÐ½ÐµÐ³Ð¾ ÐºÐ¸Ð½Ð¾ÑÐµÐ°ÑÑÐ°").find_parent().find_parent().find_parent().find_parent()
# print(shit_number)
# description = soup.find(class_="lmenu").text
# print(description)
# hrefs = soup.find(class_="lmenu").find("ul").find_all("a")
# for i in hrefs:
#     print(LINK + i.get("href"))

# page_number = soup.find(class_="lmenu").find("a").get("href")

# print(page_number)
# # print(soup)
description = soup.find(class_="lmenu").find_all("a")
for item in description:
    item_text = item.text
    item_url = LINK + item.get("href")
    print(f"{item_text} - {item_url}")
