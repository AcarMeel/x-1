# First Time
python3 -m venv venv
source venv/bin/activate
pip3 install django
update .zshrc with the PATH
source .zshrc

# Create project
create a project: django-admin startproject name_here .

# Run app
python3 manage.py runserver

# Add apps
django-admin startapp home


# When app is setup
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# if requirements.txt does not exist
pip freeze > requirements.txt
