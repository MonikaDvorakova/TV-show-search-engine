import click
from CT_functions import (set_current_date, set_week_day,
                          download_TVlisting_xml, replace_special_characters,
                          find_show_in_TVlisting)


url = "https://www.ceskatelevize.cz/services-old/programme/xml/schedule.php"


@click.command()
@click.argument("name")
@click.option("--date", help="Write the date in dd.mm.yyyy format.")
@click.option("--channel", multiple=True, help="Write the channel(s) for the searching (ct1, ct2, ct4, ct24, ct5, ct6)")
def find_show(name, date, channel):
    all_channels = ['ct1', 'ct2', 'ct24', 'ct4', 'ct5', 'ct6']
    if date:
        date = date
    else:
        date = set_current_date()
    if channel:
        channels = channel
    else:
        channels = all_channels
    modified_name = replace_special_characters(name) #removes special characters
    xml_roots = download_TVlisting_xml(date, channels, url) #download xml files and saves them as a root
    set_week_day(date) # prints day of the week and date
    find_show_in_TVlisting(xml_roots, modified_name) #prints time and channel of the show broadcasting


def shows_name_time(root):
    for porad in root:
        cas = porad.find('cas').text
        for popisky in porad.findall('nazvy'):
            nazev = popisky.find('nazev')
            print(nazev.text, cas)


def find_show_time(root, show_name):
    for porad in root:
        cas = porad.find('cas').text
        for popisky in porad.findall('nazvy'):
            nazev = popisky.find('nazev').text
            if nazev == show_name:
                print(f'{show_name}: {cas}')


if __name__ == "__main__":
    find_show()