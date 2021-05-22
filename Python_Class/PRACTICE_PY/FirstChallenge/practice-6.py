#reto 6
def run():
    slice1 = int(input('cuantas rebanadas de pizza traes?: '))
    print('*********')
    sliceres = int(input('cuantas slices comieron?: '))
    
    resta = slice1 - sliceres

    print('quedaron')
    print(resta)
    print('slices de pizza')


if __name__ == '__main__':
    run()