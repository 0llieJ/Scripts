print ("I am back again\nThis is the code behind the mac_changer.py")
---------------------------------------------------------------------------------------------------------------
# Mac_Changer, using moduels, specfically the *subprocess* moduel. These will execute system commands. 
# There are loads of different moduels which can be used in python
# Syntax*
# import subprocess
# subprocess.call("COMMAND",Shell=true)

import subprocess
subprocess.call("ifconfig", shell=True)
---------------------------------------------------------------------------------------------------------------
# Now we want to change to change the MAC address automatically, through Python
#!usr/bin/env python
import subprocess
subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:66", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)
---------------------------------------------------------------------------------------------------------------
# This is good but we need a MAC address which will change automatically.
# We are going to use *variables* to do this.
# Variables store infomration which contains a certain value
# Rememeber your actual interface has to be wlan0

#!usr/bin/env python

# Assigning values to variables
import subprocess

# Below are examples of variables
interface = "wlan0"
new_mac = "00:11:22:33:44:77"

print('[+] Changing MAC address for ' + interface + " to " + new_mac)

subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 00:11:22:33:44:66", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)
---------------------------------------------------------------------------------------------------------------
#!usr/bin/env python
import subprocess

# We now just have to change the interface value or the mac address value for it to work with whatever you want.
interface = "wlan0"
new_mac = "00:11:22:33:44:77"

print('[+] Changing MAC address for ' + interface + " to " + new_mac)

# Now we are calling the variable within our submoduel
subprocess.call("ifconfig" + interface + "down", shell=True)
subprocess.call("ifconfig" + interface + "hw ether" + new_mac, shell=True)
subprocess.call("ifconfig" + interface + "up", shell=True)
---------------------------------------------------------------------------------------------------------------
#!usr/bin/env python
import subprocess
# To change the values of the variable we would have to come into the code, instead lets use the *input* function which will allow us to have choice in what the interface and MAC becomes.
interface = input("interface >")
new_mac = input("new MAC >")

print('[+] Changing MAC address for ' + interface + " to " + new_mac)

subprocess.call("ifconfig" + interface + "down", shell=True)
subprocess.call("ifconfig" + interface + "hw ether" + new_mac, shell=True)
subprocess.call("ifconfig" + interface + "up", shell=True)
---------------------------------------------------------------------------------------------------------------
# shell=True can be a security hazard.
# This is now in a list, rather than a string, it is harder for an attacker to hyjack the command.
# Note, lists are done with [] brackets

import subprocess
interface = input("interface >")
new_mac = input("new MAC >")

print('[+] Changing MAC address for ' + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
---------------------------------------------------------------------------------------------------------------
# Whilst we have user input, it is not very integrated. Let's use another moduel 'optparse'
import subprocess
import optparse

# Teaching the parser what it can do
parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

# Below is allowing the user to pass arguments
(options, arguments) = parser.parse_args()

interface = options.interface
new_mac = options.new_mac

print('[+] Changing MAC address for ' + interface + " to " + new_mac)

subprocess.call(["ifconfig", interface, "down"])
subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
subprocess.call(["ifconfig", interface, "up"])
---------------------------------------------------------------------------------------------------------------
#!usr/bin/env python
# Now we are going to use function,
import subprocess
import optparse

# Where I am going to store the function
def change_mac(interface, new_mac):
     print('[+] Changing MAC address for ' + interface + " to " + new_mac)

     subprocess.call(["ifconfig", interface, "down"])
     subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
     subprocess.call(["ifconfig", interface, "up"])

parser = optparse.OptionParser()

parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

(options, arguments) = parser.parse_args()

# Going to remove the two lines below because we have made them a function.
# interface = options.interface
# new_mac = options.new_mac

# The function for storing interface and the new mac
change_mac(options.interface, options.new_mac)

# We can put this in a function so we don't have to keep typing this code. 
# You can see above it then stored in the funtion before.
# print('[+] Changing MAC address for ' + interface + " to " + new_mac)

# subprocess.call(["ifconfig", interface, "down"])
# subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
# subprocess.call(["ifconfig", interface, "up"])
---------------------------------------------------------------------------------------------------------------
#!usr/bin/env python
import subprocess
import optparse

#New function
def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    return parser.parse_args()


def change_mac(interface, new_mac):
     print('[+] Changing MAC address for ' + interface + " to " + new_mac)
     subprocess.call(["ifconfig", interface, "down"])
     subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
     subprocess.call(["ifconfig", interface, "up"])

(options, arguments) = get_arguments()
change_mac(options.interface, options.new_mac)

# We have condensed the code into functions and told the code to return the option and argument commands.
---------------------------------------------------------------------------------------------------------------
# We are gonna look at "IF" statements
# Only executing code based on certain conditions

# Example 1
if *condition*
    Code to execute when 
    Condition is true
else:
    Code to execute when
    condition is false
# Rest of code

# Example 2
if condition1:
    code to execute when
    condition1 is true
elif condition2:
    code to execute when
    condition2 is true AND
    condition1 is false
else:
    code to execute when
    all conditions are false
# Rest of code
# elif (else if)

# Example 3
if condition1:
    code to execute when
    condition1 is true
if condition2:
    code to execute when
    condition2 is true
# Rest of code
---------------------------------------------------------------------------------------------------------------
#!usr/bin/env python
import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args() #Values and arguments entered by the user
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
        #code to handle an error, error being they haven't inputted any info
    elif not options.new_mac:
         parser.error("[-] Please specify an interface, use --help for more info")
        #code to handle an error, error being they haven't inputted any info
    return options


def change_mac(interface, new_mac):
     print('[+] Changing MAC address for ' + interface + " to " + new_mac)
     subprocess.call(["ifconfig", interface, "down"])
     subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
     subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
change_mac(options.interface, options.new_mac)
---------------------------------------------------------------------------------------------------------------
# Going to add functionality, so it displays the MAC address so we don't have to manually check it
# First we need to execute and read system commands which in this case, would be *ifconfig* through subprocess.check_output

#!usr/bin/env python
import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args() #Values and arguments entered by the user
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
        #code to handle an error, error being they haven't inputted any info
    elif not options.new_mac:
         parser.error("[-] Please specify an interface, use --help for more info")
        #code to handle an error, error being they haven't inputted any info
    return options


def change_mac(interface, new_mac):
     print('[+] Changing MAC address for ' + interface + " to " + new_mac)
     subprocess.call(["ifconfig", interface, "down"])
     subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
     subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
# change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interfacce])
---------------------------------------------------------------------------------------------------------------
# Step 2 of automting the MAC address output process
# We are going to implement Regex (Regular expressions) allows to search for rules or patterns
# The MAC address uses character, character, colon and it is alphanumeric. So we would us the Regex expression, \w\w:
# 

#!usr/bin/env python
import subprocess
import optparse

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change MAC address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args() #Values and arguments entered by the user
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
        #code to handle an error, error being they haven't inputted any info
    elif not options.new_mac:
         parser.error("[-] Please specify an interface, use --help for more info")
        #code to handle an error, error being they haven't inputted any info
    return options


def change_mac(interface, new_mac):
     print('[+] Changing MAC address for ' + interface + " to " + new_mac)
     subprocess.call(["ifconfig", interface, "down"])
     subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
     subprocess.call(["ifconfig", interface, "up"])

options = get_arguments()
# change_mac(options.interface, options.new_mac)

ifconfig_result = subprocess.check_output(["ifconfig", options.interfacce])