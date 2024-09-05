import subprocess

# Run git add .
subprocess.run(["git", "add", "."], check=True)

# Run git commit -m "git INIT"
subprocess.run(["git", "commit", "-m", "git INIT"], check=True)

# Run git push
subprocess.run(["git", "push"], check=True)
