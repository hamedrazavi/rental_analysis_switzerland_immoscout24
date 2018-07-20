import pandas as pd
import numpy as np

def SingleAptListing_to_table(single_apt_listing):

    apt_nRoom_area = single_apt_listing.split("]")[0]
    rest = single_apt_listing[2:].split("]")[1]
    n_splt = rest[2:].find(")")
    apt_link = rest[2:][:n_splt]
    rest = rest[2:][n_splt + 1:]
    n_splt = rest.find("»\n\n")
    apt_descr = rest[6:n_splt]
    rest = rest[n_splt:]
    splt = rest.split("Close\n\n###")
    apt_address = splt[0][3:-2]
    rest = splt[1]
    n_splt1 = rest.find("Bookmark")
    n_splt2 = rest.find("##")
    apt_price = rest[1:n_splt1 - 2]
    apt_bkmrk = rest[n_splt1 + 10: n_splt2]

    colnames = ['Id', 'SurfaceArea', 'NumRooms', 'Type', 'Address', 'Description', 'Rent', 'Bookmark', 'Link']
    apt_df = pd.DataFrame(columns=colnames)
    apt_df['Address'] = [apt_address]
    if apt_nRoom_area.find(',') != -1:
        apt_df['NumRooms'] = [float(apt_nRoom_area.split('room')[0][0:-1])]
        apt_df['SurfaceArea'] = [float(apt_nRoom_area.split(',')[1].replace("'", '')[1:-3])]
    elif apt_nRoom_area.find('room') == -1:
        apt_df['NumRooms'] = [1.0]
        apt_df['SurfaceArea'] = [float(apt_nRoom_area[:-3].replace("'", ''))]
    else:
        apt_df['NumRooms'] = [float(apt_nRoom_area.split('room')[0][0:-1])]
        apt_df['SurfaceArea'] = np.nan

    apt_df['Description'] = [apt_descr]

    if apt_price == 'Price on request':
        apt_df['Rent'] = [np.nan]
    else:
        apt_df['Rent'] = [float(apt_price[4:-2].replace(',', ''))]

    if apt_bkmrk == '':
        apt_df['Bookmark'] = 'None'
    else:
        apt_df['Bookmark'] = apt_bkmrk[:-1]

    apt_id = int(apt_link.split('?')[0].split('/')[3])
    apt_df['Id'] = apt_id

    apt_type = apt_link.split('-rent-')[0].split('/')[2]
    apt_df['Type'] = apt_type
    apt_df['Link'] = apt_link

    return apt_df