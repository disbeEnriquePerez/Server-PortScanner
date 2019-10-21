#!/usr/bin/python3
#we are going to create an Nmap scanner for scripts
import nmap
from FunctionsforScanner import *

scanner = nmap.PortScanner()

print("Welcome, this is a simple nmap automation tool")
print("<-------------------------------------------------->")

ip_addr = input("Please enter the IP address you want to scan: ")

print("The IP you entered is: ", ip_addr)
type(ip_addr)
resp = response()

print("You have selected option: " , resp)

if int(resp) == 1:
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-7000', '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif int(resp) == 2:
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-500', '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif int(resp) == 3:
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, '1-1024', '-v -sS - sV -sC -A -O')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
