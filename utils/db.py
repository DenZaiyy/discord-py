import os
import mysql.connector

class DB:
    def __init__(self, db_name: str = os.getenv('MYSQL_DATABASE'), user: str = os.getenv('MYSQL_USER'), password: str= os.getenv('MYSQL_PASSWORD'), host: str = os.getenv('MYSQL_HOST')):
        self.con = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=db_name
        )
        self.cur = self.con.cursor()
        pass

    def query(self, q: str, params: tuple = None, fetchone: bool = False, fetchall: bool = False) -> None:
        r = self.cur.execute(q, params)
        if fetchone:
            return self.cur.fetchone()
        elif fetchall:
            return self.cur.fetchall()
        return r

    def commit(self) -> None:
        return self.con.commit()

    def lastrowid(self) -> None:
        return self.cur.lastrowid