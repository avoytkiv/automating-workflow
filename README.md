# Automating workflow

This is a Python script that automates the process of checking an XLSX file for updates, parsing it, and sending messages to different Google Hangout chats.

The script begins by importing necessary modules like os, sys, pandas, logging, traceback, and time. It then sets up logging for the script and initializes the path to the XLSX file to be monitored.

The script defines two functions - `hangout_send_message()` and `read_excel_file()`. The hangout_send_message() function sends a message to a Google Hangout chat using an HTTP request, while the `read_excel_file()` function reads the XLSX file and extracts specific data from it.

The main body of the script runs an infinite loop using while True. In each iteration, the script checks the last modification time of the XLSX file. If the file has been modified since the last check, the script parses the data from the file using the `read_excel_file()` function and creates a message using the extracted data. The message is sent to different Google Hangout chats using the `hangout_send_message()` function.

The urls list contains the URLs for the Google Hangout chats to which the message is sent. The script sleeps for 60 seconds after each iteration of the loop. If any exceptions occur in the main body of the script, it prints the traceback and sleeps for 60 seconds before continuing.

Overall, this script automates the process of checking an XLSX file for updates and sending messages to different Google Hangout chats, making the process more efficient and automated.

This Python script is running within a Docker container, which is being used to run the Python script in a standardized environment that can be easily moved from one server to another. Additionally, both the XLSX file and the Docker container are located on the same server, which is where the script is executing. This allows the script to easily access the file and send messages to the Google Hangout chats without needing to go through any external network connections.

<img width="930" alt="Screenshot 2023-02-22 at 16 18 53" src="https://user-images.githubusercontent.com/74664634/220785491-a10a6014-aad1-492b-90fd-6ef853b0fb6c.png">
