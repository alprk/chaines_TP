# coding: utf-8 
import unittest
import password as pwd

class TestPassword(unittest.TestCase):

    def test_getNextNormal(self):
        self.assertEqual(pwd.getNext("abcde"), "abcdf")

    def test_getNextEndLine(self):
        self.assertEqual(pwd.getNext("abhzv"), "abhzw")
        
    def test_getNext_zzzzz(self):
        self.assertEqual(pwd.getNext("zzzzz"), "La valeur entrée est incorrecte\nUne erreur devra donc être levée ")

    def test_getNext_password(self):
        self.assertEqual(len("likol"), 5)
        
# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()
