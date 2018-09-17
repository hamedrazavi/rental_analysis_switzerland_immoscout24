# Download the immoscoutHtml, and add the New (not existed before) rental data to the csv file which
# includes all previous rental data
import html2text
import requests
import time
import os
import datetime
import pandas as pd
from SingleAptListing_to_table import SingleAptListing_to_table

city_path = '../../rental_list/lausanne/'
all_rental_data_path = city_path + 'all_rental_data'
date_today = datetime.datetime.now().strftime ("%Y%m%d")
all_rental_data_path = city_path + 'all_rental_data'
if not os.path.exists(all_rental_data_path):
    os.makedirs(all_rental_data_path)
csv_today_path = all_rental_data_path + '/rental_' + date_today + '.csv'
if not os.path.exists(all_rental_data_path + '/combined'):
    os.makedirs(all_rental_data_path + '/combined')
if not os.path.exists(csv_today_path):
    df = pd.read_csv(all_rental_data_path + '/combined/rental_all.csv')
    first_page = requests.get('https://www.immoscout24.ch/en/flat/rent/city-lausanne')
    h = html2text
    c = h.html2text(first_page.text)
    def find_max_page_num(c):
        string = "Page** 1 **of** "
        l_string = len(string)
        a = c.find(string)
        b = c.find("**", a + l_string)
        return int(c[a + l_string : b-1])

    max_page_num = find_max_page_num(c)
    main_url = 'https://www.immoscout24.ch/en/flat/rent/city-lausanne?ci&pn='
    df_today = pd.DataFrame()
    for i in range(1, max_page_num + 1):
        page_url = main_url + str(i)
        page = requests.get(page_url)
        c = h.html2text(page.text)
        end_c_n = c.find("Page** ")
        c = c[0:end_c_n]
        splt_listing = c.split("### [")
        for j in range(1, len(splt_listing)):
            single_apt_listing = splt_listing[j]
            print(single_apt_listing)
            tmdf = SingleAptListing_to_table(single_apt_listing)
            if (df['Id'] == tmdf['Id'][0]).sum() == 0:
                df_today = pd.concat(objs=[df_today, tmdf], axis = 0).reset_index(drop = True)
        time.sleep(5)

    df_today.to_csv(csv_today_path, index = False)
    df = pd.concat(objs=[df_today, df], axis = 0).reset_index(drop = True)
    df.to_csv(all_rental_data_path + '/combined/rental_all.csv', index = False)

