from typing import List, Dict, Optional
from pydantic import BaseModel


# class Player(BaseModel):
#     player_name: str
#     player_deposit: int
#     player_items: List[Dict[str, int]]
#     player_friends: List[str] = []
#     player_souvenir: Optional[str] = None
#
#
# player1 = Player(player_name='qpaHma3eP', player_deposit=10000, player_items=[{'Швабра': 1}])
# print(vars(player1))


# class User(BaseModel):
#     user_name: str
#     comment: str='Super!'
#     likes: int=0
#
# class Comment(BaseModel):
#     user:User
#     comment: str
#     likes: int


# class Bank(BaseModel):
#     name: str
#     money_amount: int
#     currency: str
#
# bank_client = {'name': 'Pasha', 'money_amount': 23000, 'currency': 'sum'}
# client1 = Bank(**bank_client)
# print(vars(client1))


# class User(BaseModel):
#     name: str
#     followers: int
#     posts: int
# user1 = User(name='dilshodjohnakromov', followers=1427, posts=28)
# print(vars(user1))


class User(BaseModel):
    username: str
    mail: str
    language: str
class Artist(BaseModel):
    artist_name: str  
    artist_followers: int = 0
class Song(BaseModel):
    artist: Artist
    song_name: str
    date_of_publishing: str
class Playlist(BaseModel):
    user: User
    song: List[Song]
    likes: int = 0