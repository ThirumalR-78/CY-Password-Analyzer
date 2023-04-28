# Password Analyser
Check to see if a password is safe using many different methods, including HavIBeenPwned and comparing it to a list of over 100000+ common passwords.
No sensitive information is shared at all. Only the first five characters of the SHA-1 hash is uploaded to HaveIBeenPwned, all others processes are competed locally on the computer.

# Requirements
pip install requests 
pip install termcolor
pip instll colorama
pip install hashlib
pip install argparse

# Usage
Check out to the project path and in the command prompt follow the steps below.
`cd password-analyser`

To run :
`python password-analyser.py PASSSWORD`   
///Replace PASSWORD with your choice of your password  
 Or, to read a password from a file:  
`python password-analyser.py -f FILE`


To pass the input from UI run the following commands
python SubProcess.py
then it will launch the application in the http://127.0.0.1:5000
provide the input in the UI then it will display the password strength.
