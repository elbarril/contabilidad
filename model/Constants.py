APP_NAME = "Contabilidad"
DB_NAME = "contabilidad"
DB_PATH = "database/"

EXIT_INPUTS = ["x", "q", "exit", "quit"]
HELP_INPUTS = ["h", "help"]
ACTIONS_INPUTS = ["la", "ls", "na", "ns"]
CLEAR_INPUTS = ["c", "clear"]

INSTALL_SUCCESS = "Application is ready to go."
PRESS_ENTER_TO_CONTINUE = "Press Enter to continue..."
INSERT_NAME = "Insert your name: "
USER_NAME_SUCCESS = "User name was added."
DB_TABLE_CREATED = "table created."

STRINGS = {
    "space": " ",
    "comma": ",",
    "equals": "=",
    "single_quotation": "'",
    "open_parenthesis": "(",
    "close_parenthesis": ")",
    "hyphen": '-'
}

DB = {
    
    "path": "database/",
    "name": "contabilidad",
    "tables": {
        "user": {
            "columns": [
                {
                    "name": "id",
                    "type": "INTEGER",
                    "primarykey": True,
                    "autoincrement": True
                },
                {
                    "name": "name",
                    "type": "VARCHAR",
                    "limit": 255
                },
            ]
        },
        "account": {
            "columns": [
                {
                    "name": "id",
                    "type": "INTEGER",
                    "primarykey": True,
                    "autoincrement": True
                },
                {
                    "name": "name",
                    "type": "VARCHAR",
                    "limit": 255
                },
                {
                    "name": "amount",
                    "type": "INTEGER"
                }
            ]
        },
        "spends": {
            "columns": [
                {
                    "name": "id",
                    "type": "INTEGER",
                    "primarykey": True,
                    "autoincrement": True
                },
                {
                    "name": "accountId",
                    "type": "INTEGER"
                },
                {
                    "name": "detail",
                    "type": "VARCHAR",
                    "limit": 255
                },
                {
                    "name": "amount",
                    "type": "INTEGER"
                }
            ]
        }
    }    
}

ACTIONS = {
    "na": {
        "query": "INSERT",
        "data": {
            "table": "account",
            "columns": ["name", "amount"]
        }
    },
    "ns": {
        "query": "INSERT",
        "data": {
            "table": "spends",
            "columns": ["accountId", "detail", "amount"]
        }
    },
    "la": {
        "query": "SELECT",
        "data": {
            "table": "account",
            "columns": ["*"]
        }
    },
    "ls": {
        "query": "SELECT",
        "data": {
            "table": "spends",
            "columns": ["*"]
        }
    }
}


HELP = """(na) New account - (x,q) Exit - (ns) New spend - (la) List accounts
(ls) List spends"""