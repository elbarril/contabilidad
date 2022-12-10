APP_NAME = "Contabilidad"
DB_NAME = "contabilidad"
DB_PATH = "database/"
INPUTS = {
    "exit": ["x", "q"],
    "newAccount": "na",
    "myName": "mn"
}
ACTIONS = {
    "na": "Creating new account.."
}
HELP = "(na) New account - (x,q) Exit"
INSTALL_SUCCESS = "Application is ready to go."
PRESS_ENTER_TO_CONTINUE = "Press Enter to continue..."
INSERT_NAME = "Insert your name: "
USER_NAME_SUCCESS = "User name was added."
DB_TABLE_CREATED = "table created."
DB_USER_TABLE = "user"
DB_USER_TABLE_ROWS = "(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255))"
DB_ACCOUNT_TABLE = "account"
DB_ACCOUNT_TABLE_ROWS = "(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), amount INTEGER)"