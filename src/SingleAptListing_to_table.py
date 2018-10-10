import pandas as pd
import numpy as np
import re

def SingleAptListing_to_table(single_apt_listing):

    colnames = ['Id', 'SurfaceArea', 'NumRooms', 'Type', 'Address', 'Description', 'Rent', 'Bookmark', 'Link']
    apt_df = pd.DataFrame(columns=colnames)
    
    apt_nRoom_area = single_apt_listing.split("]")[0]
    tmp_nRoom = re.findall('([\d+\.?]+) rooms', apt_nRoom_area)
    apt_df['NumRooms'] = [float(tmp_nRoom[0]) if len(tmp_nRoom) > 0 else np.nan]

    tmp_area = re.findall('([\d+\.?]+) m²', apt_nRoom_area)
    apt_df['SurfaceArea'] = [float(tmp_area[0]) if len(tmp_area) > 0 else np.nan]

    rest = single_apt_listing[2:].split("]")[1]
    apt_link = "".join(re.findall('\((.*)', rest) + re.findall('(.*)\)', rest))
    apt_df['Link'] = apt_link

    apt_df['Description'] = "".join(re.findall('## «(.*)»', rest))
    apt_df['Address'] = "".join(re.findall('[^\n]+',"".join(re.findall('»\n\n([\s\S]+)Close\n\n', rest))))

    apt_rent = (re.findall('\n\nClose\n\n### \D+([\d,]+)', rest))
    apt_df['Rent'] = float((apt_rent[0]).replace(',','')) if len(apt_rent) > 0 else np.nan

    apt_df['Bookmark'] = "".join(re.findall('\n\nFavourite\n\n(.+)\n\n', rest))

    apt_df['Id'] = int("".join(re.findall('/en/d/.+/(\d+)', apt_link)))
    apt_df['Type'] = "".join(re.findall('/en/d/(.+)-rent-', apt_link))

    return apt_df