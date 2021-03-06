#strings

street = "Rua Benno Mohr"
number = '97'
district = 'Salto Weissback'
city = "Blumenau"
state = 'SC'
country = 'Brasil'


#concatenando uma string

address = street + ', ' + number + ', bairro ' + district + ', ' + city + '/' + state + ' - ' + country

print(address)

#maiúsculo
address_upper = address.upper()
print(address_upper)

#minúsculo
address_lower = address.lower()
print(address_lower)