# FinanceAppRemastered
This is the remastered version of my FinanceApp project from long ago.

# Project Components
Initially, this project used Python (v3.12) and MySQL (v8.0) but I wanted to package this app into an executable file and realized that I would run into issues there. So, I migrated from MySQL to SQlite which is embedded in Python. It was a surprisingly seamless transition too.

So the project only really uses:
- Windows 10 or greater
- Python (v3.12)

# Project Requirements
- Windows 10 or greater
- Python (3.x) or greater

This may be Installed by visiting https://www.python.org/ and downloading the latest version of Python from there.

Please DO NOT try installing dependencies without installing Python. It will not work. This whole project relies on Python.

## Installing dependencies (after installing python)
Run the following commands in Powershell (v5.1 or greater):
~~~
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\automate.ps1
~~~

That's really about it. I've tried to simplify this as much as I can.