import random
def run():
    secret_num = random.randint(0, 100)
    resp = int(input('intenta adivinar el numero: '))

    
    while resp != secret_num:
        if resp > secret_num:
            print('el numero es mas pequeno')
        else:
            print('el numero es mas grande')
        resp = int(input('intenta adivinar el numero: '))
    else:
        print(f'el numero era {secret_num} acertaste')





if __name__ == '__main__':
    run()