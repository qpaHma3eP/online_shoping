import sqlite3

# Подключение к базе данных
conn = sqlite3.connect('bank.db')
c = conn.cursor()

# Создание таблицы клиентов
c.execute('''CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone TEXT NOT NULL,
            balance REAL DEFAULT 0.0)''')

def register_client(name, phone):
    c.execute("INSERT INTO clients (name, phone) VALUES (?, ?)", (name, phone))
    conn.commit()

# Пример регистрации клиента
register_client('Акромов Дильшод', '998200052080')


def find_client(name, phone):
    c.execute("SELECT * FROM clients WHERE name=? AND phone=?", (name, phone))
    return c.fetchone()

# Пример поиска клиента
client = find_client('Акромов Дильшод', '998200052080')
print(client)


def deposit(phone, amount):
    c.execute("UPDATE clients SET balance = balance + ? WHERE phone=?", (amount, phone))
    conn.commit()

# Пример пополнения баланса
deposit('9980052080', 10000000.0)


def withdraw(phone, amount):
    c.execute("UPDATE clients SET balance = balance - ? WHERE phone=?", (amount, phone))
    conn.commit()

# Пример снятия денег с баланса
withdraw('998200052080', 5000000.0)


def check_balance(phone):
    c.execute("SELECT balance FROM clients WHERE phone=?", (phone,))
    return c.fetchone()[0]

# Пример просмотра баланса
balance = check_balance('998200052080')
print(balance)


def calculate_investment(balance, months, interest_rate=0.25):
    return balance * ((1 + interest_rate) ** (months / 12))

# Пример подсчета вклада
investment_12 = calculate_investment(10000000.0, 12)
investment_24 = calculate_investment(10000000.0, 24)
investment_36 = calculate_investment(10000000.0, 36)
print(investment_12, investment_24, investment_36)


def client_dashboard(phone):
    client = find_client(None, phone)
    if client:
        print(f"Клиент: {client[1]}")
        print(f"Телефон: {client[2]}")
        print(f"Баланс: {client[3]}")
    else:
        print("Клиент не найден")

# Пример личного кабинета клиента
client_dashboard('998200052080')

