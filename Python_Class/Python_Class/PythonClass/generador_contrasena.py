import random

def gen_password():
     mayusculas = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O']
     minusculas = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o']
     simbolos = ['!','#','$','&','/','(',')']
     numeros = ['1','2','3','4','5','6','7','8','9','0']

     caracteres = mayusculas + minusculas + simbolos + numeros

     password = []

     for i in range(15):
         caracter_random = random.choice(caracteres)
         password.append(caracter_random)
     
     password = "".join(password) 
     return password


def run():
    password = gen_password()
    print('Your new password is ' + password)


if __name__ == '__main__':
    run()