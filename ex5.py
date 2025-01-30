"""
Write a script that gets system information like distro info, memory(total, used, free), CPU info (model, core numbers, speed), current user, system load average, and IP address. Use arguments for specifying resources. (For example, -d for distro -m for memory, -c for CPU, -u for user info, -l for load average, -i for IP address).
"""

import argparse
import subprocess

#debo revisar el sistema operativo. 

parser = argparse.ArgumentParser()
parser.add_argument("-d", action="store_const", const="True")
parser.add_argument("-m", action="store_const", const="True")
parser.add_argument("-c", action="store_const", const="True")
parser.add_argument("-u", action="store_const", const="True")
parser.add_argument("-l", action="store_const", const="True")
parser.add_argument("-i", action="store_const", const="True")

args = parser.parse_args()
if args.d: 
    process = subprocess.Popen(['uname', '-a'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(f'Information of kernel:\n{stdout.decode('utf-8')}')
if args.m: 
    command = "sysctl vm.swapusage | awk '{print $2, $3, $4, $5, $6, $7, $8, $9, $10}'"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate() 
    print(f'Information of RAM Memory:\n{stdout.decode('utf-8')}')
if args.c: 
    command = 'sysctl -n machdep.cpu.brand_string' #modelo
    answer = ''
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    answer += f'Model = {stdout.decode('utf-8')}'

    command = 'sysctl -n machdep.cpu.core_count' #cores
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    answer += f'Number of Cores = {stdout.decode('utf-8')}'

    command = 'sysctl -n machdep.cpu.thread_count' #Threads
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    answer += f'Threads = {stdout.decode('utf-8')}'

    command = 'echo "$(echo "$(sysctl -n hw.cpufrequency) / 1000000000" | bc -l) GHz"' #Frecuency
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    answer += f'Threads = {stdout.decode('utf-8')}'

    print(f'CPU information:\n',answer)

if args.u: 
    command = 'whoami' #Frecuency
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    print(f'Current user: ', stdout.decode('utf-8'))
    
if args.l: print("load average")
if args.i: print("IP address")
