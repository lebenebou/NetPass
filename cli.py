
import subprocess

def runCommand(command: str) -> subprocess.CompletedProcess:

    command = subprocess.run(command, capture_output=True, text=True, shell=True)
    return command