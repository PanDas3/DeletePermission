from os import system, mkdir, path
from sys import exc_info
from time import sleep, strftime
from datetime import datetime

# import pyodbc
from pyodbc import connect
from pyodbc import Error

# import pandas
from pandas import read_sql

# Custom lib
from log import Log

class Database():
    def __init__(self) -> None:
        self.log = Log()

    def connect(self, params):
        self.server = params["server"]
        self.env = params["env"]

        driver = params["driver"]
        user = params["user"]
        passwd = params["passwd"]
        
        try:
            self.con = connect(f"DRIVER={driver}; SERVER={self.server}; UID={user}; PWD={passwd}")
            
            self.log.info(f"Connected to {self.server}")
            print(f"Connected to {self.server}")
            print(f"--------- <system> {self.env} ---------")
            self.log.info(f"########## <system> - {self.env} ##########")

            self.cursor = self.con.cursor()

        except Error as ex:
            self.log.error(ex.args[1])
            print(ex.args[1])
            print("\n")
        
        finally:
            exit()

    def get_user(self, queries):
        self.db = queries["database"]
        looking_query_user = queries["sql_looking_user"]
        login = queries["block_login"]
        found = "n"

        for database in self.db:
            instance = self.change_database(database)
            try:
                if(instance == "Repozytorium"):
                    continue
                self.cursor.execute(database)
            except:
                print(f"Nie znaleziono bazy danych {instance}")
                self.log.warining(exc_info()[1])
                continue

            self.cursor.execute(looking_query_user)
            self.log.info(f"Looking for user: {login} on the base - {instance}")
            row = self.cursor.fetchone()

            if(row == None):
                print(f"Nie istnieje użytkownik dla instancji <system> {instance}")
                self.log.info(f"Not found user for <system> {instance} - {self.env}")
            
            else:
                print(f"------------ {instance} - {self.env} ------------")
                self.print_status(row)
                found = "t"
                
            if(found != "n"):
                found = input("Czy dane się zgadzają? t/n: ").lower()

            if((found == "t") or (found == "n")):
                print("\n")

            else:
                print("Błędna odpowiedź - zaznaczam Nie...")
                found = "n"

            return found

    def dump_permissions(self, queries):
        sql_dump_system = queries["sql_dump_system_profiles"]
        sql_dump_repo = queries["sql_dump_repo_profiles"]
        db = queries["database"]
        login = queries["block_login"]

        currentdate = strftime("%Y%m%d")

        for database in db:
            instance = self.change_database(database)

            try:
                self.cursor.execute(database)
            except:
                continue

            if(instance == "Repozytorium"):
                sql_dump_system = sql_dump_repo
            
            self.log.info(f"Read system permission - <system> {instance} for user: {login}")
            print(f"Czytanie uprawnień - <system> {instance}: {login}...")
            df = read_sql(sql_dump_system, self.con)

            self.log.info(f"Dump permissions to file - <system> {instance} for user: {login}")
            print(f"Wykonywanie dump'a uprawnień do pliku <system> - {instance}: {login}...\n")

            if(path.isdir("Uprawnienia") == False):
                mkdir("Uprawnienia")

            with open(f"Uprawnienia\\uprawnienia_{login}_{currentdate}.txt", 'a') as file:
                file.write(f"------------------ <system> {instance} ------------------\n")
                file.write(f" ----- WYGENEROWANO: {datetime.now()} -----\n\n")
                df_text = df.to_string(header=True, index=False)
                file.write(df_text)
                if(df.empty == True):
                    file.write("\nNieznaleziono przypisanych uprawnień...")
                file.write("\n\n")
                file.close()

    def deactivate_user(self, queries):
        sql_disabled = queries["sql_disabled_account"]
        login = queries["block_login"]
        db = queries["database"]

        for database in db:
            instance = self.change_database(database)
            if(instance == "Repozytorium"):
                continue
            try:
                self.cursor.execute(database)
            except:
                print(f"Nie znaleziono bazy danych {instance}\n")
                self.log.warining(exc_info()[1])
                continue

            self.cursor.execute(sql_disabled)
            self.con.commit()
            self.log.info(f"Disabled account - <system> {instance}: {login}")
            print(f"Wyłączenie konta - <system> {instance}: {login}...\n")

    def delete_permission(self, queries):
        sql_del_profiles = queries["sql_delete_profiles"]
        sql_del_repo = queries["sql_delete_profiles_repo"]
        login = queries["block_login"]
        db = queries["database"]

        for database in db:
            instance = self.change_database(database)
            try:
                self.cursor.execute(database)
            except:
                print(f"Nie znaleziono bazy danych {instance}\n")
                self.log.warining(exc_info()[1])
                continue

            if(instance == "Repozytorium"):
                sql_del_profiles = sql_del_repo

            self.cursor.execute(sql_del_profiles)
            self.con.commit
            self.log.info(f"Delete profiles - <system> {instance}: {login}")
            print(f"Usuwanie ról - <system> {instance}: {login}...")

        next = input("Następny użytkownik? t/n: ").lower()
        if((next == "t") or (next == "n")):
            pass

        else:
            print("Błędna odpowiedź - zaznaczam Nie...")
            next = "n"

        system("CLS")
        return next

    def print_status(self, row):
        print("ID:", row[0])
        print("Login:", row[1])
        print("Imię:", row[2])
        print("Nazwisko:", row[3])
        print("PESEL:", row[4])
        print("Aktywny:", row[5], "\n")

    def change_database(self, database):
        if(database == "Use <base>"):
            instance = "Sprzedaz"

        elif(database == "Use <base instance2>"):
            instance = "BackOffice"

        elif(database == "Use <base repository>"):
            instance = "Repozytorium"

        return instance

    def disconnect(self):
        self.cursor.close()
        self.con.close()
        print("Zamykam połączenie z bazą...\n")
        self.log.info(f"Close connection with {self.server}")
        sleep(1.5)

    def __del__(self):
        del self.log