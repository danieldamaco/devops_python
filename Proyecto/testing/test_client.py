import unittest
import subprocess

class Clienttest(unittest.TestCase):
    pass
    #test create 'El id es: {data_parsed['order']['id']}'
    #test menu 'El menu es: {data_parsed['menu']}'
    #test status  El status es: {data_parsed['status']}
    #test add_pizza 'success'
    #test delete pizza 'success'

    #test create falla 'El id es: {data_parsed['order']['id']}'
    #test menu falla 'El menu es: {data_parsed['menu']}'
    #test status  falla El status es: {data_parsed['status']}
    #test add_pizza falla 'success'
    #test delete pizza falla 'success'

if __name__ == '__main__':
    unittest.main()