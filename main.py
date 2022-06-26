## Instalacja sterowników ODBC for SQL Server

from sys import exc_info
from os import getlogin

# Custom lib
from database import Database
from log import Log
from config import Configuration

if __name__ == "__main__":

    # New instance class
    base = Database()
    log = Log()
    cfg = Configuration()

    current_login = getlogin()
    log.info("### Start Application ###")

    print("#########################")
    print("## Powered by Majster ###")
    print("#########################\n")
    print(f"Witaj {current_login}!\n")
    log.info(f"User {current_login} is running script.")

    try:

        params = cfg.read_config()                              # Read params
        base.connect(params)                                    # Connect to DB

        next = "t"
        while(next == "t"):
            lock_login = input("Podaj login (0 - zakończ program): ")
            if(lock_login == "0"):
                break

            queries = cfg.read_queries(lock_login)                  # Read SQL queries

            print("\n")
            determine = "n"
            while(determine == "n"):
                determine = base.get_user(queries)      # Read user status
                break
            
            if(determine == "t"):
                dump = base.dump_permissions(queries)   # Select user profiles
                # dump to file
                base.deactivate_repository(queries)     # Delete profiles user in repository
                next = base.deactivate_user(queries)    # Disable user and delete user profiles

            print("\n")

    except KeyboardInterrupt:
        pass

    except:
        if(type(exc_info()[1]) != SystemExit):
            print(exc_info())
            log.error(exc_info())

    finally:
        try:
            base.disconnect()
        
        except:
            print(exc_info()[1])
            log.warining(exc_info()[1])
            if(str(exc_info()[1]) == ("'Database' object has no attribute 'cursor'")):      # If connect isn't open, you cannot close this connection then
                log.warining("Cannot close connection, because it didn't was opened.")
        
        finally:
            
            log.info("### End Application ###\n")

            print("\n#########################")
            print("## Powered by Majster ###")
            print("#########################")

            # Delete instance class
            del log
            del base
            del cfg