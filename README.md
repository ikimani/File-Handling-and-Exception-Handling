Week 4 Assignment — File Handling and Exception Handling

Author: Hadassa Wangari Kimani
Course: Power Learn Project — Software Development (Python Track)
Date: October 2025

📘 Description

This project demonstrates the use of file handling and exception handling in Python.

It includes two parts:

File Read & Write Challenge: Reads names from a file, modifies the content, and writes the results into a new file.

Error Handling Lab: Prompts the user for a filename and handles errors such as missing or inaccessible files.

🧩 Files in this Repository

week_4_assignment.py → Main Python program with both tasks.

students.txt → Example input file with sample student names.

students_upper.txt → Output file automatically created by the program (after running Part 1).

🧪 How to Run

Make sure you have Python 3 installed.

Save the files in the same folder.

Run the program in a terminal or IDE with:

python week_4_assignment.py


When prompted:

Enter 1 to run the File Read & Write Challenge

Enter 2 to run the Error Handling Lab

🧠 Example

If students.txt contains:

Alice
Bob
Charlie


The program will create a file students_upper.txt with:

ALICE
BOB
CHARLIE


If the user tries to open a missing file, the program will print:

⚠️ File not found. Please check the filename and try again.
