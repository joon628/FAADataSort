import matplotlib.pyplot as plt
import pymysql
import pandas as pd
import numpy as np


def connect(host, user, password):
    conn = pymysql.connect(host=host, user=user, password=password, db='mysql', charset='utf8')
    curs = conn.cursor()
    return conn, curs


def grab_data():
    conn, curs = connect("127.0.0.1", "root", 'Organictech3085')

    lat_list = []
    sql = "SELECT lat FROM ground_data.generic WHERE 42.199444 < lat AND lat < 42.498333 AND -71.2 < lon AND lon < -70.849167 AND alt < 2000 "
    curs.execute(sql)
    lat = curs.fetchall()
    for element in lat:
        lat_list.append(element[0])

    lon_list = []
    sql = "SELECT lon FROM ground_data.generic WHERE -71.2 < lon AND lon < -70.849167 AND 42.199444 < lat AND lat < 42.498333 AND alt < 2000"
    curs.execute(sql)
    lon = curs.fetchall()
    for element in lon:
        lon_list.append(element[0])

    return lat_list,lon_list

def plot():
    lon,lat = grab_data()
    lat = [float(item) for item in lat]
    lon = [float(item) for item in lon]
    print(lat,lon)
    # Sample (0.33% over 1.5 million)
    sample_coords = list(zip(lat,lon))

    df = pd.DataFrame(sample_coords, columns = ["lat","lon"])
    print(df)
    BBox = (df.lat.min(),df.lat.max(),df.lon.min(),df.lon.max())
    print(BBox)
    ruh_m = plt.imread('/Users/joonkang/Desktop/map.png')

    fig, ax = plt.subplots(figsize = (20,20))
    ax.scatter(df.lat, df.lon, zorder=1, alpha= 0.2, c='r', s=10)
    ax.set_title('Flight Data Scatter Plot, All')
    ax.set_xlim(BBox[0],BBox[1])
    ax.set_ylim(BBox[2],BBox[3])
    ax.imshow(ruh_m, zorder=0, extent = BBox, aspect= 'equal')
    fig.savefig("map_plot.png")

def all_data():
    conn, curs = connect("127.0.0.1", "root", 'Organictech3085')

    all_list = []
    sql = "SELECT * FROM ground_data.generic WHERE 42.199444 < lat AND lat < 42.498333 AND alt < 2000 AND -71.2 < lon AND lon < -70.849167"
    curs.execute(sql)
    all = curs.fetchall()
    print(all)

if __name__ == "__main__":
    plot()
