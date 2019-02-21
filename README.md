# CactBot

A simple DiscordBot that uses wrappers to interface with the Discord API. The primary goal is to help trivialize various aspects of raiding management. It interfaces with a Google Sheets to gather available times and present them into the discord client as well as manage loot for the raid team. Google Sheets is used because it is an easy to use interface for non-programmers.

## Getting Started
Simply clone and use your own Discord bot token and Google Drive token and run.

### Prerequisites
Install Python 3.4 to 3.6

Install these plugins:
```
discord.py
oauth2client
gspread
```

To install
```
pep3 install discord
pep3 install oauth2client
pep3 install gspread

```

### Versioning
I use [SemVer](http://semver.org/) for versioning.

### Basic Commands*
```
!help will display all of the available commands
!drops or loot will display various aspects depending on params
!time will display raid times for everyone
!timeedit will edit the times people are available
!joke will tell a funny raid joke
```
*this command list will be updated as the bot is updated

