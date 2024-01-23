# MeToGod

## Overview

The MeToGod repository is designed to read phone numbers from WhatsApp and save them in a CSV file. Additionally, if someone has a subscription for ME, users can find the name of the phone number owner. The user interface is built using SimpleGUI for a straightforward user experience.
## Main Window

The main window of the application provides different functionalities based on user actions. Here's an overview of the available options:

![Main Window](/images/main_window.png)
## Usage
### Read from Excel File

- Clicking "Read from Excel File" opens a new window with the option to input an Excel file.
- After submitting the file, the program reads the file, scrapes ME information, and saves the results in a CSV file.

   ![Read from Excel File](/images/excel_file.png)

### Read from WhatsApp

- Clicking "Read from WhatsApp" opens a window for searching numbers in a WhatsApp group.
- After submitting the group name, the program searches for numbers, scrapes ME information, and saves the results in a CSV file.

   ![Read from WhatsApp](/images/whatsapp.png)

### Read from WhatsApp - Numbers Only

- Clicking "Read from WhatsApp - Numbers Only" opens a window to get numbers from a WhatsApp group without additional information.
- After submitting the group name, the program searches for numbers and saves them in a CSV file.

   ![Read from WhatsApp - Numbers Only](/images/whatsapp.png)

### Split Excel File

- Clicking "Split Excel File" opens a window to split an Excel file into smaller files.
- After submitting the file name and the number of rows per file, the program splits the Excel file.

   ![Split Excel File](/images/spliter.png)

## Notes

- The code uses SimpleGUI for the user interface.
- Ensure that the required dependencies are installed (provide them in the `requirements.txt` file).


## Setup Instructions

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt` (if applicable).
3. Run the main code using a Python interpreter.

