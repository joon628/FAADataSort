import pymysql

def connect(host, user, password):
    conn = pymysql.connect(host=host, user=user, password=password, db='mysql', charset='utf8')
    curs = conn.cursor()
    return conn, curs

def insert_flight(data):
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

def insert_ground(data):
    conn, curs = connect("127.0.0.1", "root", '')
    temp = data['ns2:asdexMsg']['mlatReport']
    full = temp['full']

    if type(temp) != type("string"):
        if temp.get('report'):
            if temp['report'].get('basicReport'):
                basic_report = temp['report']['basicReport']
                if basic_report.get('time'):
                    time = basic_report['time']
                else:
                    time = None
                if basic_report.get('position'):
                    if basic_report['position'].get('lon'):
                        lon = basic_report['position']['lon']
                    else:
                        lon = 0
                    if basic_report['position'].get('lat'):
                        lon = basic_report['position']['lat']
                    else:
                        lon = 0 
                if basic_report.get('track'):
                    track = basic_report['track']
                else:
                    track = 0
            if full == 'true':
                acAddress = temp['report']['acAddress']
            else:
                acAddress = None
            


    for i in temp:
        if type(i) != type("string"):
            g = i.get('track')
            if g:
                time = i['track']['mrtTime']
                acAddress = i['track']['acAddress']
                lon = i['track']['lon']
                lat = i['track']['lat']
                reportedAltitude = i['track']['reportedAltitude']

                sql = f"INSERT INTO ground_data.ground (time,acAddress,lon,lat,alt) values {time,acAddress,lon,lat,reportedAltitude}"
                curs.execute(sql)
                conn.commit()
