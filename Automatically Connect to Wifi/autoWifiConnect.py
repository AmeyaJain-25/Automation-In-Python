#check saved networks, check available network from saved one, ask user to connect to which one, disconnect present or current network, 
#if asked network is not available then cut the program, if network asked is available then connect

import os
import sys
import time

#os.popen()   opens a pipe between program and command prompt to run the command and returns and open file object connected to the pipe

show_saved_network_cmd = os.popen("netsh wlan show profiles").read()        #reads the command that need to be put there in command prompt using os and popen

show_available_network_cmd = os.popen("netsh wlan show network").read()     #shows available network

print("Available Networks are: \n", show_available_network_cmd)    #show the connections available to user in display screen

preffered_network_ssid = input("Enter preferred Wifi for your Connection: ")     #ask for the preffered connection for the user

disconnect_current_network = os.popen("netsh wlan disconnect").read()           #disconnects the current connection

print(disconnect_current_network)



#is preferred id is there in saved connection, then connect, else go and connect

if preffered_network_ssid not in show_saved_network_cmd:
    print("The network", preffered_network_ssid, " is not saved in the System")
    print("Connection establishment UNSUCCESSFUL")
    time.sleep(1)
    sys.exit()
else:
    print("The network", preffered_network_ssid, " is saved in the System")
    print("Connection establishment in Process")
    time.sleep(1)


#Check if the Network preferred is available or not
while True:
    if preffered_network_ssid in show_available_network_cmd:
        print("The preferred Network", preffered_network_ssid, "is Found")
        time.sleep(0.5)
        break
    

print("------Connecting------")
time.sleep(2)
#Connect with the network
os.popen("netsh wlan connect name=" + '"' + preffered_network_ssid + '"')