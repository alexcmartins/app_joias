from faker import Faker

fake = Faker('pt_BR')


def generator_jewel():
    return {
        'name': fake.name(),
        'models': fake.word(),
        'weight': fake.random_number(digits=2, fix_len=True),
        'metal': fake.word(),
        'stone': fake.word(),
        'foundry': fake.name(),
        'workshop': fake.name(),
        'value': fake.random_number(digits=5),
        'note': fake.text(),
        'cover': {
            'url': 'https://loremflickr.com/320/240/jewel'
        }
    }


# print(generator_jewel())

if __name__ == '__main__':
    from pprint import pprint
    pprint(generator_jewel())
