# The TV-show-search-engine

The program is the command-line application and it uses Click library to set the commands.

The program looks up the selected TV show in the TV listing of Česká televize.
For the selected day, it prints out at what time and on what channel(s) the show is broadcast.
The TV listing is provided by Česká televize in XML format on webpage https://www.ceskatelevize.cz/xml/tv-program/
after registration.

## Requirements
* Python 3
* requests library
* click library

## Authentication
All requests to the program must be authenticated using your username (registration here:
https://www.ceskatelevize.cz/xml/tv-program/registrace/).

## How to use it and examples
* Register here: https://www.ceskatelevize.cz/xml/tv-program/registrace/.
* Create login.txt file and save there your username.
* Use CT_prohledavac.py to run the program
* Use the command:

 **python CT_prohledavac.py "The show name"**, if you want to see the result for today and all CT channels.

* Use the command:

 **python CT_prohledavac.py "The show name" --date "date in dd.mm.yyyy format"**, if you want to see the result for a specific day.
 
* Use the command:

 **python CT_prohledavac.py "The show name" --channel "channel from a list (ct1, ct2, ct4, ct24, ct5, ct6)"**,
 if you want to see the result for a specific channel.
 
 * you can use multiple commands for --channels.
 
 * The command:
 
 **python CT_prohledavac.py udalosti --date 14.01.2020 --channel ct1 --channel ct2**,
 
 finds if the show "Udalosti" is in the TV listing of CT1 and CT2 channels on 14th January 2020.
 
 
