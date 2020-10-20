def run():
    pregunta1 = input('esta lloviendo?: ')
    resp_posi = ['si', 'Si','SI']
    resp_neg = ['no','No','NO']
    

    if pregunta1 in resp_posi:
        pregunta2 = input('y esta haciendo mucho viento?: ')
    else:
        print('ok, ten un lindo dia jejeps')
    
    if pregunta2 in resp_posi:
        print('no lleves sombrilla ve en carro')
    else:
        print('lleva sombrilla')


if __name__ == '__main__':
    run()