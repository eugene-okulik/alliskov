import json


class Flower:
    has_petals = True
    has_a_smell = True
    has_a_stem = True

    def __init__(self, datafile):
        self.datafile = datafile
        self.data = self.convert_data_to_dict()
        self.price_usd = self.data['price_usd']
        self.wilting_time_in_days = self.data['wilting_time_in_days']
        self.petal_color = self.data['petal_color']
        self.stem_length = self.data['stem_length']

    def convert_data_to_dict(self):
        new_dict = dict(self.read_data_from_file())
        return new_dict

    def read_data_from_file(self):
        file = open(self.datafile, 'r')
        data = json.load(file)
        file.close()
        return data

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'


class Lavender(Flower):

    def __init__(self, datafile):
        super().__init__(datafile)
        self.subtype = self.data['subtype']

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'


class Rose(Flower):

    def __init__(self, datafile):
        super().__init__(datafile)
        self.subtype = self.data['subtype']
        self.has_thorns = self.data['has_thorns']

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'


class Peony(Flower):

    def __init__(self, datafile):
        super().__init__(datafile)
        self.subtype = self.data['subtype']

    def __str__(self):
        return f'{self.data}'

    def __repr__(self):
        return f'{self.data}'


class Bouquet:

    def __init__(self, *kwargs):
        self.flowers = list(kwargs)
        self.bouquet_price = f'Стоимость букета: {self.count_bouquet_price()} USD'
        self.wilting_time = f'Время увядания букета: {self.count_bouquet_lifetime()} дней'
        self.count_bouquet_price()
        self.count_bouquet_lifetime()
        self.sort_flowers_by_wilting()
        self.sort_flowers_by_petal_color()
        self.sort_flowers_by_stem_length()
        self.sort_flowers_by_price()

    def count_bouquet_price(self):
        return round(sum(flower.price_usd for flower in self.flowers), 2)

    def count_bouquet_lifetime(self):
        return round(sum(flower.wilting_time_in_days for flower in self.flowers) / len(self.flowers))

    def sort_flowers_by_wilting(self, descending=False):
        if descending:
            return sorted(self.flowers, key=lambda flower: flower.wilting_time_in_days, reverse=True)
        else:
            return sorted(self.flowers, key=lambda flower: flower.wilting_time_in_days)

    def sort_flowers_by_petal_color(self, descending=False):
        if descending:
            return sorted(self.flowers, key=lambda flower: flower.petal_color, reverse=True)
        else:
            return sorted(self.flowers, key=lambda flower: flower.petal_color)

    def sort_flowers_by_stem_length(self, descending=False):
        if descending:
            return sorted(self.flowers, key=lambda flower: flower.stem_length, reverse=True)
        else:
            return sorted(self.flowers, key=lambda flower: flower.stem_length)

    def sort_flowers_by_price(self, descending=False):
        if descending:
            return sorted(self.flowers, key=lambda flower: flower.price_usd, reverse=True)
        else:
            return sorted(self.flowers, key=lambda flower: flower.price_usd)

    def find_flower_by_wilting_time(self, value):
        return [flower for flower in self.flowers if getattr(flower, 'wilting_time_in_days') == value]


rose_1 = Rose('./files/rose1.json')
rose_2 = Rose('./files/rose2.json')
lavender_1 = Lavender('./files/lavender1.json')
peony_1 = Peony('./files/peony1.json')
peony_2 = Peony('./files/peony2.json')

new_bouquet = Bouquet(rose_1, rose_2, lavender_1, peony_1, peony_2)

print(new_bouquet.bouquet_price)
print(new_bouquet.wilting_time)
print(new_bouquet.sort_flowers_by_wilting())
print(new_bouquet.sort_flowers_by_stem_length(True))
print(new_bouquet.sort_flowers_by_petal_color())
print(new_bouquet.sort_flowers_by_price(True))
print(new_bouquet.find_flower_by_wilting_time(14))
