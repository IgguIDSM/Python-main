class ExcecaoCustom(Exception):
    pass;

x = - 1;
if x < 0:
    raise Exception('Valor Negativo!');

x = 'hello';
if not type(x) is int:
    raise TypeError('Use apenas Inteiros!!!!');