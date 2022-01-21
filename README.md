sensor2notion

![](https://raw.githubusercontent.com/iayanpahwa/holiday-star/master/assets/cover.jpg)

[Balena](https://balena.io) ❤️ [Notion](http://notion.so) 

## Introduction

Notion meets Physical Computing : Log sensor data to a Notion Database
--------------------
## Use Case

I build this project for my personal use case, but feel free to adopt it for your's.

An year ago I started tracking my habits in a Notion database, things such as- What time I woke up? and went to bed? My total screen time. If I exercised and listened to Music in a day, how many cups I had in a day and what was my overall mood throughout the day. 

I noticed any day where I had more then 3 cups of coffee or had coffee after 7PM that day I felt really anxious, it was later verified once I cut down my caffeine intake.

With this project I want to add few more things in that database such as Temperature, Humidity and Air Quality with a hope to find some patterns in order to better improve my habits and lifestyle.
--------------------
## What it does 

- Fetch outside temperature and Air Quality of your area from [OpenWeatherMap API](http://openweathermap.org/)(free tier subscription should be more than enough).
- Fetch Inside temperature and Humidity using sensors
- Upload this as entry to your habit tracking DB with a date and other fields.
--------------------
## Notion Template

I've created a small [Notion template](https://codensolder.notion.site/codensolder/Daily-Habit-Tracker-template-53dc7f0c300e4aa09dfe59dd68a2d05b) here which you can adapt for your use case. just click the [hyperlink](https://codensolder.notion.site/codensolder/Daily-Habit-Tracker-template-53dc7f0c300e4aa09dfe59dd68a2d05b) and duplicate into your notion workspace.

--------------------
## Hardware required

- A Raspberry Pi computer 
- 16GB Micro-SD Card (recommended Sandisk Extreme Pro SD cards)
- Power supply(s)
- Raspberry Pi SenseHAT (currently supported) 
--------------------
## Software required

- balenaCloud account (free)
- adafruitIO account (free)
- balenaEtcher (optional)(free) - to flash the SD card with balenaOS
- balenaCLI (optional)(free) - if using balena push to deploy the fleet

--------------------
## Deploy a fleet

You can deploy this app to a new balenaCloud fleet in one click using the button below:


[![deploy button](https://balena.io/deploy.svg)](https://dashboard.balena-cloud.com/deploy?repoUrl=https://github.com/iayanpahwa/sensor2notion)


Or, you can create a fleet in your balenaCloud dashboard and `balena push` this code to it, the traditional way.

--------------------

#### Configuring Weather and Notion APIs

The following [Device Configuration](https://www.balena.io/docs/learn/manage/configuration/#configuration-variables) variables are required, these can be set at balenaCloud dashboard :


| Name                                  | Value                                                                                     |
| ------------------------------------- | ----------------------------------------------------------------------------------------- |
| WEATHER_API_KEY                       | API key received after signing up on http://openweathermap.org/
| TEMP_UNIT                             | default is ```metric``` but can ```imperial``` or ```kelvin```                            |
| LAT                                   | Latitude of your location                                                                 |
| LON                                   | Longitude of your location                                                                |
| NOTION_API_KEY                        | API key received from notion                                                              |
| DATABASE_ID                           | Page ID of notion database                                                                |

