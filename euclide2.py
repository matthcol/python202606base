# module euclide

# solution #2 pour gérer les arguments en mode CLI
# inclus dans la lib standard de python
import argparse 

# def pgcd(a, b):  # without annotation type (hints)
def pgcd(a: int, b: int) -> int:  # with annotation type (hints)
    while b != 0:
        t = a
        a = b
        b = t % b
    return a

# NB: __name__ = nom du module
# * possibilité 1 : utilisé dans une autre application : __name__ = 'euclide'
# * possibilité 2 : utilisé comme application (point d'entrée) : __name__ = '__main__'
if __name__ == '__main__':
    # paramètrage
    argparser = argparse.ArgumentParser('euclide')
    argparser.add_argument('x', type=int)
    argparser.add_argument('y', type=int)
    # appliquer le paramétrage
    args = argparser.parse_args()
    # récupérer chaque paramètre
    x = args.x
    y = args.y
    # utiliser les paramètres
    g = pgcd(x, y)
    print(f"Le pgcd de {x} et {y} est {g}")