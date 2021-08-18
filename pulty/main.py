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

r = requests.get(LINK)
encoding = r.encoding if 'charset' in r.headers.get('content-type', '').lower() else None
soup = BeautifulSoup(r.content, "lxml", from_encoding=encoding)

description = soup.find(class_="lmenu").find_all("a")


def pults_listing(last_pult_url2):
    global text
    third_level = requests.get(last_pult_url2)
    soup3 = BeautifulSoup(third_level.content, "lxml", from_encoding=encoding1)
    remotes_html = soup3.find('div', class_="tovarlist").find_all('div', class_='tblockw')
    pult_arr=[]
    for remote in remotes_html:
        remotes_url = remote.find_all("a")
        for remote_url in remotes_url:
            text = remote_url.text
            pult_url = LINK + remote_url.get("href")
            # print(f"{text} - {pult_url}")
            pult_arr.append(pult_url)

    print(pult_arr[0])
    # third_level = requests.get(pult_arr)
    # soup4 = BeautifulSoup(third_level.content, "lxml", from_encoding=encoding1)
    # remotes_html2 = soup4.find(text="AV100").find_parent()
    # print(remotes_html2)



for brend in description[0:1]:  # [0:1]
    item_text = brend.text
    item_url = LINK + brend.get("href")
    print(f"{item_text} - {item_url}")

    second_level_url = requests.get(item_url)
    encoding = second_level_url.encoding if 'charset' in second_level_url.headers.get('content-type',
                                                                                      '').lower() else None
    soup1 = BeautifulSoup(second_level_url.content, "lxml", from_encoding=encoding)

    # brand_list = soup1.find(text="Akira").find_parent()
    # print(brand_list)

    brands = soup1.find(class_="cmenu").find_all("a")
    for brend in brands[2:3]:  # [2:3]
        brand_text = brend.text
        first_url = LINK + brend.get("href")
        print(f"{brand_text} - {first_url}")

        # СПИСОК ВСЕХ БРЕНДОВ
        # brands = soup1.find(class_="brands").find_all("a")
        # for item in brands:
        #     brand_text = item.text
        #     brand_url = LINK + item.get("href")
        #     print(f"{brand_text} - {brand_url}")

        ###пауза
        arr = []
        arr2 = []

        third_level_url = requests.get(first_url)
        encoding1 = third_level_url.encoding if 'charset' in third_level_url.headers.get('content-type',
                                                                                         '').lower() else None
        soup2 = BeautifulSoup(third_level_url.content, "lxml", from_encoding=encoding1)

        pages = soup2.find('div', class_="pgw")
        try:
            page_numbers = pages.text
            for page in page_numbers:
                if page.isnumeric():
                    arr.append(page)
            last_pult_url = first_url + pagination + arr[-1]
            x = range(1, int(arr[-1]) + 1, 1)
            for n in x:
                last_pult_url2 = first_url + pagination + str(n)
                # print(last_pult_url2)
                pults_listing(last_pult_url2)

            ###

            # third_level_url = requests.get(last_pult_url)
            # encoding1 = third_level_url.encoding if 'charset' in third_level_url.headers.get('content-type',
            #                                                                                  '').lower() else None
            # soup3 = BeautifulSoup(third_level_url.content, "lxml", from_encoding=encoding1)
            #
            # pages = soup3.find('div', class_="pgw")
            # page_numbers = pages.text
            #
            # for page in page_numbers:
            #     if page.isnumeric():
            #         arr2.append(page)

            # x = range(1,int(arr2[-1])+1,1)
            # for n in x:
            #     last_pult_url2 = brand_url + pagination + str(n)
            #     print(last_pult_url2)

            # last_pult_url2 = brand_url + pagination + arr2[-1]
            # print(last_pult_url2)

            ###

            # for ar in arr:
            #     brand_url1 = brand_url + pagination + ar
            #     print(brand_url1)

            # remotes_html = soup2.find('div', class_="tovarlist").find_all('div', class_='tblockw')

            # for remote in remotes_html:
            #     remotes_url = remote.find_all("a")
            #     for remote_url in remotes_url:
            #         text = remote_url.text
            #         pult_url = LINK + remote_url.get("href")
            #         print(f"{text} - {pult_url}")

        except:
            pults_listing(first_url)
            # print(first_url)
