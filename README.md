# whatsapp_spammer

This is the readme for a WhatsApp Bot, which automaticaly send messages to a contact in WhatsApp Web


## Requiriments
* Python 3.6
* pip
* Selenium

## Installing Selenium
##### Install python package
```
pip3 install -U selenium
```
##### Download Firefox driver
 
```
https://github.com/mozilla/geckodriver/releases
```
Unzip and copy geckodriver to folder */usr/bin* or */usr/local/bin*



## Setings
The `data.json` file contains the spawn contents, it must be defined:

| variables        | description|
| ------------- |--------------:|
| contact_name                              | target contact's name in your phone |
| messages                                  | list of messages to send           |


This variables define how the bot will work, you don't need change them:

| min_delay and max_delay                   | delay between messages              |
| min_interval & max_interval               | big delay between messages          |
| min_count2interval & min_count2interval   | count of messages for big delay     |


## Running

- run bot.py
    ```
    python bot.py
    ```
- wait firefox opens WhatsApp Web's page
- login in WhatsApp Web
- press Enter in terminal


