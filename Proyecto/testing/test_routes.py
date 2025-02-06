import unittest
from backend import create_app

class RoutingTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls): #Se ejecuta antes de todos los tests. 
        cls.app = create_app()
        cls.client = cls.app.test_client()
        #Aqui podria iniciar el servidor y la base de datos redis. 
    
    def test_menu_get_response_and_status(self): 
        response = self.client.get('/menu') #Mandar una petición get
        self.assertEqual(response.status_code, 200) #Verificar el response status
        self.assertDictEqual(response.json, {"menu": "['pepperoni', 'mexicana', 'tres quesos', 'carnes frias']"}) #Verificar el json de respuesta. 
    
    #Falta hacer lo de post y el de delete 
    def test_menu_post_response_and_status(self):
        pass

    def test_menu_delete_response_and_status(self):
        pass

    @classmethod
    def tearDownClass(cls): #Se ejecuta al terminar las pruebas. (Borrar archivos temporales o conexiones a)
        #cerrar db y server. 
        pass

if __name__ == '__main__':
    unittest.main()