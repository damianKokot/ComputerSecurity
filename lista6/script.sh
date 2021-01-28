#!/bin/bash

# Damian Kokot

for passwrd in $(strings ./login)
do
 cp ./login temp.out
 bilal=$(./temp.out $passwrd | grep -v "Unauthorized")
 if [ "$bilal" != '' ]
 then
   printf "\nThe password is: %s\n" "$passwrd"
   ./temp.out $passwrd
 fi
done