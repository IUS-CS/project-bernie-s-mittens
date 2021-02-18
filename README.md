# Pro-Vax

Pro-Vax is a web app that notifies users of their eligibility for a Covid-19 vaccination and shows the closest available 
vaccination center. Future features may include symptom trackers and notifications regarding mutant strains and virus surges 
in the user's area.


## Build Info
Install the latest version of [Python](https://www.python.org/downloads/) This project uses the SQLite database that is 
included in Python installs. Set up a virtual environment, [venv](https://docs.python.org/3/tutorial/venv.html) to avoid 
installing packages system-wide. In order to install Django, you will need to have [pip](https://pip.pypa.io/en/latest/installing/#installing-with-get-pip-py) 
installed. Finally, you can install [Django](https://www.djangoproject.com/) using this command: `$ python -m pip install Django`

## Required Operating Systems
- Windows 8 or higher
- macOS X 10.9 or higher


## Built With
- Python
- Django
- PyCharm
- SQLite

## Initial Setup
- Clone repository
- Open terminal to root repository directory
- `python --version` to confirm Python v3.8
- `python -m venv django_env` to create virtual environment directory named django_env
- `django_env\Scripts\activate` to start using virtual environment
- `pip install requirements.txt` to correctly initialize virtual environment and django
- Outside of the terminal, hold down Win + Pause to enter system properties and navigate to Advanced System Settings then Environment Variables. Click New... and label the variable DJANGO_SECRET_KEY and set it to the given key.
- Return to your terminal and enter `cd src` to enter src directory
- `python manage.py runserver` to activate server
- visit http://127.0.0.1:8000/ in a web-browser that does not force HTTPS connection to check site status
- `Ctrl + C` to stop the server when finished
- `deactivate` to leave virtual environment


## Authors
Nick Jones  
Jon Clements  
Amanda Schneider


## License
[MIT](https://choosealicense.com/licenses/mit/)
