# receber a temperatura em celsius do usuario como decimal em uma variavel
print("lembre-se de usar '.' no lugar da ','!")
var_celsius = float(input('digite a temperatura em °c:'))

# execute a formula e armazenar em uma variavel
var_fahrenheit = var_celsius * 9/5 +32
# exibe no terminal co duas casas decimais
print (f'a temperatura e {var_fahrenheit:.2f} °f')
 
 