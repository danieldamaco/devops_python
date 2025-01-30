"""
Create a script that reads the access log from a file. The name of the file is provided as an argument. An output of the script should provide the total number of different User Agents and then provide statistics with the number of requests from each of them. Here is a link to an example access.log file.
"""

import argparse

def add_req(stats, ip, req_type):
    """
    It resolves to which request type must be added on stats dictonary a new entry based on the ip provided. 
    """
    if req_type == '"GET': 
        stats[ip]['GET'] +=1
    elif req_type == '"POST': 
        stats[ip]['POST'] +=1
    else:
        stats[ip]['OTHER'] += 1

parser = argparse.ArgumentParser(description='Path of the file: ')
parser.add_argument('-name', required=True)

args = parser.parse_args().name

stats = {}
try:
    with open(args) as f:
        content = f.readlines()

        if len(content) == 0: raise Exception("NotLinesFounds") #if file empty raise an error

        for line in content:
            line = line.split(" ") #separete lines by spaces 
            ip=line[0]
            if ip in stats: #ip is already on dict 
                add_req(stats, ip, req_type=line[5])
            else: #ip in a new entry on dict 
                stats[ip] = {'GET': 0, 'POST': 0, 'OTHER': 0}
                add_req(stats, ip, req_type=line[5])
    
    total_number = len(stats)
    print(f'Total number different users: {total_number}\nIPs and their respective request types:\n', stats)

except FileNotFoundError as err:
    print('File not found')
except Exception as err:
    print(f'{err.args[0]}: The file is empty')


