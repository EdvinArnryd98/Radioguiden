import json
import urllib.request


def get_channels():
    api_url = 'https://api.sr.se/api/v2/channels?format=json'
    response = urllib.request.urlopen(api_url)
    answer = response.read()
    json_dict = json.loads(answer)

    channels = json_dict["channels"]

    return channels


def print_channels(channels):
    number = 0
    for x in channels:
        print(x["name"], number)
        number += 1


def count_channels(channels):
    stations_amount = len(channels)
    return stations_amount


def user_command(choice):
    # Create a function that gets called everytime the page is changed of the stations and return the amount of
    # stations are in the list
    channels = get_channels()
    number_of_channels = count_channels(get_channels())
    if choice < 0:
        print("Wrong input! Try again")

    elif choice < number_of_channels:
        # print the table of selected channel
        print(channels[choice]["id"], channels[choice]["name"])
        return channels[choice]["id"]

    else:
        print("Choice is out of bounds!")


if __name__ == '__main__':
    running = 1
    print_channels(get_channels())

    while running:
        station = int(input("Pick a station with its number: "))
        current_station = user_command(station)
