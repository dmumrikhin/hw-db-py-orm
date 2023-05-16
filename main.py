import sqlalchemy
import json, os
from sqlalchemy.orm import declarative_base, relationship, sessionmaker
from models import create_tables, Publisher, Book, Shop, Stock, Sale

login = os.getenv('PGLOG')
pasw = os.getenv('PGPASS')
base_name = os.getenv('PGBASE')
base_address = os.getenv('PGADDRESS')

DSN = (f'postgresql://{login}:{pasw}@{base_address}/{base_name}')

engine = sqlalchemy.create_engine(DSN) 
# create_tables(engine)

Session = sessionmaker(bind=engine)
session = Session()

# with open('/Users/a1/files/tests_data.json') as file:
#     data = json.load(file)

# for record in data:
#     model = {
#         'publisher': Publisher,
#         'shop': Shop,
#         'book': Book,
#         'stock': Stock,
#         'sale': Sale,
#     }[record.get('model')]
#     session.add(model(id=record.get('pk'), **record.get('fields')))

Pub_id = input('Введите айди издателя: ')

ps = session.query(Publisher.name, Book.title, Sale.price, Sale.date_sale
    ).join(Book).join(Stock).join(Shop
    ).join(Sale).filter(Publisher.id == Pub_id).all()
for item in ps:
    print(f'{item[1]}'.ljust(40)+f'| {item[0]}'.ljust(10
                    )+f' | {item[2]} | {item[3]}')

session.close

