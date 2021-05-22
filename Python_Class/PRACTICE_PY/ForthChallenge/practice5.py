import math

def run():
    rad_cil = int(input('ingresa el numero de radio: '))
    prof_cil = int(input('ingresa la profundidad: '))
    
    volumen = math.pi * rad_cil **2* prof_cil

    print(volumen)
    print(round(volumen, 2))



if __name__ == '__main__':
    run()