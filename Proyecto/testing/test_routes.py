import unittest
from backend import create_app
import subprocess
import time 
import json

class RoutingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls): #Se ejecuta antes de todos los tests. 
        cls.app = create_app()
        cls.client = cls.app.test_client()
        #Aqui podria iniciar el servidor y la base de datos redis. 
    
    def test_menu_get_response_and_status(self): 
        response = self.client.get('/api/menu') #Mandar una petición get
        self.assertEqual(response.status_code, 200, response.data) #Verificar el response status
        res = response.json
        self.assertEqual(res, {'menu': '{\'types\': "[\'pepperoni\', \'mexicana\', \'tres quesos\', \'carnes frias\']"}'}, res) #Verificar el json de respuesta. 
    
    def test_menu_post_response_and_status(self):
        headers = {"Authorization": "Bearer UnTokenSeguro", "Content-Type": "application/json"}
        body = {"name": "daniel", "new_pizza": "sin carne"}
        body = json.dumps(body)
        response = self.client.post('/api/menu', data=body, headers=headers) #Mandar una petición post
        self.assertEqual(response.status_code, 201, response.data) #Verificar el response status
        self.assertDictEqual(response.json, {"success": "Nueva pizza agregada con éxito"}) #Verificar el json de respuesta. 

    def test_menu_delete_response_and_status(self):
        headers = {"Authorization": "Bearer UnTokenSeguro", "Content-Type": "application/json"}
        body = {"name": "daniel", "delete_pizza": "pepperoni"}
        body = json.dumps(body)
        response = self.client.delete('/api/menu', data=body, headers=headers) #Mandar una petición post
        self.assertEqual(response.status_code, 200,  response.data) #Verificar el response status
        self.assertDictEqual(response.json, {"success": "Pizza eliminada con éxito"}) #Verificar el json de respuesta. 


    @classmethod
    def tearDownClass(cls): #Se ejecuta al terminar las pruebas. (Borrar archivos temporales o conexiones a)
        #cerrar db y server. 
        pass

if __name__ == '__main__':
    unittest.main()