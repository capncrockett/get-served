# get-served
Python back-end server action. Learning how to hook it up.

### FOR SERVER

#### Check Python installation
`$ python3 --version`  

##### If not installed
`$ sudo apt-get update`  
`$ sudo apt-get install python3.6`  

##### If problems
https://docs.python-guide.org/starting/install3/linux/


#### Ensure pip is installed  
`$ command -v pip`  
or  
`$ command -v pip3`  

##### If problems
https://pip.pypa.io/en/stable/installation/  


#### Install Pipenv
`$ pip install --user pipenv`  

##### If problems  
https://python.land/virtual-environments/pipenv  


#### Install dependencies  
`$ pipenv install requests`  


#### Run server.py in a virtual environment
`$ pipenv run python3 server.py`  
