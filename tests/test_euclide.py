from euclide import pgcd


def test_pgcd_when_gcd_greater_than_1():
    x = 15
    y = 21
    g = pgcd(x, y)
    assert g == 3

def test_pgcd_when_both_are_1():
    x = 1
    y = 1
    g = pgcd(x, y)
    assert g == 1    

def test_pgcd_when_first_is_1():
    x = 1
    y = 7
    g = pgcd(x, y)
    assert g == 1    

# TODO: faire les autres cas : 
# 2 nbs premiers, ...
# 2 nbs de la suite de Fibonacci
# cas d'erreurs : nbs <=0