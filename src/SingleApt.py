import pandas as pd
import numpy as np
import re

class SingleApt:

  def __init__(self):
    self.keys = ['Id', 'SurfaceArea', 'NumRooms', 'Type', 'Address', 'Description', 'Rent', 'Bookmark', 'Link']

  def get_map(self, single_apt_listing):
    """
    Get the Single Apartment map from the single_apt_listing (string) 
    """

    singleApt = {key:'' for key in self.keys}

    apt_nRoom_area = single_apt_listing.split("]")[0]
    tmp_nRoom = re.findall('([\d+\.?]+) rooms', apt_nRoom_area)
    singleApt['NumRooms'] = float(tmp_nRoom[0]) if len(tmp_nRoom) > 0 else np.nan

    
    tmp_area = re.findall('([\d+\.?]+) m²', apt_nRoom_area)
    singleApt['SurfaceArea'] = float(tmp_area[0]) if len(tmp_area) > 0 else np.nan

    rest = single_apt_listing[2:].split("]")[1]
    apt_link = "".join(re.findall('\((.*)', rest) + re.findall('(.*)\)', rest))
    singleApt['Link'] = apt_link

    singleApt['Description'] = "".join(re.findall('## «(.*)»', rest))
    singleApt['Address'] = "".join(re.findall('[^\n]+',"".join(re.findall('»\n\n([\s\S]+)Close\n\n', rest))))

    apt_rent = (re.findall('\n\nClose\n\n### \D+([\d,]+)', rest))
    singleApt['Rent'] = float((apt_rent[0]).replace(',','')) if len(apt_rent) > 0 else np.nan

    singleApt['Bookmark'] = "".join(re.findall('\n\nFavourite\n\n(.+)\n\n', rest))

    singleApt['Id'] = int("".join(re.findall('/en/d/.+/(\d+)', apt_link)))
    singleApt['Type'] = "".join(re.findall('/en/d/(.+)-rent-', apt_link))

    return singleApt