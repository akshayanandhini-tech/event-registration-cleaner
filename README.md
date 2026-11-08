# Event Registration Cleaner

## 1. Project Overview

The Event Registration Cleaner is a console-based Python application designed to clean, validate, and organize event registration data collected from different sources such as online forms, WhatsApp messages, and manual entries.

Registration data may contain inconsistent formats, missing details, invalid phone numbers, incorrect email formats, and duplicate registrations. This project uses an AI language model to extract information from unstructured text and Python validation rules to check the extracted data.

The main goal is to produce a reliable list of valid registrations and separate records that require human review.

## 2. Problem Statement

Event organizers may receive registration details in different formats. Manually checking every registration takes time and can lead to mistakes.

Common problems include:
- Missing names or contact details.
- Phone numbers containing spaces, country codes, or symbols.
- Email addresses with invalid formats.
- Different ways of writing academic years and department names.
- Duplicate registrations submitted by the same person.
- Unstructured information received through messages.

The Event Registration Cleaner helps automate the process while keeping uncertain or invalid records available for human review.

## 3. Project Objectives

The objectives of this project are:

1. Read registration entries from a CSV file.
2. Use an AI language model to extract structured information.
3. Convert extracted information into a consistent format.
4. Validate phone numbers, email addresses, academic years, and branches using Python.
5. Detect duplicate registrations.
6. Identify missing or invalid information.
7. Generate separate reports for valid and problematic registrations.
8. Maintain transparency by preserving the original registration entry.
9. Prevent the AI from inventing or silently correcting contact information.
10. Allow the event team to review problematic records before taking further action.

## 4. Technologies Used

- **Programming Language:** Python
- **Data Storage:** CSV files
- **AI Integration:** Large Language Model (LLM) API
- **Python Modules:** `csv`, `json`, and other standard modules as required
- **Development Tools:** Python editor or IDE, terminal, and Git
- **Version Control:** Git and GitHub

The exact LLM provider and API will be selected during implementation.

## 5. Input Data

The input file is named `registrations.csv`.

It contains two main columns:

- `id` — a unique identifier for each registration entry.
- `entry` — the original registration information as received.

Example:

| id | entry |
|---|---|
| 1 | Name: Arun Kumar, Phone: 9876543210, Email: arun@example.com, Year: 2, Branch: CSE |
| 2 | Priya S; mobile 98765 43210; priya@example.com; second year; IT |

The project should contain at least 20 sample registration entries with a mixture of valid, invalid, incomplete, differently formatted, and duplicate records.

All sample personal information should be fictional.

## 6. Project Workflow

The application follows these steps:

1. Read registration records from `registrations.csv`.
2. Send the original entry to the configured LLM API.
3. Extract the name, phone, email, year, and branch as structured JSON.
4. Check that extracted contact information actually appears in the original entry.
5. Clean the extracted values using Python functions.
6. Validate the cleaned fields using predefined rules.
7. Compare valid contact details with previously processed records to detect duplicates.
8. Assign an appropriate status to each record.
9. Write valid records and problematic records into separate CSV reports.
10. Generate a summary report containing counts and registration statistics.

Python validation rules, rather than the AI model alone, determine whether the extracted information is acceptable.

## 7. Data Extraction

The AI model extracts the following fields:

- Name
- Phone number
- Email address
- Academic year
- Branch or department

The expected JSON structure is:

    {
      "name": "Arun Kumar",
      "phone": "9876543210",
      "email": "arun@example.com",
      "year": "2",
      "branch": "CSE"
    }

The model must extract only information supported by the original entry. If a field is missing or unclear, it must not invent a value.

The actual API response will be checked and parsed by Python.

## 8. Data Cleaning and Validation Rules

### Name
- Remove unnecessary spaces at the beginning and end.
- Replace repeated spaces with single spaces.
- Convert the name to title case where appropriate.
- Do not invent missing names.

### Phone Number
- Remove spaces, dashes, and the plus sign.
- Remove a leading `91` or `0` according to the project rules.
- The final phone number must contain exactly 10 digits.
- The first digit must be between 6 and 9.
- Verify the number against the original entry before accepting it.

### Email Address
- Convert the email address to lowercase.
- Reject spaces in the email address.
- Require exactly one `@` symbol.
- Require a dot after the `@` symbol.
- Preserve the original entry for verification.

These checks are basic validation rules and do not guarantee that an email address or phone number is active.

### Academic Year
- Accept academic years from 1 to 4.
- Convert formats such as `first year`, `second year`, and Roman numerals I–IV into numbers 1–4.
- Treat the final year as year 4.
- Mark missing or unrecognized values for review.

### Branch
The accepted branch values are:

- CSE
- IT
- AIDS
- ECE
- EEE
- MECH
- CIVIL

Recognized variations may be mapped to these standard values. Unknown branches should be stored as `other`.

### Duplicate Detection
A record is considered a duplicate when its cleaned phone number or cleaned email address matches an earlier accepted record.

The first accepted occurrence is retained. Later matching records are marked as duplicates and sent to `problems.csv`.

## 9. Registration Status

Each registration receives one of the following statuses:

- `valid` — the required fields pass validation and the record is not a duplicate.
- `needs_fix` — one or more fields are missing, invalid, or require human review.
- `duplicate` — the cleaned phone number or email address matches an earlier accepted record.

The processing order and handling of conflicting conditions will follow the rules approved by the project guide.

## 10. Output Files

### clean_list.csv
Contains registrations that pass validation and are not duplicates.

Expected information includes:
- Registration ID
- Cleaned name
- Cleaned phone number
- Cleaned email
- Academic year
- Branch

