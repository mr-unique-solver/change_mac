#!usr/bin/env python3
import subprocess
import optparse
parser = optparse.OptionParser()
parser.add_option("-i", "--interface",dest="interface",help="this is used to change the mac address")
parser.add_option("-m","--mac",dest="mac_address",help="this is used to change the mac address")
(options,arguments)=parser.parse_args()
subprocess.call(["ifconfig",options.interface,"down"])
subprocess.call(["ifconfig",options.interface,"hw","ether",options.mac_address])
subprocess.call(["ifconfig",options.interface,"up"])


