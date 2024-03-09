from flask import Flask, render_template, request
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        
        test_string = request.form.get("test_string")
        regex_pattern = request.form.get("regex_pattern")
    
        matched_strings = perform_regex_matching(test_string, regex_pattern)
        
        return render_template("index.html", test_string=test_string, regex_pattern=regex_pattern, matched_strings=matched_strings)

    else:
        return render_template("index.html", test_string="", regex_pattern="", matched_strings=None)

@app.route("/validate-email", methods=["POST"])
def validate_email():
    if request.method == "POST":
        email = request.form.get("email")
        
        is_valid = validate_email_address(email)
        
        return render_template("email_validation.html", email=email, is_valid=is_valid)

@app.route("/results", methods=["POST"])
def results():
    if request.method == "POST":
        test_string = request.form.get("test_string")
        regex_pattern = request.form.get("regex_pattern")
        
        matched_strings = perform_regex_matching(test_string, regex_pattern)

        if not matched_strings:
            return render_template("resuts.html",test_string=test_string,regex_pattern=regex_pattern,matched_strings=None,no_matches=True)
        
        
        return render_template("results.html", test_string=test_string, regex_pattern=regex_pattern, matched_strings=matched_strings,no_matches=False)

def perform_regex_matching(test_string, regex_pattern):
    try:
        matches = re.findall(regex_pattern, test_string)
        return matches
    except re.error:
        return ["Invalid Regex Pattern"]

def validate_email_address(email):
    try:
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        is_valid = re.match(email_pattern, email) is not None
        return is_valid
    except re.error:
        return False

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
