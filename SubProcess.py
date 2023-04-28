import subprocess
from src import main

from flask import Flask, render_template, request

app = Flask(__name__)
data = {'output': ''}

@app.route("/")
def home():
    
    return render_template("passwordInput.html",data=data)

@app.route("/run_script", methods=["POST"])
def run_script():
    input_text = request.form["input_text"]
    print("\nPassword: ", input_text)
    # result = subprocess.run(["python", "password-analyser.py",input_text])
    print('****************************************')
    # print(result)
    output= main.Function1(input_text)
    print(':::::::::::::::::::::::::::::::::::::'+output)
    data['output'] = output
    return render_template("passwordInput.html",data=data)
    # return "Script has been run!::: "+input_text

if __name__ == "__main__":
    app.run()
