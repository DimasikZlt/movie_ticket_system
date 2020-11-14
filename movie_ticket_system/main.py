from data_base import DataBase
from movie import Movie
from user import User

db = DataBase.connect('../data/movie_ticket_system.sqlite')
user = User.create_table(db)
movie = Movie.create_table(db)
