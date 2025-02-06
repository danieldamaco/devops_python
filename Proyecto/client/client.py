import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-create', help='Create a new order')
parser.add_argument('-status', help="Check order's status")
parser.add_argument('-cancel', help='Cancel an order if not ready to be delivered')
parser.add_argument('-admin', help='Access admin features. It is required an access token.')
parser.add_argument('-add_pizza', '-ap', help='Add a pizza to the menu. Admin permission is requiered.')
parser.add_argument('-delete_pizza', '-dp',  help='Delete a pizza to the menu. Admin permission is requiered.')

args = parser.parse_args()

if args.create:
    print('estoy en create')
    #Necesito name y tipo de pizza como body: es a /orders en POST. Recibo JSON de error o de order con: (name, status, pizza)
elif args.status:
    print('estoy en status')
    #Necesito el id del pedido como pathparam. es a /orders/<orderid>. Recibo error o JSON con order_is y status. 
elif args.cancel:
    print('estoy en cancel')
    #Aun no implementado uwu
elif args.add_pizza or args.ap:
    print('estoy en add_pizza')
    #Verificar si esta la flag de admin. Y mandar para saber si es correcta. 
    #Necesito admin token. En el body necesito new_pizza. Recibo mensaje de success
elif args.delete_pizza or args.dp:
    print('estoy en delete_pizza')
    #Verificar si esta la flag de admin. Y mandar para saber si es correcta. 
    #Necesito admin token. En el body necesito delete_pizza. Recibo mensaje de success
else:
    print('estoy en opcion incorrecta')
    #Lanzar error de no valido 
 