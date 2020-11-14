from data_base import DataBase
from role import Role

db = DataBase.connect('../data/movie_ticket_system.sqlite')
role = Role.create_table(db)
