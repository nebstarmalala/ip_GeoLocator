import pygeoip
import requests

ip_addr = requests.get('https://api.ipify.org').text

gip = pygeoip.GeoIP('GeoLiteCity.dat')
res = gip.record_by_addr(ip_addr)

for key, val in res.items():
    print(f'{key} : {val}')