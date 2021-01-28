#!/bin/bash

echo "Step 1: Parse SSID"
tshark -Y 'wlan.ssid eq "KFC Hostspot"' -r 400kpackets.pcapng | sed "s/→//g" > out

echo "Step 2: Count SSID's"
cat out | sort | uniq | wc -l
