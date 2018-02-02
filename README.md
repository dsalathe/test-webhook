# DD2480 Assignment 2: Continuous Integration

## Set-up
* Install python 3.6, pip and sqlite3
* Clone repo
* ```sudo pip install -r requirements.txt``` to download dependencies
* `pytest` to run unit tests
* ```cd src && python -m app run``` to run server

## CI features

### Compilation

The CI server uses the [`py_compile` module](https://docs.python.org/3/library/py_compile.html) to compile the Python source code into byte-code, checking for syntax errors. Compilation is unit tested using two Python files, one containing a syntax error and one without any syntax errors. The CI server expects all Python source code to be in a directory `src` in the repo's root. Any files in `src` (or any subdirectory of `src`, recursively) will be compiled and syntax errors reported. If no syntax errors were found the server will print out `Compilation succeeded` on the console, else `Compilation failed` will be printed.

### Database setup
* When you first run the application, it will create a database called `database.db`

### Webhook setup
To be able to receive webhooks from github you need to be able to receive requests to your local server. For this purpose we use [Ngrok](https://ngrok.com/).
Download Ngrok and run `./ngrok http 8014` to open port 8014. Now paste the new url
`<generated url>/pull-request` in the settings for webhooks in the github repository.
hey
