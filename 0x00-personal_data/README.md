## Personal data
### Learning Objectives:
* Examples of Personally Identifiable Information (PII)
* How to implement a log filter that will obfuscate PII fields
* How to encrypt a password and check the validity of an input password
* How to authenticate to a database using environment variables

### Tasks:
### [0. Regex-ing](./filtered_logger.py)<br>
Write a function called `filter_datum` that returns the log message obfuscated:

* Arguments:
  * `fields`: a list of strings representing all fields to obfuscate
  * `redaction`: a string representing by what the field will be obfuscated
  * `message`: a string representing the log line
  * `separator`: a string representing by which character is separating all fields in the log line (`message`)
* The function should use a regex to replace occurrences of certain field values.
* `filter_datum` should be less than 5 lines long and use `re.sub` to perform the substitution with a single regex.<br>

```
simam@DESKTOP-5QTVNRV:~/alx-backend-user-data/0x00-personal_data$ cat main.py 
#!/usr/bin/env python3
"""
Main file
"""

filter_datum = __import__('filtered_logger').filter_datum

fields = ["password", "date_of_birth"]
messages = ["name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;", "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"]

for message in messages:
    print(filter_datum(fields, 'xxx', message, ';'))
simam@DESKTOP-5QTVNRV:~/alx-backend-user-data/0x00-personal_data$ ./main.py 
name=egg;email=eggmin@eggsample.com;password=xxx;date_of_birth=xxx;
name=bob;email=bob@dylan.com;password=xxx;date_of_birth=xxx;
simam@DESKTOP-5QTVNRV:~/alx-backend-user-data/0x00-personal_data$
```

### [1. Log formatter](./filtered_logger.py)<br>
Copy the following code into `filtered_logger.py`.<br>
```ps1
import logging


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
    """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        super(RedactingFormatter, self).__init__(self.FORMAT)

    def format(self, record: logging.LogRecord) -> str:
        NotImplementedError
```

Update the class to accept a list of strings `fields` constructor argument.
Implement the `format` method to filter values in incoming log records using `filter_datum`. Values for fields in `fields` should be filtered.
DO NOT extrapolate `FORMAT` manually. The `format` method should be less than 5 lines long.<br>

### [2. Create logger](./filtered_logger.py)<br>
Use [user_data.csv](./user_data.csv) for this task

Implement a `get_logger` function that takes no arguments and returns a `logging.Logger` object.

The logger should be named `"user_data"` and only log up to `logging.INFO` level. It should not propagate messages to other loggers. It should have a `StreamHandler` with `RedactingFormatter` as formatter.

Create a tuple `PII_FIELDS` constant at the root of the module containing the fields from `user_data.csv` that are considered PII. `PII_FIELDS` can contain only 5 fields - choose the right list of fields that can are considered as “important” PIIs or information that you <b>must hide</b> in your logs. Use it to parameterize the formatter.<br>

### [3. Connect to secure database](./filtered_logger.py)<br>
Database credentials should NEVER be stored in code or checked into version control. One secure option is to store them as environment variable on the application server.

In this task, you will connect to a secure `holberton` database to read a `users` table. The database is protected by a username and password that are set as environment variables on the server named `PERSONAL_DATA_DB_USERNAME` (set the default as “root”), `PERSONAL_DATA_DB_PASSWORD` (set the default as an empty string) and `PERSONAL_DATA_DB_HOST` (set the default as “localhost”).

The database name is stored in `PERSONAL_DATA_DB_NAME`.

Implement a `get_db` function that returns a connector to the database (`mysql.connector.connection.MySQLConnection object`).

Use the `os` module to obtain credentials from the environment
Use the module `mysql-connector-python` to connect to the MySQL database (`pip3 install mysql-connector-python`)<br>

### [4. Read and filter data](./filtered_logger.py)<br>
Implement a `main` function that takes no arguments and returns nothing.

The function will obtain a database connection using `get_db` and retrieve all rows in the `users` table and display each row under a filtered format like this:
```
[HOLBERTON] user_data INFO 2019-11-19 18:37:59,596: name=***; email=***; phone=***; ssn=***; password=***; ip=e848:e856:4e0b:a056:54ad:1e98:8110:ce1b; last_login=2019-11-14T06:16:24; user_agent=Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; KTXN);
```

Filtered fields:

name
email
phone
ssn
password
Only your `main` function should run when the module is executed.<br>

### [5. Encrypting passwords](./encrypt_password.py)<br>
User passwords should NEVER be stored in plain text in a database.

Implement a `hash_password` function that expects one string argument name `password` and returns a salted, hashed password, which is a byte string.

Use the `bcrypt` package to perform the hashing (with `hashpw`).<br>

### [6. Check valid password](./encrypt_password.py)<br>
Implement an `is_valid` function that expects 2 arguments and returns a boolean.

Arguments:

* `hashed_password`: `bytes` type
* `password`: string type
Use `bcrypt` to validate that the provided password matches the hashed password.<br>