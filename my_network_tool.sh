#!/bin/bash 

#Creating a menu interface 
echo "Menu
1) Check Network Interface Information
2) Ping a Host
3) Port Scan with Nmap 
4) Display Routing Table 
5) Traceroute to Host
6) Exit"

#Request prompt from the user by selecting one option from the menu
echo "Select the option from the Menu"
read option 
echo "Executing $option"

#Create a script using if statements to check the network interface information 
if [ $option -eq 1 ]; then
ip a
else
echo "Menu 1:Locked";

fi 

#Repeat the process but this time to ping a host 
if [ $option -eq 2 ]; then
echo "What host you want to ping?"
read host
ping -c 3 $host
else 
echo "Menu 2:Locked"

fi

#Use if and case statements for the nmap to work to it's full potential. 
if [ "$option" -eq 3 ]; then
    echo "What host do you want to scan?"
    read host

    echo "What kind of scan do you want to do?"
    echo "1) Quick Scan"
    echo "2) Full Scan"
    echo "3) Specific Port Scan"
    read scan

    case "$scan" in
        1)
            echo "Quick Scan on $host..."
            nmap -F "$host"
            ;;
        2)
            echo "Full Scan on $host..."
            nmap -p- "$host"
            ;;
        3)
            echo "Enter the port number(s) to scan"
            read ports
            echo "Scanning ports: $ports on $host..."
            nmap -p "$ports" "$host"
            ;;
        *)
            echo "Invalid choice. Exiting."
            exit 1
            ;;
    esac
else
    echo "Menu 3: Locked"
fi

#Create a script to display the routing table  
if [ $option -eq 4 ]; then 
ip route 
else 
echo "Menu 4:Locked" 

fi

#Create a script to traceroute a specific host
if [ $option -eq 5 ]; then
echo "Enter host to traceroute to"
read host 
traceroute $host
else
echo "Menu5:Locked" 

fi

#Create a script to exit from the menu
if [ $option -eq 6 ]; then
echo "Exiting..." 
exit 0 
else 
echo "Menu 6:Locked" 

fi

