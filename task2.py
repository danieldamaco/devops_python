import argparse
import http.client
from dotenv import load_dotenv
import os
import json 
import tabulate

parser = argparse.ArgumentParser(description='Survey')
parser.add_argument('-n', help='Name of new survey')
parser.add_argument('-l', help='List all the existing surveys', action="store_const", const=True)

args = parser.parse_args()

load_dotenv()  # Carga variables desde .env
access_key = os.getenv("ACCESS_KEY")
url = os.getenv("API_URL")

conn = http.client.HTTPSConnection(url)
headers = {
    'Content-Type': "application/json",
    'Accept': "application/json",
    'Authorization': f'Bearer {access_key}'
    }

#Si hay un error de conexion debe cachar el error y mandar un mensaje a consola/ 
#Consultar la lista de surveys existentes. 
if args.l:
    try:
        conn.request("GET", "/v3/surveys", headers=headers)
        res = conn.getresponse()
        data = res.read()
        
        if res.status != 200: raise Exception("There was a problem listing the survey(s)")
        
        data_parsed = json.loads(data.decode('utf-8'))


        tabla = [
            ['NAME', 'ID']
        ]
        
        for survey in data_parsed['data']:
            survey_temp = []
            survey_temp.append(survey['title'])
            survey_temp.append(survey['id'])
            tabla.append(survey_temp)

        print(tabulate.tabulate(tabla, headers="firstrow"))

    except Exception as err:
        print(err)

#El usuario quiere crear el survey 
    #Si no existe debe mandar un error 
if args.n:
    name = args.n
    if len(name) == 0: raise Exception("No name provided")
    try:
        payload = f'{{"title":"{name}"}}' 
        conn.request("POST", "/v3/surveys", payload, headers)
        res = conn.getresponse()
        data = res.read()
        if res.status != 201: raise Exception("Something went wrong creating the survey :(")

        data_parsed = json.loads(data.decode('utf-8'))

        tabla = [
            ['NAME', 'ID']
        ]
        tabla.append([data_parsed['title'], data_parsed['id']])
        print("Survey created successfully")
        print(tabulate.tabulate(tabla, headers="firstrow"))

    except Exception as err:
        print(err)

#El usuario quiere consultar un survey 
    #Requiere el ID del survey 
    #Si no existe el ID debe mandar error

#El usuario quiere ver los usuarios que la contestaron 
    #Requiere el ID del survey 
    #Si no existe el ID debe mandar error

