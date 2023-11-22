# NatterNet
### Requirements
- Python 3.10 version
- PIP libraries: see requirements.txt file
### How to
#### Make a Python virtual environment with 3.10 version (or higher)
(check Default Python version: python --version. To use a specific version  - python3.10 -m venv artifexgen )
- python -m venv natternet
#### Activate your virtual environment
- Windows:
- .\natternet\Scripts\activate
- Linux/Mac
- source natternet/bin/activate
(Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted)
#### Install the PIP libraries: 
- pip install -r requirements.txt
#### Run the project: 
- flask run --host=0.0.0.0 --debugger
#### Access the Web cliente application on you browser: 
- http://localhost:5000
- The Web client applictation is on http://localhost:5000/
- The API endpoint is on http://localhost:5000/api