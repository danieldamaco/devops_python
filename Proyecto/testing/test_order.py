import unittest
import json
import uuid
from backend import create_app

class OrderTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls): #Se ejecuta antes de todos los tests. 
        cls.app = create_app()
        cls.client = cls.app.test_client() 

    def test_orders_post_response_and_status(self):
        headers = {"Authorization": "Bearer UnTokenSeguro", "Content-Type": "application/json"}
        body = {"name": "daniel", "pizza-type": "pepperoni"}
        body = json.dumps(body)
        response = self.client.post('/api/orders', data=body, headers=headers) #Mandar una petición post
        self.assertEqual(response.status_code, 200, response.data) #Verificar el response status
        self.assertIn("order", response.json)
        self.assertIn("id", response.json["order"])
        self.assertEqual(response.json["order"]["status"], "created")

    def test_menu_get_response_and_status(self): 
        response = self.client.get(f'/api/orders/{uuid.uuid4()}') #Mandar una petición get
        self.assertEqual(response.status_code, 200) #Verificar el response status
        self.assertDictEqual(response.json, {'error': 'Id no valido'}) #Verificar el json de respuesta. 
    
    
    def test_menu_delete_response_and_status(self):
        headers = {"Authorization": "Bearer UnTokenSeguro", "Content-Type": "application/json"}
        body = {"name": "daniel", "delete_pizza": "sin carne"}
        body = json.dumps(body)
        response = self.client.delete(f'/api/orders/{uuid.uuid4()}', data=body, headers=headers) #Mandar una petición post
        self.assertEqual(response.status_code, 200, response.data) #Verificar el response status
        self.assertDictEqual(response.json, {'error': 'Id no valido'}) #Verificar el json de respuesta. 


    @classmethod
    def tearDownClass(cls): #Se ejecuta al terminar las pruebas. (Borrar archivos temporales o conexiones a)
        #cerrar db y server. 
        pass

if __name__ == '__main__':
    unittest.main()