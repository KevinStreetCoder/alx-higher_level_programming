# Python Network #1 - Holberton School

This project is part of the Holberton School curriculum and focuses on network programming in Python. The goal of this project is to learn how to fetch internet resources, make HTTP requests, and work with APIs using Python.

## Project Tasks

### Task 0: What's my status?

Write a Python script that fetches [https://alx-intranet.hbtn.io/status](https://alx-intranet.hbtn.io/status) using the `urllib` package and displays information about the response body.

### Task 1: Response header value

Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the X-Request-Id variable found in the response header using `urllib`.

### Task 2: POST an email

Write a Python script that takes in a URL and an email, sends a POST request to the URL with the email as a parameter, and displays the body of the response (decoded in utf-8) using `urllib`.

### Task 3: Error code

Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response (decoded in utf-8). Handle `urllib.error.HTTPError` exceptions and print the error code if an error occurs.

### Task 4: What's my status? #1

Write a Python script that fetches [https://alx-intranet.hbtn.io/status](https://alx-intranet.hbtn.io/status) using the `requests` package and displays information about the response body.

### Task 5: Response header value #1

Write a Python script that takes in a URL, sends a request to the URL, and displays the value of the X-Request-Id variable in the response header using the `requests` package.

### Task 6: POST an email #1

Write a Python script that takes in a URL and an email address, sends a POST request to the URL with the email as a parameter, and displays the body of the response using the `requests` package.

### Task 7: Error code #1

Write a Python script that takes in a URL, sends a request to the URL, and displays the body of the response using the `requests` package. If the HTTP status code is greater than or equal to 400, print an error message.

### Task 8: Search API

Write a Python script that takes in a letter and sends a POST request to [http://0.0.0.0:5000/search_user](http://0.0.0.0:5000/search_user) with the letter as a parameter using the `requests` package. Display the results based on the response.

### Task 9: My GitHub!

Write a Python script that takes your GitHub credentials (username and password as a personal access token) and uses the GitHub API to display your user id.

### Task 10: GitHub Commits

Write a Python script that lists 10 commits (from the most recent to oldest) of a specified repository by a user. This task involves using the GitHub API to fetch commit information.

## Usage

To run any of the scripts, simply execute them in your terminal. For example:

```bash
./0-hbtn_status.py

