# weatherino

This project is a microclimate mapping system in development. I mean to create cheap weather stations (sub $10) and
have them feed data in 10 byte packets back to the mother ship for analysis.

There are 4 components:

1. A server
2. A weatherino
3. A database


# Device

The arduino has 4 attachments:

1. Sim800L for communication
2. 9v battery (or another pack style) for power
3. Hiletgo LM393 Rain Detector to determine precipitation
4. BME280 for humidity and temperature


# Server

The server needs 2 components:

1. An endpoint for the weatherino to send its packets
2. An endpoint for me to see what we have

# Database

1 table:

| id | device | datetime | battery | rain | temperature | humidity |

# Packets

We will send packets every 10 minutes. It will be just bytes and contain the following values:

battery|rain|humidity|temp

This is 4 bytes.

4*(24*60/10)=slightly more than half a kilo a day

Battery will be replaceable.

we'll put the whole thing in a zip lock bag.

# Cost Per Device

| Item | Cost | Notes |
|----|----|----|
| Sim Card | $1 | |
| Phone # | $1 | |
| Sim800L | $0.10 | I think I can get this really cheap on alibaba |
| BME280 | $0.10 | Alibaba |
| LM393 | $0.50 | Alibaba |
| 9v | 1.20 | Amazon |
| 9v connector | 0.50 | Amazon |
| Arduino Nano | 0.70 | Alibaba
Total = 
