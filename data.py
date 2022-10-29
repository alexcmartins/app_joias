from faker import Faker

fake = Faker('pt_BR')


def generator_jewel():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'name': fake.name(),
        'code': fake.word(),
        'category': fake.word(),
        'models': fake.word(),
        'genre': fake.word(),
        'weight': fake.random_number(digits=2, fix_len=True),
        'length': fake.random_number(digits=2, fix_len=True),
        'width': fake.random_number(digits=2, fix_len=True),
        'height': fake.random_number(digits=2, fix_len=True),
        'thickness': fake.random_number(digits=2, fix_len=True),
        'metal': fake.word(),
        'stones': {
            'types': "Diamond",
            'origin': "Japanese",
            'amount': fake.random_number(digits=2, fix_len=True),
            'size': "0.03",
            'carat': "0.08",
            'value': "1.650"
        },
        'services': {"1": {
            'metal_stones_pearls': "metal",
            'provider': "provider1",
            'service': "service2",
            'value': "45",
        },
            "2": {
            'metal_stones_pearls': "stones",
            'provider': "provider3",
            'service': "service1",
            'value': "98",
        }},
        'stone': fake.word(),
        'foundry': fake.name(),
        'workshop': fake.name(),
        'value': float(fake.random_number(digits=5)),
        'note': fake.text(600),
        'cover': {
            'url': 'https://loremflickr.com/1920/1080/gold'
        }
    }


def generator_contact():
    return {
        'id': fake.random_number(digits=2, fix_len=True),
        'name': fake.name(),
        'lastName': fake.word(),
        'instagram': fake.word(),
        'mobile': fake.random_number(digits=11),
        'houseoffice': fake.random_number(digits=11),
        'company': fake.company(),
        'birthday': fake.date(),
        'address': fake.address(),
        'email': fake.email(),
        'note': fake.text(600)
    }


# print(generator_jewel())

if __name__ == '__main__':
    from pprint import pprint
    pprint(generator_jewel())


if __name__ == '__main__':
    from pprint import pprint
    pprint(generator_contact())
