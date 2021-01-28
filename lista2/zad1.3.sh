#!/bin/bash

echo "Step 1: parse domains"
tshark -T fields -Y dns -e dns.qry.name -r 400kpackets.pcapng > domains

echo "Step 2: count domains"
cat domains | sort | uniq -c | sort -rn
