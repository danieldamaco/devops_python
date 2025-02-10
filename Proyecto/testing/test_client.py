import unittest
import subprocess
from backend import create_app
import sys
import os

class Clienttest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.idOrder = None 
    
    def test_create_and_name(self):
        process = subprocess.Popen("python3 ./Proyecto/client/client.py -n Daniel -create pepperoni", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr  = process.communicate()
        stdout = stdout.decode('utf-8')
        id = stdout.split()
        id = id[-1]
        Clienttest.idOrder = id
        self.assertIn('El id es: ', stdout, id)

    def test_menu_show_current_menu(self):
        process = subprocess.Popen("python3 ./Proyecto/client/client.py -menu hola", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr  = process.communicate()
        stdout = stdout.decode('utf-8')
        self.assertIn('El menu es: ', stdout, stdout)


    def test_status_of_order_created(self):
        process = subprocess.Popen(f"python3 ./Proyecto/client/client.py -status {Clienttest.idOrder}", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr  = process.communicate()
        stdout = stdout.decode('utf-8')
        self.assertIn('El status es: created', stdout, stdout)
    
    def test_add_pizza_authenticated(self):
        process = subprocess.Popen(f"python3 ./Proyecto/client/client.py -add_pizza pizzaTest -admin UnTokenSeguro", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr  = process.communicate()
        stdout = stdout.decode('utf-8')
        self.assertIn('Nueva pizza agregada con éxito', stdout, stdout)

    def test_delete_pizza_authenticated(self):
        process = subprocess.Popen(f"python3 ./Proyecto/client/client.py -delete_pizza pizzaTest -admin UnTokenSeguro", shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr  = process.communicate()
        stdout = stdout.decode('utf-8')
        self.assertIn('Pizza eliminada con éxito', stdout, stdout)


if __name__ == '__main__':
    unittest.main()