# Python Automated Birthday Wisher Mail Sender

## Description

The Birthday Wisher script sends personalized birthday emails to individuals listed in a CSV file.
The script checks today's date and matches it with the birthday records in the CSV file.
If a match is found, it sends a randomly selected birthday letter to the birthday person via email.

## Prerequisites

Ensure you have the following installed:

    Python 3.x
    pandas library
    python-dotenv library

## Setup

    1. Environment Variables: Create a .env file in the same directory as your script and add your email credentials.

        MY_EMAIL=your_email@gmail.com
        MY_PASSWORD=your_email_password

    2. CSV File: Prepare a birthdays.csv file with the following columns:

        name: Name of the person
        email: Email address of the person
        month: Month of the birthday (as a number)
        day: Day of the birthday

    Example:

        csv

            name,email,month,day
            John Doe,john.doe@example.com,7,17
            Jane Smith,jane.smith@example.com,7,18

    3. Letter Templates: Create a directory named letter_templates and add your letter templates.
       Each template should contain [NAME] placeholder where the name of the person should be inserted.

## Usage

`python3 main.py` on MacOs or `py main.py` on Windows

The script will:

    ~ Load the environment variables.
    ~ Read the current date.
    ~ Load the birthday records from birthdays.csv.
    ~ Select a random letter template.
    ~ Replace the [NAME] placeholder with the actual name.
    ~ Send an email if today's date matches a birthday record.

## Notes

    ~ Make sure to create an App Password if you have 2-Step Verification enabled.
    ~ The script uses the SMTP server of Gmail. Modify the SMTP settings if you are using a different email provider.

## License

This project is licensed under the MIT License. See the LICENSE file for details.