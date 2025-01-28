from pydantic import BaseModel, EmailStr, Field
from typing import List, Optional
from datetime import date

# Модель для пользователя
class User(BaseModel):
    name: str
    mail: EmailStr
    address: str

# Модель для банков
class Banks(BaseModel):
    name: str
    rating: float
    opened: date

# Модель для карт
class Cards(BaseModel):
    cardholder: User
    which_bank: Banks
    opened: date

# Модель для баланса
class Balance(BaseModel):
    card: Cards
    amount: float
    currency: str

# Пример использования
user = User(name="Dilshodjohn", mail="dilshodjohn@gmail.com", address="Murgob 1 St, 8A home")
bank = Banks(name="National Bank", rating=4.5, opened=date(2021, 12, 25))
card = Cards(cardholder=user, which_bank=bank, opened=date(2024, 8, 13 ))
balance = Balance(card=card, amount=10000000.0, currency="UZS")

print(balance)
