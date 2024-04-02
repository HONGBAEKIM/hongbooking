from flask import Flask, render_template, request, url_for, redirect
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/handle_form', methods=['POST'])
def handle_form():
    user_id_from_app = request.form.get('user_id')
    password_from_app = request.form.get('password')
    project_name = request.form.get('project_name')
    evaluation_day = request.form.get('evaluation_day')
    start_time = request.form.get('start_time')
    end_time = request.form.get('end_time')

    # Process the form data as needed
    # For example, print the data to the console
    print(f'User ID: {user_id_from_app}')
    #print(f'User password: {password_from_app}')
    print(f'Project Name: {project_name}')
    print(f'Evaluation Day: {evaluation_day}')
    print(f'Start Time: {start_time}')
    print(f'End Time: {end_time}')

    # Perform further actions with the form data if necessary
    result = subprocess.run(['python3', 'eval_booker16.py', user_id_from_app, password_from_app, project_name, evaluation_day, start_time, end_time],
                            capture_output=True, text=True)
    # Print both stdout and stderr for debugging
    print("Output from eval_booker16.py (stdout):", repr(result.stdout))
    print("Output from eval_booker16.py (stderr):", repr(result.stderr))
    
    return "Form submitted successfully"

if __name__ == '__main__':
    app.run(debug=True)
