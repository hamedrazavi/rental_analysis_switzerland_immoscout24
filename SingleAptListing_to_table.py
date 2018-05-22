import pandas as pd
import numpy as np

def SingleAptListing_to_table(single_apt_listing):

    # apt_nRoom_area = single_apt_listing[2:].split("]")[0]
    # rest = single_apt_listing[2:].split("]")[1]
    # splt = rest[2:].split(")")
    # apt_link = splt[0]
    # rest = splt[1]
    # splt = rest[6:].split("»")
    # apt_descr = splt[0]
    # rest = splt[1]
    # splt = rest.splitlines()
    # apt_address = splt[2]
    # apt_price = splt[6][4:]
    # apt_bkmrk = splt[-2]

    apt_nRoom_area = single_apt_listing[2:].split("]")[0]
    rest = single_apt_listing[2:].split("]")[1]
    n_splt = rest[2:].find(")")
    apt_link = rest[2:][:n_splt]
    rest = rest[2:][n_splt + 1:]
    splt = rest[6:].split("»")
    apt_descr = ''
    for i in range(len(splt) - 1):
        apt_descr += '»' + splt[i]
    rest = splt[-1]
    splt = rest.split("Close")
    apt_address = splt[0][2:-2]
    apt_price = splt[1].split("Bookmark")[0][6:-2]
    apt_bkmrk = splt[1].split("Bookmark")[1][1:-1]

    colnames = ['Id', 'SurfaceArea', 'NumRooms', 'Type', 'Address', 'Description', 'Rent', 'Bookmark', 'Link']
    apt_df = pd.DataFrame(columns=colnames)
    apt_df['Address'] = [apt_address]
    if apt_nRoom_area.find(',') != -1:
        apt_df['NumRooms'] = [float(apt_nRoom_area.split('room')[0][0:-1])]
        apt_df['SurfaceArea'] = [float(apt_nRoom_area.split(',')[1][1:-3])]
    elif apt_nRoom_area.find('room') == -1:
        apt_df['NumRooms'] = [1.0]
        apt_df['SurfaceArea'] = [float(apt_nRoom_area[:-3])]
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
        apt_df['Bookmark'] = apt_bkmrk[1:-1]

    apt_id = int(apt_link.split('?')[0].split('/')[3])
    apt_df['Id'] = apt_id

    apt_type = apt_link.split('-rent-')[0].split('/')[2]
    apt_df['Type'] = apt_type
    apt_df['Link'] = apt_link
    return apt_df