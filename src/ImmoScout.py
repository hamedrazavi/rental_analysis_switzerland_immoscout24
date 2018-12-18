import html2text
import requests
import time
import os
import datetime
import pandas as pd
from SingleAptListing_to_table import SingleAptListing_to_table
from SingleApt import SingleApt

class ImmoScout:
  """
  Immoscout rental data to CSV given the city name and a path to save the csv file
  """
  def __init__(self, city_name, list_type = 'rent'):
    """
    Initialize the class: list_type can be 'rent' or 'buy'. Currently it only works and has been tested for 
    list_type = 'rent'.
    """
    self.city_name = city_name.lower()
    self.type = list_type.lower()
    self.SingleApt = SingleApt()

  
  def page2text(self, page_num = 1):
    """
    Convert html to text 
    """
    base_url = 'https://www.immoscout24.ch/en/flat/'
    url = base_url + self.type + '/city-' + self.city_name + '?ci&pn=' + str(page_num) 
    res = requests.get(url)
    res.encoding = 'utf-8'
    h = html2text
    c = h.html2text(res.text)
    return c

  def find_max_page_num(self, c):
    string = "Page** 1 **of** "
    l_string = len(string)
    a = c.find(string)
    b = c.find("**", a + l_string)
    return int(c[a + l_string : b-1])

  def text2apts_map(self, c):
    end_c_n = c.find("Page** ")
    c = c[0:end_c_n]
    splt_listing = c.split("### [")
    apts_map = {key:[] for key in self.SingleApt.keys}
    for j in range(1, len(splt_listing)):
        single_apt_listing = splt_listing[j]
        single_map = self.SingleApt.get_map(single_apt_listing)
        for key in self.SingleApt.keys:
          apts_map[key].append(single_map[key])
    return apts_map
  
  def text2df(self, c):
    apts_map = self.text2apts_map(c)
    df = pd.DataFrame(apts_map)
    return df

  def to_df(self, in_path=''):
    """
    Convert the city 'rent' or 'buy' data to a pandas data frame.
    If 'in_path' is given, data in 'in_path' is included. 
    """
    df = pd.DataFrame({key:[] for key in self.SingleApt.keys})
    if in_path:
      df = pd.read_csv(in_path)
    c1 = self.page2text(page_num=1)
    max_page_num = self.find_max_page_num(c1)

    for i in range(1, max_page_num + 1):
      time.sleep(10)
      c = self.page2text(page_num=i)
      dfi = self.text2df(c)
      id_exists = dfi['Id'].isin(df['Id'])
      if (id_exists).sum() == 0: # check if the entry already exists
        df = pd.concat(objs=[df, dfi], axis = 0).reset_index(drop = True)
      else:
        dfi = dfi.loc[id_exists]
        df = pd.concat(objs=[df, dfi], axis = 0).reset_index(drop = True)
        break
    return df

  def to_csv(self, in_path='', out_path=''):
    """
    Save the city 'rent' or 'buy' date in 'out_path'. 'out_path' is the path to 
    a 'csv' file.  
    If 'in_path' is given the data in 'in_path' is included in the output, and 
    only new online data is added.  
    """
    df = self.to_df(in_path)
    df.to_csv(out_path, index = False)

    