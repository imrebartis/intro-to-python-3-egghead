# Create a new virtual environment via the terminal & activate it:
#     virtualenv -p python3 venv # here venv is the virtual environment's name
#     source venv/bin/activate

# Installing packages for requests:
#     pip install requests

# terminal: pip freeze > requirements.txt
# => the requirements.txt created will include
# a list of the packages installed as well as their version numbers
# if u'd uninstalled these packages at some point & u want to reinstall them
# type this into the terminal: pip install -r requirements.txt

# Leaving the virtual environment:
   # terminal: deactivate

# Removing the virtual environment:
    # rm -rf venv

import requests

r = requests.get('http://httpbin.org/get')
print(r.status_code)
print(r.content)