### problems.csv
Contains registrations that need correction or review, including duplicates.

Expected information includes:
- Registration ID
- Original entry
- Extracted or cleaned fields, where available
- Status
- Reason for the problem

### summary.txt
Contains a summary of the processing results, including:
- Total number of registrations processed.
- Number of valid registrations.
- Number of registrations needing fixes.
- Number of duplicate registrations.
- Valid registrations grouped by branch.
- Valid registrations grouped by academic year.

## 11. Planned Python Functions

The project will use separate functions to make the code easier to understand, test, and maintain.

- `read_entry()` — reads registration data.
- `is_valid()` — checks whether a field or record satisfies the relevant validation rules.
- `check_facts()` — verifies extracted contact information against the original entry.
- `clean_phone()` — standardizes and validates phone numbers.
- `clean_email()` — standardizes and validates email addresses.
- `clean()` — cleans and organizes the extracted registration fields.
- `process()` — coordinates extraction, validation, duplicate detection, and status assignment.
- `write_reports()` — generates the output reports.

The function definitions and responsibilities may be refined during implementation while preserving the approved project requirements.

## 12. AI Safety and Reliability

The AI model is used for information extraction, not as the final authority on data validity.

The project will apply the following safeguards:

- Preserve the original registration entry.
- Instruct the model not to invent missing information.
- Use structured JSON output.
- Validate extracted contact information against the original text.
- Apply deterministic Python rules after extraction.
- Detect duplicates using cleaned contact information.
- Handle API failures and invalid JSON using appropriate error handling.
- Never place API keys directly in source code or upload them to GitHub.
- Send uncertain or problematic records for human review.

Text inside a registration entry must be treated as data, not as instructions to the AI system.

## 13. Testing and Evaluation

The application will be tested with normal, incomplete, invalid, duplicate, and potentially misleading entries.

Testing will include:

1. Valid registration details.
2. Missing or invalid phone numbers.
3. Invalid email formats.
4. Different academic-year formats.
5. Recognized and unknown branch names.
6. Duplicate registrations with differently formatted phone numbers.
7. AI output containing information that was not present in the original entry.
8. Prompt-injection text inside a registration entry.
9. Missing files, malformed CSV rows, invalid JSON, and API errors.

An evaluation set containing five entries will be used to compare expected and actual statuses and cleaned phone numbers. Three red-team tests will check whether the application resists invented data, embedded instructions, and differently formatted duplicates.

## 14. Human Review

Records written to `problems.csv` will be reviewed by the event team.

The team can contact registrants to confirm missing or unclear information and correct errors. The application will not automatically invent missing information or silently change contact details.

The original entry and the reason for each problem will be retained to support this review.

## 15. API Cost and Performance

The project will record:
- The approximate number of API calls made per day.
- The average time taken for an API call.
- The estimated daily API cost, based on the selected provider's pricing and actual usage.

These values will be measured or estimated after the API provider and model have been selected. They will not be treated as confirmed values before testing.

## 16. Project Folder Structure

The project will follow this structure:

    event-registration-cleaner/
    |
    |-- documents/
    |   |-- specification.docx
    |   |-- system_prompt.txt
    |   |-- judgment_framework.md
    |   |-- ai_decision_journal.md
    |
    |-- data/
    |   |-- registrations.csv
    |
    |-- src/
    |   |-- main.py
    |
    |-- tests/
    |   |-- test_cases.csv
    |   |-- evaluation_results.txt
    |   |-- red_team_results.txt
    |
    |-- clean_list.csv
    |-- problems.csv
    |-- summary.txt
    |-- README.md
    |-- .gitignore

This structure may be adjusted as the project develops.

## 17. Setup and Execution

The application will be implemented using a supported version of Python.

Planned execution steps:

1. Install Python and verify the installation.
2. Create the project folder and required subfolders.
3. Prepare `data/registrations.csv`.
4. Configure the LLM API key using an environment variable or another secure method.
5. Install any additional dependencies required by the selected API provider.
6. Run the application from the project directory.
7. Review the generated CSV reports and summary file.

The planned command is:

    python src/main.py

This command will work after `src/main.py` has been implemented.

## 18. Version Control and Documentation

Git will be used to track project changes, and GitHub will host the project repository.

The repository will include:
- Source code.
- Sample registration data.
- Project documentation.
- Testing and evaluation results.
- Red-team testing results.
- Judgment framework.
- AI decision journal.
- A `.gitignore` file to prevent API keys and other sensitive files from being committed.

At least three meaningful commits will document progress throughout development.

## 19. Final Deliverables

The final submission will include:

1. Approved project specification.
2. Sample `registrations.csv` with at least 20 entries.
3. Working Python application.
4. Required AI system prompt in a separate text file.
5. `clean_list.csv`.
6. `problems.csv`.
7. `summary.txt`.
8. Evaluation results.
9. Red-team test results.
10. Judgment Framework table.
11. API cost and latency note.
12. AI Decision Journal.
13. GitHub repository and README.
14. A reflection of approximately 400 words.
15. A presentation for the project showcase.

## 20. Current Project Status

**Current stage:** Project setup and specification approval.

The next steps are to:
1. Submit the project specification to the faculty guide for approval.
2. Prepare at least 20 fictional registration entries.
3. Set up Python and the development environment.
4. Test one AI extraction request end to end.
5. Implement cleaning, validation, and duplicate detection.
6. Generate reports and complete testing.
7. Prepare the documentation and final presentation.

The project will be developed step by step, with the specification approved before full implementation begins.