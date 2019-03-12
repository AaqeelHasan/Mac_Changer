#!/usr/bin/env python3

import subprocess
import optparse
import re

def change_mac(interface,new_mac):
    print("[+]Changing MAC address for " + interface + " to " + new_mac)
    # Changing the mac address
    #subprocess.call("ifconfig " + interface + " down", shell=True)
    #subprocess.call("ifconfig " + interface + " hw ether " + new_mac, shell=True)
    #subprocess.call("ifconfig " + interface + " up ", shell=True)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    
def format_mac(new_mac: str) -> str:
    new_mac = re.sub('[.:-]', '', new_mac).lower()  # remove delimiters and convert to lower case
    new_mac = ''.join(new_mac.split())  # remove whitespaces
    assert len(new_mac) == 12  # length should be now exactly 12 (eg. 008041aefd7e)
    assert new_mac.isalnum()  # should only contain letters and numbers
    # convert mac in canonical form (eg. 00:80:41:ae:fd:7e)
    new_mac = ":".join(["%s" % (new_mac[i:i+2]) for i in range(0, 12, 2)])
    return new_mac

# Command line inputs
parser = optparse.OptionParser()
parser.add_option("-i", "--interface", dest="interface", help="The interface to be changed")
parser.add_option("-m", "--mac", dest="new_mac", help="Enter new MAC address")
(options , arguments) = parser.parse_args()

# Listing the networks
subprocess.call(["ifconfig"])

# Input Command Line arguments
#interface = options.interface
#new_mac = options.new_mac

# Input user variables
interface = input(">Enter Interface to change:")
new_mac = input(">Enter new MAC address: ")
new_mac = format_mac(new_mac)

change_mac(interface,new_mac)

#Displaying the changed MAC address
print("[+]MAC address changed for " + interface + " to " + new_mac)
ifconfig_result = subprocess.check_output(["ifconfig", interface])
subprocess.call(["ifconfig", interface])
#print(ifconfig_result)
#new_mac_address = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
# if new_mac_address:
#     print("The new MAC address is " + new_mac_address)
# else:
#     print("[-]Could not read a MAC address")
