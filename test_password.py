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
        
    def test_hasSeries_f(self):
        self.asserEqual(pwd.hasSeries("baaac"),False)
        
    def test_hasSeries_t(self):
        self.asserEqual(pwd.hasSeries("baabc"),True)

    def test_hasTwoPairs_f(self):
        self.asserEqual(pwd.hasTwoPairs("baaac"),False)
        
    def test_hasTwoPairs_t(self):
        self.asserEqual(pwd.hasTwoPairs("bffcu"),True)
        
    def test_hasNoBadChar_f(self):
        self.asserEqual(pwd.hasNoBadChar("jolie"),False)
        
     def test_hasNoBadChar_t(self):
        self.asserEqual(pwd.hasNoBadChar("bffcu"),True)
            
# Permet d'exécuter les tests si ce fichier est exécuté
unittest.main()
