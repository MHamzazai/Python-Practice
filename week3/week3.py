from pathlib import Path
import json, os, time


# Q1. Write a Python script to read a file and print its contents.
def read_file(f_name: str = "Demo.json") -> str:
    file_Path: Path = Path.joinpath(Path(__file__).parent, f_name)
    # add the content if file exists otherwise create a new file
    #                              current folder   file
    with open(file_Path, "w") as file:
        json.dump(
            {
                "name": "Muhammad Hamza zai",
                "age": 17,
                "father name": "Muhammad Ifraq Zai",
                "qualification": "Intermediate",
                "Profession": "Teacher",
                "residence": "Europe",
                "Hobbies": ["cricket", "racing", "swimming"],
            },
            file,
            indent=4,
        )

    # getting it's contents
    with open(file_Path, "r") as file:
        data: dict = json.load(file)

    # deleting the file
    os.remove(file_Path)

    # returning the data
    return json.dumps(data, indent=4)


# print(read_file())


# Q2. Create a file and write your name into it.
def name_file(f_name: str = "Demo2.txt") -> str:
    file_path: Path = Path.joinpath(Path(__file__).parent, f_name)
    # creating a new file
    try:
        with open(file_path, "w") as f:
            f.writelines("Hi, I am Muhammad Hamza Zai!")
    except FileExistsError as e:
        print({e})

    print(
        f"\nYou have 10 seconds to check the file '{f_name}' after it, it will get vanish!"
    )
    time.sleep(10)

    # deleting the file
    os.remove(file_path)

    return f"\n\tThe file '{f_name}' has been deleted!"


# print(name_file())

# Q3. Handle a ZeroDivisionError using try-except.
# Q4. Write a program to handle file not found error.
# Q5. Create a module with a function and import it in another file.
# Q6. Use a list comprehension to filter even numbers from a list.
# Q7. Write a generator that yields even numbers up to N.
# Q8. Create a program to count lines and words in a file.
# Q9. Write a program to read a CSV file and print its contents.
# Q10. Handle multiple exceptions in a single try block
# Q11. Write a program that copies a large text file to another file in chunks (not all at once), and explain why chunked reading matters for memory.
# Q12. Write a program that reads a file and reverses its content line by line, writing the reversed lines to a new file — without loading the whole file into a list at once.
# Q13. Implement a program that uses a context manager (with) to safely append data to a log file, and explain what happens internally if an exception occurs mid-write.
# Q14. Write a program that detects and removes duplicate lines from a text file while preserving the original order.
# Q15. Write a program to merge the contents of multiple .txt files into a single output file, labeling each section with its source filename.
# Excel File Handling (openpyxl focus)
# Q16. Write a program that creates a new Excel workbook, adds a sheet named "Report", and writes a header row followed by 5 rows of sample data.
# Q17. Write a program that reads an existing Excel file and calculates the sum and average of a numeric column, printing the result — without using pandas.
# Q18. Write a program that opens an Excel file, finds all rows where a specific column's value meets a condition (e.g., marks < 40), and writes those rows into a new "Failed" sheet in the same workbook.
# Q19. Write a program that applies formatting (bold headers, colored fills, column width auto-adjust) to an Excel sheet using openpyxl styling.
# Q20. Write a program that reads data from a CSV file and writes it into a formatted Excel file (essentially a CSV-to-XLSX converter).
# Q21. Write a program that appends a new row of data to an existing Excel file without overwriting the existing content.
# Q22. Write a program that reads multiple sheets from one Excel workbook and combines their data into a single summary sheet.
# Q23. Write a program that handles the specific errors that can occur when working with Excel files (e.g., file not found, corrupted file, sheet name doesn't exist, invalid cell reference) using proper exception handling.
# Q24. Write a program that reads an Excel file containing student names and marks, then generates a new Excel file with an added "Grade" column calculated from the marks (using conditional logic).
