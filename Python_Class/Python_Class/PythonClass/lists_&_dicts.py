def run():
    my_list = [1, 'hello', True, 4,5]
    my_dict = {'name':'lastname', 'lastname':'garcia'}

    super_list = [
        {'name':'lastname', 'lastname':'torres'},
        {'name':'lastname', 'lastname':'garcia'},
        {'name':'lastname', 'lastname':'reyes'},
        {'name':'lastname', 'lastname':'garcia'},
        {'name':'lastname', 'lastname':'ramos'}
    ]
    super_dict = {
        'natural_nums':[1,2,3,4,5],
        'integer_nums':[-1,-2,0,1,2],
        'floating_nums':[1.1,1.2,6.45]
    }

    for key, value in super_dict.items():
        print(key, '-', value)

    
if __name__ == '__main__':
    run()