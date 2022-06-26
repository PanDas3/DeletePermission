# Custom lib
from log import Log

class Configuration():
    def __init__(self) -> None:
        self.log = Log()

    def read_config(self):
        env = "DEV"
        driver = "{ODBC Driver 17 for SQL Server}"
        server = "SQL"
        user = "user"
        passwd = "123"

        params = {
            "env":env,
            "driver":driver,
            "server":server,
            "user":user,
            "passwd":passwd
        }

        return params

    def read_queries(self, login):
        database = ["Use <base>", "Use <base_instance2>"]
        database_rpz = "Use <base repository>"

        sql_looking_user = f"""SELECT 
        [ID],
        [Login],
        [FirstName],
        [LastName],
        [PESEL],
        [Status] 
        FROM [dbo].[User] with (nolock)
        WHERE [Login] = '{login}'"""

        sql_dump_system_profiles = f"""SELECT
        [User].[ID],
        [User].[Name],
        [User].[FirstName],
        [User].[Login],
        Case [User].[Status] WHEN 1 'Aktywny' ELSE 'Nieaktywny' END as 'Status',
        [OrgUnit].[Symbol],
        [OrgUnit].[Name],
        [Profile].[Symbol],
        [Profile].[Name],

        FROM [dbo].[ProfileUser] with (nolock)
        INNER JOIN [dbo].[User] ON [ProfileUser].[ID] = [User].[ID]
        INNER JOIN [dbo].[Profile] ON [ProfileUser].[ProfileID] = [Profile].[ID]
        INNER JOIN [dbo].[OrgUnit] ON [Profile].[OrgUnitID]

        WHERE [Login] = '{login}'"""

        sql_dump_repo_profiles = f"""SELECT 
        ru.[UserID],
        u.[Login],
        u.[Name],
        r.[Symbol],
        r.[Name]
        FROM [dbo].[RoleUser] with (nolock) as ru
        INNER JOIN [dbo].[Role] as r on ru.[RoleID] = r.[ID]
        INNER JOIN [dbo].[User] as u on ru.[UserID] = u.[ID]
        WHERE [UserID] = (Select [ID] FROM [dbo].[User] WHERE [Login] = '{login}')"""

        sql_disabled_account = f"""UPDATE [dbo].[User] 
        SET Status = 0 
        WHERE [Login] = '{login}'"""

        sql_delete_profiles = f"""DELETE FROM [dbo].[ProfileUser] 
        WHERE [ID] = (SELECT [ID] FROM [dbo].[User] WHERE [Login] = '{login}')"""

        sql_delete_profiles_repo = f"""DELETE FROM [dbo].[RoleUser]
        WHERE [ID] = (SELECT [ID] FROM [dbo].[User] with (nolock) WHERE [Login] = '{login}')"""

        queries = {
            "database":database,
            "database_rpz":database_rpz,
            "sql_looking_user":sql_looking_user,
            "sql_dump_system_profiles":sql_dump_system_profiles,
            "sql_dump_repo_profiles":sql_dump_repo_profiles,
            "sql_delte_profiles_repo":sql_delete_profiles_repo,
            "sql_disabled_account":sql_disabled_account,
            "sql_delete_profiles":sql_delete_profiles,
            "blokc_login":login
        }

        return queries

    def __del__(self):
        del self.log