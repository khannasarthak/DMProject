We have used FLASK framework for our application. 
For running the application you need to perform following steps-

1. Install Python 2.7 on your system-
   https://www.python.org/downloads/

2. Install Microsoft Visual C++ compiler package for python version-
   https://www.microsoft.com/en-us/download/details.aspx?id=44266

3. Install MySQL Database in your system-
   https://www.sitepoint.com/how-to-install-mysql/

4. Run the "DDLqueries" script to create database.

5. Install flask in your system-
   $ pip install Flask 

6. Open the "app.py" python file and make following changes-
   app.config['MYSQL_USER'] = '<your mySQL user name>'
   app.config['MYSQL_PASSWORD'] = '<your mySQL password>'
   app.config['PORT'] = <your port number for mySQL database>

7. Locate to the "Flask App" folder (in our submission) and run following commands on command promt-
   >set FLASK_APP=app.py

   >python -m flask run

8. Now you can easily interact with the application. 