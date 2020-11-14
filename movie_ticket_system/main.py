from data_base import DataBase
from user import User

db = DataBase.connect('../data/movie_ticket_system.sqlite')
user = User.create_table(db)
