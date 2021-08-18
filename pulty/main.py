from bs4 import BeautifulSoup
import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36"
}

LINK = "https://pulty.tv"
append = "product/category"
pagination = "?page="
first_pagination = "?page=1"

temp_link = 'https://pulty.tv/product/index/DVB-T2%2B2_ver_2020_4200'
r = requests.get(temp_link)
encoding = r.encoding if 'charset' in r.headers.get('content-type', '').lower() else None
soup = BeautifulSoup(r.content, "lxml", from_encoding=encoding)

description = soup.find(class_="tovar").find_all("h1")
price = soup.find(class_="tovar").find_all("div", id="col2")
description52 = soup.find(class_="tovar").find("p").find("strong").find_next()
description55 = soup.find(class_="tovar").find("p").find_all("strong")
pics = soup.find(class_="tovar").find_all("div", id="tc2")
pult_dict = {}
for pr in price:
    for p_headerd in description:
        for gg in description55:
            for pic in pics:
                image = LINK + pic.find("img").get('src')
                names = gg.text
                pult_desriction = description52.text.split(":")[1].strip('\n')
                p_headerd = p_headerd.text
                arrs = pr.text.strip('\n').split()
                # print(pr.text.strip('\n').split())
                pult_dict[arrs[4]] = {"Товар": p_headerd}, {arrs[0].strip(':'): arrs[1]}, {
                    arrs[5].strip(':'): arrs[6]}, {
                                         names: pult_desriction}, {"JPG": image}
                print(pult_dict)

# pics = soup.find(class_="tovar").find_all("div", id="tc2")
# for pic in pics:
#     image = LINK + pic.find("img").get('src')
#     print(LINK + image)

# for g3 in description52:
#     desc = g3.text.strip('\n').strip('\n')
#     print(desc)


# print(description55)
# print(price)
# for p_headerd in description:
#     print(p_headerd.text)

# description = soup.find(class_="lmenu").find_all("AV210")
#
#
# def pults_listing(last_pult_url2):
#     # global text
#     third_level = requests.get(last_pult_url2)
#     soup3 = BeautifulSoup(third_level.content, "lxml", from_encoding=encoding1)
#     remotes_html = soup3.find('div', class_="tovarlist").find_all('div', class_='tblockw')
#     pult_arr = []
#     for remote in remotes_html:
#         remotes_url = remote.find_all("a")
#         for remote_url in remotes_url:
#             text1 = remote_url.text
#             pult_url = LINK + remote_url.get("href")
#
#             pult_arr.append(pult_url)
#
#     print(pult_arr[1])
#     # for ff in pult_arr:
#     #     print(ff)
#     # third_level = requests.get(pult_arr)
#     # soup4 = BeautifulSoup(third_level.content, "lxml", from_encoding=encoding1)
#     # remotes_html2 = soup4.find(text="AV100").find_parent()
#     # print(remotes_html2)
#
#
# for brend in description[0:1]:  # [0:1]
#     item_text = brend.text
#     item_url = LINK + brend.get("href")
#     print(f"{item_text} - {item_url}")
#
#     second_level_url = requests.get(item_url)
#     encoding = second_level_url.encoding if 'charset' in second_level_url.headers.get('content-type',
#                                                                                       '').lower() else None
#     soup1 = BeautifulSoup(second_level_url.content, "lxml", from_encoding=encoding)
#
#     # brand_list = soup1.find(text="Akira").find_parent()
#     # print(brand_list)
#
#     brands = soup1.find(class_="cmenu").find_all("a")
#     for brend in brands[2:3]:  # [2:3]
#         brand_text = brend.text
#         first_url = LINK + brend.get("href")
#         print(f"{brand_text} - {first_url}")
#
#         # СПИСОК ВСЕХ БРЕНДОВ
#         # brands = soup1.find(class_="brands").find_all("a")
#         # for item in brands:
#         #     brand_text = item.text
#         #     brand_url = LINK + item.get("href")
#         #     print(f"{brand_text} - {brand_url}")
#
#         ###пауза
#         arr = []
#         arr2 = []
#
#         third_level_url = requests.get(first_url)
#         encoding1 = third_level_url.encoding if 'charset' in third_level_url.headers.get('content-type',
#                                                                                          '').lower() else None
#         soup2 = BeautifulSoup(third_level_url.content, "lxml", from_encoding=encoding1)
#
#         pages = soup2.find('div', class_="pgw")
#         try:
#             page_numbers = pages.text
#             for page in page_numbers:
#                 if page.isnumeric():
#                     arr.append(page)
#             last_pult_url = first_url + pagination + arr[-1]
#             x = range(1, int(arr[-1]) + 1, 1)
#             for n in x:
#                 last_pult_url2 = first_url + pagination + str(n)
#                 print("+++")
#                 pults_listing(last_pult_url2)
#
#
#         except:
#             print('ok!')
#             # pults_listing(first_url)
#             # print(first_url)
