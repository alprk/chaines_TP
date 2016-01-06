# coding: utf-8 
def getNext(password):
    """
    Série de tests exprimés en doctest
    >>> getNext('a')
    'b'
    >>> getNext('az')
    'ba'
    >>> getNext('bc')
    'bd'
    """
    pwd = list(password)  #1 # On crée un tableau de la taille de la chaine envoyée en argument (password) ( en explosant les caractères ) 
    found = False
    i=len(pwd)-1

    while not found:
        if pwd[i] < 'z':
           pwd[i] = chr(ord(pwd[i])+1)  #2.1 Retourne la lettre en ASCII  du caractère à l'indice i
		   # 2.2  ajoute +1 ,
		   # 2.3  retourne le nouveau code ASCII en Caractère alpha
           found = True             
        else:
           i = i-1
           pwd[i+1] = 'a'
    
    return ''.join(pwd) #3 Assemble le tableau de chaine par des '' et retourne la chaine final



# Grâce à ce fragment de code, si vous exécutez ce fichier, les tests doctests seront exécutés également. 
# Si vous ne voulez plus que les tests s'exécutent, commentez les deux lignes ci-dessous. 
# Si vous préférez lancer vos tests à la main, commentez également les lignes, et utilisez "python -m doctest pass.py" en console. 
if __name__ == "__main__":
    import doctest
    doctest.testmod()
