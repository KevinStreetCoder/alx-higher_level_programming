# Project: Python Network 0

This project contains a set of Bash and Python scripts for performing various network-related tasks using cURL and Python. The scripts are designed to meet specific requirements and perform tasks such as sending HTTP requests, handling JSON data, and more.

## Requirements
- Allowed editors: vi, vim, emacs
- All scripts will be tested on Ubuntu 20.04 LTS
- All Bash scripts should be exactly 3 lines long
- All your files must end with a new line
- All your files must be executable
- The first line of all Bash files should be exactly `#!/bin/bash`
- The second line of all Bash scripts should be a comment explaining the script's purpose
- All cURL commands must have the option `-s` (silent mode)
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.8.5
- The first line of all Python files should be exactly `#!/usr/bin/python3`
- The code should use pycodestyle (version 2.8.*)
- All modules, classes, and functions should be documented with meaningful descriptions

## List of Tasks

### Task 0: cURL body size
- Script: [0-body_size.sh](0-body_size.sh)
- Description: This Bash script sends a GET request to a URL and displays the size of the response body in bytes.

### Task 1: cURL to the end
- Script: [1-body.sh](1-body.sh)
- Description: This Bash script sends a GET request to a URL and displays the body of the response for a 200 status code.

### Task 2: cURL Method
- Script: [2-delete.sh](2-delete.sh)
- Description: This Bash script sends a DELETE request to a URL and displays the body of the response.

### Task 3: cURL only methods
- Script: [3-methods.sh](3-methods.sh)
- Description: This Bash script takes a URL and displays all HTTP methods the server will accept.

### Task 4: cURL headers
- Script: [4-header.sh](4-header.sh)
- Description: This Bash script sends a GET request to a URL with a custom header and displays the body of the response.

### Task 5: cURL POST parameters
- Script: [5-post_params.sh](5-post_params.sh)
- Description: This Bash script sends a POST request to a URL with specified parameters and displays the body of the response.

### Task 6: Find a peak
- Script: [6-peak.py](6-peak.py)
- Description: This Python script defines a function to find a peak in a list of unsorted integers.

### Task 7: Display only the status code
- Script: [100-status_code.sh](100-status_code.sh)
- Description: This Bash script sends a request to a URL and displays only the status code of the response.

### Task 8: cURL a JSON file
- Script: [101-post_json.sh](101-post_json.sh)
- Description: This Bash script sends a JSON POST request to a URL with the contents of a JSON file and displays the response.

### Task 9: Catch me if you can!
- Script: [102-catch_me.sh](102-catch_me.sh)
- Description: This Bash script makes a request to a URL that causes the server to respond with "You got me!".

## Usage
You can run these scripts individually as needed. For example:
```bash
./0-body_size.sh 0.0.0.0:5000
./1-body.sh 0.0.0.0:5000/route_1
./2-delete.sh 0.0.0.0:5000/route_3
# ...and so on for other tasks
