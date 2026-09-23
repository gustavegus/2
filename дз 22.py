сундук = { 'location': 'Пещера дракона',
           'gold': 250,
            'items': [ 
                {'name': 'старый меч', 'value': 30, 'type': 'weapon'},
        {'name': 'магический амулет', 'value': 120, 'type': 'accessory'},
        {'name': 'зелье удачи', 'value': 50, 'type': 'зелье'}],
        'locked': False}
print(f"золото : {сундук['gold']}")
сундук['gold'] += 50
print(f"вы нашли еще золотые монеты ! : {сундук['gold']}")
vtoroq_predmet = сундук['items'][1]['name']
print(f"второй предмет : {vtoroq_predmet}")