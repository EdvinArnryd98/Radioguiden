import json
import urllib.request
# import datetime
import time


class User:
  def __init__(self, id, page):
    self.id = id
    self.page = page


user = User(0, 1)


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
    channels = get_channels()
    number_of_channels = count_channels(get_channels())
    if choice < 0:
        print("Wrong input! Try again")

    elif choice < number_of_channels:
        scheduled_episodes(channels[choice]["id"])
        user.id = channels[choice]["id"]
        return channels[choice]["id"]

    elif choice == 10:
        user.page = user.page + 1
        save_id = user.id
        next_pages(save_id, user.page)
        print("page:", user.page)

    else:
        print("Choice is out of bounds!")


def scheduled_episodes(id):
    api_url = f"https://api.sr.se/v2/scheduledepisodes?channelid={id}&format=json&page={1}"
    response = urllib.request.urlopen(api_url)
    answer = response.read()
    json_dict = json.loads(answer)

    scheduledepisodes = json_dict["schedule"]

    number = 0
    for x in scheduledepisodes:
        my_num_1 = int(''.join(filter(str.isdigit, x["starttimeutc"])))
        date_date = my_num_1
        date = time.strftime('%m/%d/%Y %H:%M:%S',
                             time.gmtime(date_date/1000.))
        print(date + " " + x["title"])
        number += 1


def next_pages(id, schedul_page):
    api_url = f"https://api.sr.se/v2/scheduledepisodes?channelid={id}&format=json&page={schedul_page}"
    response = urllib.request.urlopen(api_url)
    answer = response.read()
    json_dict = json.loads(answer)

    scheduledepisodes = json_dict["schedule"]

    number = 0
    for x in scheduledepisodes:
        my_num_1 = int(''.join(filter(str.isdigit, x["starttimeutc"])))
        date_date = my_num_1
        date = time.strftime('%m/%d/%Y %H:%M:%S',
                             time.gmtime(date_date/1000.))
        print(date)
        print(x["title"])
        number += 1


if __name__ == '__main__':
    running = 1
    print_channels(get_channels())

    while running:
        station = int(input("Pick a station with its number: "))

        # Build a function that resets the pages, if the number is 11, set user.page to 1
        # Create a menu at the beginning of the program to tell the user what different numbers do


        current_station = user_command(station)
