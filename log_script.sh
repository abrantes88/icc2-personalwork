#!/bin/bash


#Using the $ sign to tell bash that we need to run whatever is inside the parentheses as a command 
date1=$(date +%Y-%m-%d) 
date2=$(date +%H:%M:%S)


echo "$date1 $date2 User: $USER - Log Entry: Logged in successfully" 
echo "$date1 $date2 User: $USER - Log Entry: Logged in successfully" >> user_activity.log.txt

