import psycopg2
from settings import (
    DATABASE
)
from werkzeug.security import generate_password_hash


class UserManager:
    """
    A database service for performing crud operations on users on the platform
    """

    def __init__(self, host, database, user, password, port):
        self.conn = psycopg2.connect(
            host=DATABASE['HOST'],
            port=DATABASE['PORT'],
            database=DATABASE['NAME'],
            user=DATABASE['USER'],
            password=DATABASE['PASSWORD']
        )
        self.cursor = self.conn.cursor()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

    def __encrypt_password(self, password):
        encrypted_password = generate_password_hash(password)
        return encrypted_password

    def create_user(self, name, email, password, number):
        query = "INSERT INTO Users (name, email, encrypted_password, number) VALUES (%s, %s, %s, %s)"
        self.cursor.execute(query, (name, email, self.__encrypt_password(password), number))
        self.conn.commit()

    def get_all_users(self):
        query = "SELECT * FROM Users"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def get_a_single_user(self, name):
        query = "SELECT * FROM Users WHERE name=name"
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def update_user_email(self, user_id, new_email):
        query = "UPDATE users SET email = %s WHERE id = %s"
        self.cursor.execute(query, (new_email, user_id))
        self.conn.commit()

    def delete_user(self, user_id):
        query = "DELETE FROM users WHERE id = %s"
        self.cursor.execute(query, (user_id,))
        self.conn.commit()
