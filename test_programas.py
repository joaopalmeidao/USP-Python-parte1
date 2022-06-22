from tkinter import E
from maximo import maximo
from maior_primo import maior_primo as mp
from vogais import vogal as vog
from fizzbuzz_funcao import fizzbuzz as fb
from maximo_3 import maximo as max
# Teste Máximo
def test_maximo1():
    assert maximo(3,4)==4
def test_maximo2():
    assert maximo(0,-1)==0

# Teste Maior Primo
def test_mp1():
    assert mp(100)==97
def test_mp2():
    assert mp(7)==7

#Teste Vogal
def test_vog1():
    assert vog('a')==True
def test_vog2():
    assert vog('b')==False
def test_vog3():
    assert vog('E')==True

# teste FizzBuzz 
def test_fb1():
    assert fb(3)=='Fizz'
def test_fb2():
    assert fb(5)=='Buzz'
def test_fb3():
    assert fb(15)=='FizzBuzz'
def test_fb4():
    assert fb(4)==4

# Teste Maximo com 3 parametros
def test_max1():
    assert max(30,14,10)==30
def test_max2():
    assert max(0,-1,1)==1
