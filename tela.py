from conexaoAPI import get_character_by_name,get_image

dados= get_character_by_name('Spider')

for char in dados['data']['results']:
    print('------------------------')
    print(f'ID:{char["id"]}')
    print(f'Nome:{char["name"]}')
    #print(f'Imagem:{char["thumbnail"]["path"]}.{char["thumbnail"]["extension"]}')
    # for series in char["series"]["items"]:
    #     print(f'Série:{series["name"]}')
    # for events in char["events"]["items"]:
    #     print(f'Eventos:{events["name"]}')
    imagem=f'{char["thumbnail"]["path"]}.{char["thumbnail"]["extension"]}'
    get_image(imagem,{char["name"]})
