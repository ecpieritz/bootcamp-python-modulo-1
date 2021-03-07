#dictionary (dict)

cod_uf = {
    21: 'Maranhão',
    22: 'Piauí',
    23: 'Ceará',
    24: 'Rio Grande do Norte',
    25: 'Paraíba',
    26: 'Pernambuco',
    27: 'Alagoas',
    28: 'Sergipe',
    29: 'Bahia'
}
print(type(cod_uf))

#valores ordenados
print(cod_uf.values())

#duplicados não são permitidos
cod_uf_2 = {
    21: 'Maranhão',
    22: 'Piauí',
    23: 'Ceará',
    24: 'Rio Grande do Norte',
    25: 'Paraíba',
    26: 'Pernambuco',
    27: 'Alagoas',
    28: 'Sergipe',
    29: 'Bahia',
    21: 'Maranhão',
    22: 'Piauí',
    23: 'Ceará',
    24: 'Rio Grande do Norte',
    25: 'Paraíba',
    26: 'Pernambuco',
    27: 'Alagoas',
    28: 'Sergipe',
    29: 'Bahia'
}
print(cod_uf_2)

#acessando os valores
print(cod_uf.get(24))
print(cod_uf.keys())

#adicionando novos valores
cod_uf[47] = 'Santa Catarina'
cod_uf[11] = 'São Paulo'
print(cod_uf)