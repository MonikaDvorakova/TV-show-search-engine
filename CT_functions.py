import requests
import xml.etree.ElementTree as et
import datetime


def set_current_date():
    """It sets the current date in the required format."""
    current_datetime = datetime.datetime.now()
    current_date = current_datetime.strftime("%d.%m.%Y")
    return current_date


def set_week_day(date):
    """It sets the day of the week and prints it out together with the date."""
    week = ["pondělí", "úterý", "středa", "čtvrtek", "pátek",
            "sobota", "neděle"]
    day, month, year = date.split('.')
    modified_date = datetime.date(int(year), int(month), int(day))
    day_of_week = week[modified_date.weekday()]
    print(f'{day_of_week}, {date}:')


def get_login():
    """It loads the login from the file."""
    with open('login.txt') as file:
        login = file.read().strip()
    return login


def download_TVlisting_xml(date, channels, url):
    """It downloads the xml format of the TV listing and returns root as
    an ElementTree object. It downloads xml for every selected channel
    and it saves it in a dictionary, which it returns."""
    login = get_login()
    xml_roots = {}
    for channel in channels:
        channel = channel  # Tento radek tu nemusi byt?
        parameters = {'user': login, 'date': date, 'channel': channel}
        response = requests.get(url, params=parameters)
        response.encoding = 'utf-8'
        root = et.fromstring(response.text)
        xml_roots[channel] = root
    return xml_roots


def replace_special_characters(name):
    """It converts all upercase characters to lowercase and replaces
    all special characters of the czech alphabet and returns
    changed string."""
    name = name.lower()
    special_characters = {'á': 'a', 'é': 'e', 'ě': 'e', 'í': 'i', 'ý': 'y',
                          'ó': 'o', 'ú': 'u', 'ů': 'u', 'č': 'c', 'ď': 'd',
                          'ň': 'n', 'ř': 'r', 'š': 's', 'ť': 't', 'ž': 'z'}
    for letter in name:
        if letter in special_characters:
            name = name.replace(letter, special_characters[letter])
    return name


def find_show_in_TVlisting(xml_roots, name):
    """It looks up the show in the TV listing of the channels and
    returns the channel(s) and the time of the broadcasting."""
    found_results = []
    for channel, root in xml_roots.items():
        for show in root:
            time = show.find('cas').text
            for branch in show.findall('nazvy'):
                show_name = branch.find('nazev').text
                modified_name = replace_special_characters(show_name)
                if modified_name == name:
                    found_results.append([time, channel, show_name])
    if found_results:
        for time, channel, show_name in found_results:
            print(f'{show_name}: {time}, {channel}')
    else:
        print('The TV show is not in the TV listing for the selected day and/or the selected channel(s).')