"""
Write a script that gets system information like distro info, memory(total, used, free), CPU info (model, core numbers, speed), current user, system load average, and IP address. Use arguments for specifying resources. (For example, -d for distro -m for memory, -c for CPU, -u for user info, -l for load average, -i for IP address).
"""

import argparse
import subprocess

#debo revisar el sistema operativo. 

def command_runner(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr  = process.communicate()
    return (stdout.decode('utf-8'), stderr.decode('utf-8'))

parser = argparse.ArgumentParser()
parser.add_argument("-d", action="store_const", const="True")
parser.add_argument("-m", action="store_const", const="True")
parser.add_argument("-c", action="store_const", const="True")
parser.add_argument("-u", action="store_const", const="True")
parser.add_argument("-l", action="store_const", const="True")
parser.add_argument("-i", action="store_const", const="True")

args = parser.parse_args()

if args.d: 
    stdout, stderr = command_runner(command='uname -a')
    print(f'Information of kernel:\n{stdout}')

if args.m: 
    stdout, stderr = command_runner(command="sysctl vm.swapusage | awk '{print $2, $3, $4, $5, $6, $7, $8, $9, $10}'")
    print(f'Information of RAM Memory (MB):\n{stdout}')

if args.c: 
    stdout, stderr = command_runner(command='sysctl -n machdep.cpu.brand_string')
    print(f'Model = {stdout}')

    stdout, stderr = command_runner(command='sysctl -n machdep.cpu.core_count')
    print(f'Number of Cores = {stdout}')

    stdout, stderr = command_runner(command='sysctl -n machdep.cpu.thread_count')
    print(f'Threads = {stdout}')

    stdout, stderr = command_runner(command='echo "$(echo "$(sysctl -n hw.cpufrequency) / 1000000000" | bc -l) GHz"')
    print(f'Frecuency = {stdout}')

if args.u: 
    stdout, stderr = command_runner(command='whoami')
    print(f'Current user: ', stdout)

if args.l: 
    stdout, stderr = command_runner(command="uptime | awk '{print $11, $12, $13}'")
    print(f'Load average: ', stdout)

if args.i: 
    stdout, stderr = command_runner(command="ipconfig getifaddr en0")
    print(f'External IP address: ', stdout)
