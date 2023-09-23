import os
from bs4 import BeautifulSoup

# Directory containing HTML files
output_directory = "output"

# JavaScript code to add
javascript_code = """
<script>
    setTimeout(function(){
        window.close();
    }, 5000);
</script>
"""

# Iterate over HTML files in the directory
for filename in os.listdir(output_directory):
    if filename.endswith(".html"):
        file_path = os.path.join(output_directory, filename)
        
        # Read the HTML file
        with open(file_path, "r") as file:
            html_content = file.read()

        # Parse the HTML content
        soup = BeautifulSoup(html_content, "html.parser")

        # Add the JavaScript code to the end of the HTML file
        soup.body.append(BeautifulSoup(javascript_code, "html.parser"))

        # Save the modified HTML back to the file
        with open(file_path, "w") as file:
            file.write(str(soup))
