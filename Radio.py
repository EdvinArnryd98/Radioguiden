import json
import urllib.request


api_url = 'https://api.sr.se/api/v2/channels?format=json'
response = urllib.request.urlopen(api_url)
answer = response.read()
json_dict = json.loads(answer)

channels = json_dict["channels"]

#Prints out all stations
number = 0
for x in channels:
    print(x["name"], number)
    number += 1

running = 1


def pick_station(choice):

    if choice > 9:
        print("Wrong input! Try again")

    else:
        print(channels[choice]["id"], channels[choice]["name"])
        return channels[choice]["id"]


if __name__ == '__main__':
    while running:
        station = int(input("Pick a station with its number: "))
        current_station = pick_station(station)
