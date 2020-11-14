from data_base import DataBase
from role import Role
from user import User

db = DataBase.connect('../data/movie_ticket_system.sqlite')
role = Role.create_table(db)
user = User.create_table(db)
