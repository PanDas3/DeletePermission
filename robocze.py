def print_status(row):
    print("ID:", row[0])
    print("Login:", row[1])
    print("Imię:", row[2])
    print("Nazwisko:", row[3])
    print("PESEL:", row[4])
    print("Aktywny:", row[5], "\n")

db = ["Use BPO", "Use BPOBO"]
found = None
env = "QA"
instance = None
# row = ['1','2','3','4','5','6']

rows = [['1','2','3','4','5','6'], None]
for row in rows:
    for database in db:
    
        if(database == "Use BPO"):
            instance = "Sprzedaz"

        elif(database == "Use BPOBO"):
            instance = "BackOffice"

        print(database)


        # self.log.info(f"Looking for {login} on the base - SP")
        # row = self.cursor.fetchone()
        
        if(row == None):
            print(f"Nie istnieje użytkownik dla instancji Ferryt {instance}")
            found = "n"
        
        else:
            print(f"------------ {instance} - {env} ------------")
            print_status(row)
            found = "t"
        break
            

if(found != "n"):
    found = input("Czy dane się zgadzają? t/n: ").lower()

if((found == "t") or (found == "n")):
    pass

else:
    print("Błędna odpowiedź - zaznaczam Nie...")
    found = "n"