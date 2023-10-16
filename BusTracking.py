import mysql.connector as ms
db = ms.connect(
    host='localhost',
    user='root',
    password='dpsbn',
    database='hk')
cursor = db.cursor()
def busdet(busid):
    q1 = 'select bus_id,emission_compliance,fuel_type,vehicle_no from buses where bus_id=%s'
    cursor.execute(q1, (busid,))
    a = cursor.fetchall()
    for k in a:
        for g in k:
            if k.index(g)==0:
                print('BUS ID:',g)
            elif k.index(g)==1:
                print('EMMISSION NORMS:',g)
            elif k.index(g)==2:
                print('FUEL TYPE:',g)
            elif k.index(g)==3:
                print('VEHICLE NUMBER:',g)
def ckbloc():
    import requests

def get_google_maps_link(busid):
    base_url = "https://www.google.com/maps?q="
    q1 = 'SELECT latitude, longitude FROM buses WHERE bus_id=%s'
    cursor.execute(q1, (busid,))
    coordinates = cursor.fetchone()

    if coordinates:
        latitude, longitude = float(coordinates[0]), float(coordinates[1])
        google_maps_link = f"{base_url}{latitude},{longitude}"
        return google_maps_link
    else:
        return None
bus_id = 'BUS002'
link = get_google_maps_link(bus_id)
if link:
    print(link)
else:
    print(f"No coordinates found for bus ID {bus_id}")
busid = input("Enter the Bus ID:")
google_maps_link = get_google_maps_link(busid)
print(google_maps_link)
busdet(busid)
