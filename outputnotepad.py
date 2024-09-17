import subprocess

# Step 1: Run the command and capture the output
# command = ["java", "--version"]
# command = ["cmd", "/c", "dir"]
# command = ["python", "day.5.py"]
# command = ["pip", "install", "pytube", "lyricsgenius"]
command = ["docker","build","-t","my-docker-app"]
result = subprocess.run(command, capture_output=True, text=True)

# Get the standard output and error
output = result.stdout
error = result.stderr

# Combine output and error (if any) into a single string
full_output = output + error

# Step 2: Write the output to a file
file_path = "output.txt"
with open(file_path, "w") as file:
    file.write(full_output)

print(f"Output written to {file_path}")

# Optionally: Open the file in Notepad
import os
os.system(f"notepad {file_path}")
