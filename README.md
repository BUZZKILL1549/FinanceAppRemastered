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
Step 1:
Move to the root folder of your project and open cmd (commandprompt) and run the following:
~~~
.\automate.bat
~~~
This will install all needed dependencies.

Step 2:
Move to the root folder and run:
~~~
.\runPy.py
~~~
You may create a shortcut of the same or keep running it through cmd if you so wish.

That's really about it. I've tried to simplify this as much as I can.