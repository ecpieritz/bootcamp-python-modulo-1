#Sets

city = {'Blumenau', 'Osasco', 'São Paulo', 'Florianópolis', 'Indaial', 'Timbó'}

#sempre mostra desordenadamente
print(city)

#não permitem valores duplicados
city_2 = {'Blumenau', 'Osasco', 'São Paulo', 'Florianópolis', 'Indaial', 'Timbó', 'Blumenau', 'Osasco', 'São Paulo', 'Florianópolis', 'Indaial', 'Timbó', 'Blumenau', 'Osasco', 'São Paulo', 'Florianópolis', 'Indaial', 'Timbó', }
print(city_2)

#checando valores de um set
print('Osasco' in city)
print('Rio de Janeiro' in city)

#adicionando item ao set
city.add('Brusque')
city.add('Urussanga')
print(city)

#unindo sets
city_3 = {'Itajaí', 'Sorocaba', 'Navegantes', 'Foz do Iguaçú'}

city.update(city_3)
print(city)