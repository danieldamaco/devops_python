import argparse
import http.client
import json 

parser = argparse.ArgumentParser()
parser.add_argument('-menu', help='Show meny to users')
parser.add_argument('-create', help='Create a new order')
parser.add_argument('-status', help="Check order's status")
parser.add_argument('-admin', help='Access admin features. It is required an access token.')
parser.add_argument('-add_pizza', '-ap', help='Add a pizza to the menu. Admin permission is requiered.')
parser.add_argument('-delete_pizza', '-dp',  help='Delete a pizza to the menu. Admin permission is requiered.')

parser.add_argument('-n', help='Your name')

args = parser.parse_args()
conn = http.client.HTTPConnection('127.0.0.1', 5000)

if args.create:
    #Necesito name y tipo de pizza como body: es a /orders en POST. Recibo JSON de error o de order con: (name, status, pizza)
    body = {"name": f'{args.n}', "pizza-type": f'{args.create}'}
    body = json.dumps(body)
    try:
        conn.request("POST", '/api/orders', body=body)
        res = conn.getresponse()
        data = res.read()

        data_parsed = json.loads(data.decode('utf-8'))
        print(f' El id es: {data_parsed['order']['id']}')
    except Exception as err:
        print(err)

elif args.menu:
     #Necesito name y tipo de pizza como body: es a /orders en POST. Recibo JSON de error o de order con: (name, status, pizza)
    try:
        conn.request("GET", '/api/menu')
        res = conn.getresponse()
        data = res.read()

        data_parsed = json.loads(data.decode('utf-8'))
        print(f' El menu es: {data_parsed['menu']}')
    except Exception as err:
        print(err)

elif args.status:
    #Necesito el id del pedido como pathparam. es a /orders/<orderid>. Recibo error o JSON con order_is y status. 
    try:
        conn.request("GET", f'/api/orders/{args.status}')
        res = conn.getresponse()
        data = res.read()

        data_parsed = json.loads(data.decode('utf-8'))
        print(f' El status es: {data_parsed['status']}')
    except Exception as err:
        print(err)
    
elif args.add_pizza:
    try:
        if not args.admin: raise Exception("Accion solo para adminsitradores.")
        body = {"name": f'{args.n}', "new_pizza": f'{args.add_pizza}'}
        body = json.dumps(body)
        headers = {
            'Content-Type': "application/json",
            'Accept': "application/json",
            'Authorization': f'Bearer {args.admin}'
        }

        conn.request("POST", f'/api/menu', body=body, headers=headers)
        res = conn.getresponse()
        data = res.read()

        data_parsed = json.loads(data.decode('utf-8'))
        print(f'{data_parsed['success']}')

    except Exception as err:
        print(err)

elif args.delete_pizza:
    print('estoy en delete_pizza')
    #Verificar si esta la flag de admin. Y mandar para saber si es correcta. 
    #Necesito admin token. En el body necesito delete_pizza. Recibo mensaje de success
    try:
        if not args.admin: raise Exception("Accion solo para adminsitradores.")
        body = {"name": f'{args.n}', "delete_pizza": f'{args.delete_pizza}'}
        body = json.dumps(body)
        headers = {
            'Content-Type': "application/json",
            'Accept': "application/json",
            'Authorization': f'Bearer {args.admin}'
        }

        conn.request("POST", f'/api/menu', body=body, headers=headers)
        res = conn.getresponse()
        data = res.read()

        data_parsed = json.loads(data.decode('utf-8'))
        print(f'{data_parsed['success']}')

    except Exception as err:
        print(err)

else:
    print('estoy en opcion incorrecta')
    #Lanzar error de no valido 
 