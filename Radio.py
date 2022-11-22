import urllib.request
import xmltodict


api_url = 'https://api.sr.se/api/v2/channels'

response = urllib.request.urlopen(api_url)

answer = response.read()

parsed_answer = xmltodict.parse(answer)

channels = parsed_answer["sr"]["channels"]["channel"]

#Prints out all stations
number = 0
for x in channels:
    print(x["@name"], number)
    number += 1

running = 1


def pick_station(choice):

    if choice > 9:
        print("Wrong input! Try again")

    else:
        print(channels[choice])
        return channels[choice]["@id"]


if __name__ == '__main__':
    while running:
        station = int(input("Pick a station with it's number: "))
        current_station = pick_station(station)

