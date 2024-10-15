PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

articles = PRICE_LIST.split()[0::2]
prices = PRICE_LIST.split()[1::2]
prices = [price.strip('p,р') for price in prices]
prices = [int(price) for price in prices]
# prices = [int(price) for price in [s.strip('p,р') for s in PRICE_LIST.split()[1::2]]]
new_dict = dict(zip(articles, prices))

print(new_dict)
