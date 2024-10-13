import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"Command succeeded: {command}")
            print(result.stdout)
        else:
            print(f"Command failed: {command}")
            print(result.stderr)
    except Exception as e:
        print(f"Error running command {command}: {e}")

def fix_repository_url():
    # Correct the URL to your actual GitHub repository
    new_url = "https://github.com/rachealkatono/wdd130/"
    
    # Set the remote URL for the repository
    commands = [
        'git remote set-url origin ' + new_url,
        'git fetch',
        'git pull origin main',
        'git status'
    ]

    for cmd in commands:
        run_command(cmd)

if __name__ == "__main__":
    fix_repository_url()
