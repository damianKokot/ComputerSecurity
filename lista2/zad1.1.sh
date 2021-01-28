#!/bin/bash

echo "Step 1"
tshark -Y 'wlan.fc.type_subtype eq 4' -T fields -e wlan.ssid -r 400kpackets.pcapng
