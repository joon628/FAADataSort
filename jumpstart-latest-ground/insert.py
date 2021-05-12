import pymysql
import sys
def connect(host, user, password):
    conn = pymysql.connect(host=host, user=user, password=password, db='generic')
    curs = conn.cursor()
    return conn, curs

def insert_flight(data):
    conn, curs = connect("faaflightdata.cjawgfwlolns.us-east-2.rds.amazonaws.com", "admin", "Olinflightdata21")
    temp = data['ns2:TATrackAndFlightPlan']['record']
    for i in temp:
        if type(i) != type("string"):
            if i.get('track'):
                if i['track'].get('mrtTime'):
                    time = i['track']['mrtTime']
                else:
                    time = None

                if i['track'].get('acAddress'):
                    acAddress = i['track']['acAddress']
                else:
                    acAddress = 'NAN'

                if i['track'].get('lon'):
                    lon = i['track']['lon']
                else:
                    lon = 0

                if i['track'].get('lat'):
                    lat = i['track']['lat']
                else:
                    lat = 0

                if i['track'].get('reportedAltitude'):
                    reportedAltitude = i['track']['reportedAltitude']
                else:
                    reportedAltitude = 1000000001

                sql = f"INSERT INTO generic.track(time,acAddress,lon,lat,alt) values {time,acAddress,lon,lat,reportedAltitude}"
                curs.execute(sql)
                conn.commit()

def insert_ground(data):
    conn, curs = connect("faaflightdata.cjawgfwlolns.us-east-2.rds.amazonaws.com", "admin", "Olinflightdata21")

    temp = data['ns2:asdexMsg']['mlatReport']

    for i in temp:
        if type(i) != type("string"):
            if i.get('report'):
                if i['report'].get('basicReport'):
                    basic_report = i['report']['basicReport']
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
                            lat = basic_report['position']['lat']
                        else:
                            lat = 0
                    if basic_report.get('track'):
                        track = basic_report['track']
                    else:
                        track = 0

            if i.get('full'):
                full = i[full]
                print(repr(full))
                print(sys.exc_info())
                if full == 'true':
                    print(repr('True'))
                    acAddress = i['report']['acAddress']
                else:
                    print(repr('False'))
                    if time is not None:
                        date = time[0:10]
                        sql = f"SELECT acAddress FROM generic.ground WHERE DATE(time) = {date} AND track = {track}"
                        curs.execute(sql)
                        matching_address = curs.fetchall()
                        if matching_address == ():
                            acAddress = 'NAN'
                        else:
                            acAddress = matching_address[-1]
                    else:
                        acAddress = 'NAN'
            sql = f"INSERT INTO generic.ground (time,acAddress,track,lon,lat) values {time,acAddress,track,lon,lat}"
            curs.execute(sql)
            conn.commit()
