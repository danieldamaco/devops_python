import argparse
import http.client
from dotenv import load_dotenv
import os
import json 
import tabulate

parser = argparse.ArgumentParser(description='Survey')
parser.add_argument('-n', help='Name of new survey')
parser.add_argument('-l', help='List all the existing surveys', action="store_const", const=True)
parser.add_argument('-c',help='Provide the files name' )

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

internal_ids = {}
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
#if args.n:

"""
The script should accept a JSON file with questions for the survey and a text file with a list of email addresses.
The structure of a JSON file with questions:
There should be at least 3 questions and 2 recipients.
"""
#Necesito crear una survey
    #Para las preguntas debo parsear el formato del json al que me pide la api 
#Necesito crear una collection
#Necesito crear un messege 
#Como se hace asincronismo en python

#Parse the input json file
def question_parser(num, question,  choices):
    """
    Convertion of input json file to json requirements for API
    """
    answers = [{"text": answer} for answer in choices]
    question = {
        "headings": [
            {
                "heading": question
            }
        ],
        "position": num,
        "family": "single_choice",
        "subtype": "vertical",
        "answers": {
            "choices": answers
        }
    }
    return question
def survey_parser(title, questions):
    new_survey = {
        "title": title,
        "pages": [
            {
            "questions": questions
            }
        ]
    }
    return new_survey


if args.c:
    #Extract the content of json file. 
    content = {}
    try:
        #Condicional de si su extension en json o no 
        f = open(args.c, "r", encoding="utf-8")
        with f:
            content = json.load(f)
            if len(content) == 0: raise Exception('Empty file.')
            
    except FileNotFoundError as err:
        print('File not found')


    #Obtain que question and answers from json file 
    questions = content['quiz_1']['1']

    #Parse the content to APIs requirements 
    qsts = []
    for num, question in enumerate(questions.keys()):
        answers = questions[question]['Answers']
        qsts.append(question_parser(num+1, question=question, choices=answers))

    survey = survey_parser(title='quiz_1', questions=qsts)


    #Creating survey 
    try:
        survey_json_parsed = json.dumps(survey)
        conn.request("POST", "/v3/surveys", survey_json_parsed, headers=headers)
        res = conn.getresponse()
        data = res.read()
        if res.status != 201: raise Exception("Something went wrong creating the survey :(")
        data_parsed = json.loads(data.decode('utf-8'))

        print(data_parsed)
        internal_ids['survey_id'] = data_parsed['id']
        print("New survey created successfuly.")

    except Exception as err:
        print(err)