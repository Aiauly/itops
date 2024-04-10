import subprocess

def update_software():
    # Define the command to update software packages based on the operating system
    if platform.system() == 'Windows':
        update_command = 'choco upgrade all -y'  # Command for Chocolatey package manager on Windows
    elif platform.system() == 'Linux':
        update_command = 'sudo apt-get update && sudo apt-get upgrade -y'  # Command for apt package manager on Linux
    else:
        print("Unsupported operating system")
        return
    
    # Execute the update command
    try:
        subprocess.run(update_command, shell=True, check=True)
        print("Software updates completed successfully.")
    except subprocess.CalledProcessError as e:
        print("Error:", e)

if __name__ == "__main__":
    update_software()
    
