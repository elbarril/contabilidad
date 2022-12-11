APP_NAME = "Contabilidad"
DB_NAME = "contabilidad"
DB_PATH = "database/"
EXIT_INPUTS = ["x", "q"]
INSTALL_SUCCESS = "Application is ready to go."
PRESS_ENTER_TO_CONTINUE = "Press Enter to continue..."
INSERT_NAME = "Insert your name: "
USER_NAME_SUCCESS = "User name was added."
DB_TABLE_CREATED = "table created."
DB_USER_TABLE = "user"
DB_USER_TABLE_COLUMNS = "(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255))"
DB_ACCOUNT_TABLE = "account"
DB_ACCOUNT_TABLE_COLUMNS = "(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), amount INTEGER)"
DB_SPENDS_TABLE = "spends"
DB_SPENDS_TABLE_COLUMNS = "(id INTEGER PRIMARY KEY AUTOINCREMENT,accountId INTEGER, detail VARCHAR(255), amount INTEGER)"


ACTIONS = {
    "na": {
        "query": "insert",
        "data": {
            "table": DB_ACCOUNT_TABLE,
            "columns": ["name", "amount"]
        }
    },
    "ns": {
        "query": "insert",
        "data": {
            "table": DB_SPENDS_TABLE,
            "columns": ["accountId", "detail", "amount"]
        }
    },
    "la": {
        "query": "select",
        "data": {
            "table": DB_ACCOUNT_TABLE,
            "columns": ["id", "name", "amount"]
        }
    },
    "ls": {
        "query": "select",
        "data": {
            "table": DB_SPENDS_TABLE,
            "columns": ["id","accountId", "detail", "amount"]
        }
    },
    "h": """(na) New account - (x,q) Exit - (ns) New spend - (la) List accounts
(ls) List spends"""
}


QUERIES = {
    "insert": "INSERT INTO $table$ ($columns$) VALUES ($values$)",
    "select": "SELECT $columns$ FROM $table$"
}

MODIFIERS = {
    "table": "$table$",
    "columns": "$columns$",
    "values": "$values$"
}