import subprocess
import time


unix_timestamp = int(time.time())

# Your string
original_string = "This is my string"

# Append the Unix timestamp to the string
result_string = f"{original_string} {unix_timestamp}"

# Print the result
print(result_string)
# Run git add .
subprocess.run(["git", "add", "."], check=True)

# Run git commit -m "git INIT"
subprocess.run(["git", "commit", "-m", "git INIT"], check=True)

# Run git push
subprocess.run(["git", "push"], check=True)


