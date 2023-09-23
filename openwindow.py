import os
import subprocess
from flask import Flask, render_template_string, send_file, request

app = Flask(__name__)

# Define the directory where HTML files are located
html_dir = '/home/sick/fuzzing/fuzzer/freedom/output'

# Define the path to the Chrome executable
chrome_executable = '/home/sick/fuzzing/fuzzer/asan-linux-release-1192588/chrome'

@app.route('/')
def list_html_files():
    html_files = [f for f in os.listdir(html_dir) if f.endswith('.html')]
    return render_template_string(
        '''
        <!DOCTYPE html>
        <html>
        <head>
            <title>HTML File Viewer</title>
        </head>
        <body>
            <h1>List of HTML Files</h1>
            <ul>
            {% for file in html_files %}
                <li>
                    <a href="/open/{{ file }}">{{ file }}</a>
                    <form method="post" action="/open_with_chrome/{{ file }}">
                        <input type="submit" value="Open with Chrome">
                    </form>
                </li>
            {% endfor %}
            </ul>
        </body>
        </html>
        ''',
        html_files=html_files
    )

@app.route('/open/<filename>')
def open_html_file(filename):
    # Ensure the requested file is in the allowed directory
    if os.path.isfile(os.path.join(html_dir, filename)):
        return send_file(os.path.join(html_dir, filename))
    else:
        return "File not found."

@app.route('/open_with_chrome/<filename>', methods=['POST'])
def open_html_file_with_chrome(filename):
    # Ensure the requested file is in the allowed directory
    file_path = os.path.join(html_dir, filename)
    if os.path.isfile(file_path):
        try:
            process = subprocess.Popen([chrome_executable, file_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            stdout, stderr = process.communicate()
            output = f"Chrome Standard Output:\n{stdout}\n\nChrome Standard Error:\n{stderr}"
            return output
        except Exception as e:
            return f"Error opening file with Chrome: {str(e)}"
    else:
        return "File not found."

if __name__ == '__main__':
    app.run(debug=True)

