import unittest
from teste01 import get_formatted_name

class NamesTestCase(unittest.TestCase): #Teste para a função de teste01.py
    
    def test_first_last_name(self): #Nomes como 'Janis Joplin' funcionam?
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

unittest.main()