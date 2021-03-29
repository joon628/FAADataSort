import pymysql

def connect(host, user, password):
    conn = pymysql.connect(host=host, user=user, password=password, db='mysql', charset='utf8')
    curs = conn.cursor()
    return conn, curs

def insert(data):
    conn, curs = connect("127.0.0.1", "root", '')
    temp = data['ns2:TATrackAndFlightPlan']['record']
    for i in temp:
        if type(i) != type("string"):
            g = i.get('track')
            if g:
                time = i['track']['mrtTime']
                acAddress = i['track']['acAddress']
                lon = i['track']['lon']
                lat = i['track']['lat']
                reportedAltitude = i['track']['reportedAltitude']

                sql = f"INSERT INTO ground_data.generic (time,acAddress,lon,lat,alt) values {time,acAddress,lon,lat,reportedAltitude}"
                curs.execute(sql)
                conn.commit()
