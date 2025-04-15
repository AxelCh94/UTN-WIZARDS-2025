resultado = None
a = 10
b = 0
try:
    resultado = a / b # modificamos
except TypeError as e:
    print(f'TypeError - Ourrio un error: {type(e)}')
except ZeroDivisionError as e:
    print(f'ZeroDivicionError - Ocurrio un error: {type(e)}')
except Exception as e:
    print(f'Exception - Ocurrio un error: {type(e)}')

print(f'El resultado es: {resultado}')
print('seguimos ...')
