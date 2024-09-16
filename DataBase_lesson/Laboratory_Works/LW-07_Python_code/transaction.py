import mysql.connector
from datetime import datetime

# Устанавливаем соединение с базой данных
connection = mysql.connector.connect(
    host='127.0.0.1',
    database='transaction',
    user='root',
    password='1234'
)

def send_money(money, sender, recipient):
    cursor = connection.cursor(dictionary=True)
    try:
        # Проверка баланса отправителя
        cursor.execute("SELECT balance FROM accounts WHERE account_id = %s", (sender,))
        sender_balance = cursor.fetchone()['balance']

        if sender_balance < money:
            print("Недостаточно средств у отправителя!")
            return

        # Выполнение транзакции
        sql = "UPDATE `accounts` SET balance = balance + %s WHERE account_id = %s"
        cursor.execute(sql, (money, recipient))
        sql = "UPDATE `accounts` SET balance = balance - %s WHERE account_id = %s"
        cursor.execute(sql, (money, sender))

        # Регистрация операции в таблице transactions
        transaction_sql = """
            INSERT INTO transactions (from_account_id, to_account_id, amount, transaction_date)
            VALUES (%s, %s, %s, %s)
        """
        transaction_data = (sender, recipient, money, datetime.now())
        cursor.execute(transaction_sql, transaction_data)

        connection.commit()
        print("Перевод завершен успешно!")

    except mysql.connector.Error as err:
        print(f"Ошибка: {err}, перевод отменен!")
        connection.rollback()

    finally:
        cursor.close()


def check_money():
    cursor = connection.cursor(dictionary=True)
    try:
        sql = "SELECT * FROM accounts"
        cursor.execute(sql)
        data = cursor.fetchall()
        for row in data:
            print(row)
    finally:
        cursor.close()


try:
    send_money(1500, 1, 2)
    check_money()
finally:
    connection.close()