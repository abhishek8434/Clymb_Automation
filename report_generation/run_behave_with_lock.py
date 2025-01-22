import os
import time
import subprocess

# Lock file path
lockfile = '/tmp/behave.lock'

# Check if lock file exists
if os.path.exists(lockfile):
    print("Another feature file is already running!")
    exit(1)

try:
    # Create lock file to prevent parallel execution
    with open(lockfile, 'w') as f:
        f.write('locked')
    
    # Run the Behave command to execute feature files
    command = ["behave", "--format", "html", "--outfile", "report.html"]
    result = subprocess.run(command, capture_output=True, text=True)
    
    # Print output from Behave (optional)
    print(result.stdout)
    print(result.stderr)
    
finally:
    # Remove lock file after execution is finished
    os.remove(lockfile)
