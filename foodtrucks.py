import requests
import sodapy
import datetime

now = datetime.datetime.now()
hour_now = now.strftime("%H")
today = "{}".format(now.strftime("%A"))
url = "https://data.sfgov.org/resource/bbb8-hzi6.json?"
response = requests.get(url)
if response.status_code == 200:
    response_list = response.json()


# def all_foodtrucks():
#     for each_truck in response_list:
#         print("Name:{}  Address:{} Start:{} End:{}".format(
#             each_truck.get('applicant'),
#             each_truck.get('location'),
#             each_truck.get('start24'),
#             each_truck.get('end24'),
#             )
#         )


# all_foodtrucks()

def open_today():
    for each_truck in response_list:
        if (each_truck.get('dayofweekstr') == today:
        print each_truck.get('applicant')
        print each_truck.get('dayofweekstr')


open_today()
