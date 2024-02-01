import json
from mailer import MailCreds, MailRep, MailTaskComp
from flask import Flask, request, jsonify
import pandas as pd
from decryption import Decrypt
from report import Gen_rep

app = Flask(__name__)


@app.route('/')
def home():
    return "API Server Running"


@app.route('/SignedUp', methods=['GET', 'POST'])
def MailCredentials():
    # Ensure the request is a POST request
    if request.method == 'POST':
        # Get the JSON data from the request
        data = request.get_json()

        # Extract data from JSON
        employees = data.get("employees", [])

        # Extract information for each employee
        names = [employee.get("Name", "") for employee in employees]
        emails = [employee.get("Email", "") for employee in employees]
        encrypted_passwords = [employee.get("Encrypted_Password", "") for employee in employees]

        # Decrypt passwords using the Decrypt function
        decrypted_passwords = [Decrypt(password) for password in encrypted_passwords]

        # Create a DataFrame
        df = pd.DataFrame({
            "Name": names,
            "Email": emails,
            "Password": decrypted_passwords
        })

        results = []

        # Iterate over the rows of the DataFrame
        for index, row in df.iterrows():
            name = row["Name"]
            email = row["Email"]
            password = row["Password"]

            # Call Mail_Creds function for each employee
            result = MailCreds(name, email, password)

            # Store the result in the array
            results.append(result)

        # Count occurrences of 1 and -1 in the results array
        success_count = results.count(1)
        failure_count = results.count(-1)

        # Determine the final message based on majority results
        if success_count >= failure_count:
            return {'status': True}
        else:
            return {'status': False}


@app.route('/ProjectReport', methods=['GET', 'POST'])
def MailReport():
    # Ensure the request is a POST request
    if request.method == 'POST':
        # Get the JSON data from the request
        data = request.get_json()

        hr_mail = data.get("hr_mail", "")
        project_name = data.get("project_name")
        project_details = data.get("project_details", "")
        resources_util = data.get("resources_util", "")
        budget = data.get("budget")
        days = data.get("days")
        project_progress = data.get("project_progress", "")

        report_file = Gen_rep(project_name, project_details, project_progress, resources_util, budget, days)

        status = MailRep(project_name, hr_mail, report_file)

        # Determine the final message based on majority results
        if status == 1:
            return {'status': True}
        else:
            return {'status': False}


@app.route('/TaskCompleted', methods=['GET', 'POST'])
def MailCompletion():
    data = request.get_json()

    # Extract values for each variable
    reporting_manager_name = data.get("reporting_manager_name", "")
    reporting_manager_email = data.get("reporting_manager_email", "")
    employee_name = data.get("employee_name", "")
    employee_id = data.get("employee_id", "")
    task_details = data.get("task_details", "")
    skills = data.get("skills", "")
    projects = data.get("projects", "")

    status = MailTaskComp(reporting_manager_name, employee_name, employee_id, reporting_manager_email, task_details,
                          skills, projects)

    if status == 1:
        return {'status': True}
    else:
        return {'status': False}


if __name__ == '__main__':
    app.run(debug=True)
