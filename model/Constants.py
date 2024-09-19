APP_NAME = "Contabilidad"
DB_NAME = "contabilidad"
DB_PATH = "database/"

import datetime
YEAR = str(datetime.datetime.now().year)
DEFAULT_USER = "guest"

SHORTCUT_ACTIONS = [
    {"string": "na","action": "add_record_to_account"},
    {"string": "ns","action": "add_record_to_spends"},
    {"string": "la","action": "add_record_to_account"},
    {"string": "ls","action": "add_record_to_spends"}
]
KEY_SHORTCUT_CLEAR = ["c", "clear"]
KEY_SHORTCUT_EXIT = ["x", "q", "exit", "quit"]
KEY_SHORTCUT_HELP = [
    "h", "New account",
     "help"
]
HELP_TEXT = """(na)  - (x,q)  - (ns) New spend - (la) List accounts
(ls) List spends"""

HELP_ENABLED_DEFAULT = True
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
DB_TABLES = {
    "users": {
        "init_columns": [
            "id INTEGER PRIMARY KEY AUTOINCREMENT",
            "name VARCHAR(255)"
        ],
        "add_columns": ()
    }
}
DB = {
    "path": "database/",
    "name": "contabilidad",
    "methods": {
        "create_table": "CREATE TABLE :table: (:columns:)",
        "list_records": "SELECT :columns: FROM :table:",
        "list_records_filter_by": "SELECT :columns: FROM :table: WHERE :filter_column:=:filter_value:",
        "add_record_to_account": "INSERT INTO :table: (:columns:) VALUES (:values:)",
        "update_record": "",
        "delete_record": ""
    },
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