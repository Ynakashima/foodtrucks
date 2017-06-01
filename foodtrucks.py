import requests
import sodapy
import datetime

now = datetime.datetime.now()
hour_now = now.strftime("%H")
today = now.strftime("%A")
url = "https://data.sfgov.org/resource/bbb8-hzi6.json"
response = requests.get(url)
if response.status_code == 200:
    response_list = response.json()


def open_today():
    for each_truck in response_list:
        if each_truck.get('dayofweekstr') == today:
            print("Name:{}  Address:{}".format(
                each_truck.get('applicant'),
                each_truck.get('location')
                )
            )

open_today()
