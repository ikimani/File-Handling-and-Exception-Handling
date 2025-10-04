# Week 4 Assignment — File Handling and Exception Handling
# Author: Hadassa Wangari Kimani
# Date: October 2025
# Description: This program demonstrates reading and writing files in Python,
# and includes error handling for missing or invalid files.

# --- PART 1: File Read & Write Challenge ---

def file_read_write():
    try:
        # Step 1: Read data from the original file
        with open("students.txt", "r") as infile:
            content = infile.readlines()

        # Step 2: Modify the content (convert names to uppercase)
        modified_content = [line.strip().upper() + "\n" for line in content]

        # Step 3: Write the modified content to a new file
        with open("students_upper.txt", "w") as outfile:
            outfile.writelines(modified_content)

        print("✅ File has been read, modified, and saved successfully as 'students_upper.txt'.")

    except FileNotFoundError:
        print("⚠️ Error: The file 'students.txt' was not found. Please make sure it exists.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")


# --- PART 2: Error Handling Lab ---

def error_handling_lab():
    try:
        filename = input("Enter the filename you want to read: ")

        with open(filename, "r") as file:
            data = file.read()
            print("\n--- File Contents ---")
            print(data)

    except FileNotFoundError:
        print("⚠️ File not found. Please check the filename and try again.")
    except PermissionError:
        print("⚠️ You don’t have permission to access this file.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")
    finally:
        print("\nProgram execution completed.")


# --- MAIN PROGRAM EXECUTION ---

if __name__ == "__main__":
    print("=== WEEK 4: FILE HANDLING & EXCEPTION HANDLING ASSIGNMENT ===\n")
    print("1. Run File Read & Write Challenge")
    print("2. Run Error Handling Lab")

    choice = input("\nEnter your choice (1 or 2): ")

    if choice == "1":
        file_read_write()
    elif choice == "2":
        error_handling_lab()
    else:
        print("Invalid choice. Please run the program again and select 1 or 2.")
