from geolite2 import geolite2
import requests

def get_ip_location(my_ip):
    reader = geolite2.reader()
    location = reader.get(my_ip)

    a=(location['city']['names']['en'])
    b=(location['continent']['names']['en'])
    c=(location['country']['names']['en'])
    d=(location['location'])
    e=(location['postal'])
    f=(location['registered_country']['names']['en'])
    g=(location['subdivisions'][0]['names']['en'])

    print('''city: %s\ncontinent: %s\nlocation: %s\npostal: %s\nregistered_country: %s\nsubdivision: %s'''% (a,b,c,d,e,f,g))


my_ip = requests.get('https://api.ipify.org').text

get_ip_location(my_ip)
