# Progression Outcome Predictor

## Overview

This program allows staff members to predict the progression outcome for students based on the number of credits at pass, defer, and fail. The program will prompt for credit inputs, display the appropriate progression outcome, and create a histogram representation of the outcomes. The program provides error messages for incorrect data types, out-of-range credits, and incorrect total credits.

## Progression Outcome Criteria

The program uses the following criteria for progression outcomes:

```
Volume of Credit at Each Level     Progression Outcome
---------------------------------- ---------------------
1 120 0 0                          Progress
2 100 20 0                         Progress (module trailer)
3 100 0 20                         Progress (module trailer)
... (and so on for 25 more cases)
27 0 20 100                        Exclude
28 0 0 120                         Exclude
```

## Usage Instructions

1. Run the program and enter the number of credits at pass, defer, and fail when prompted.
2. The program will display the appropriate progression outcome for the student.
3. To quit, enter 'q' when prompted. Optionally, enter 'y' to continue predicting progression outcomes for more students.
4. Upon quitting, the program will use the `graphics.py` module to produce a histogram of progression outcomes, displaying the number of students in each category and the total number of students.

## Error Messages

- If a credit input is of the wrong data type, the program will display 'Integer required.'
- If credits entered are not in the range 0, 20, 40, 60, 80, 100, and 120, the program will display 'Out of range.'
- If the total of pass, defer, and fail credits is not 120, the program will display 'Total incorrect.'

## Program Structure

- The program efficiently uses conditional statements to determine progression outcomes without excessive nested conditions.
- The program loops to allow staff members to predict progression outcomes for multiple students.
- The program saves input progression data to a list or nested list for later access.
- In Part 3 (optional), the program saves the input progression data to a text file and retrieves the data for display.

## Example Output

```
To predict progression outcomes, enter the number of credits at pass, defer, and fail.
Enter 'y' for yes or 'q' to quit and view results: y

Enter your total PASS credits: 120
Enter your total DEFER credits: 0
Enter your total FAIL credits: 0
Progress

Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: y

Enter your total PASS credits: 100
Enter your total DEFER credits: 0
Enter your total FAIL credits: 20
Progress (module trailer)

Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: y

Enter your total PASS credits: 80
Enter your total DEFER credits: 20
Enter your total FAIL credits: 20
Module retriever

Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: y

Enter your total PASS credits: 60
Enter your total DEFER credits: 0
Enter your total FAIL credits: 60
Module retriever

Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: y

Enter your total PASS credits: 40
Enter your total DEFER credits: 0
Enter your total FAIL credits: 80
Exclude

Would you like to enter another set of data?
Enter 'y' for yes or 'q' to quit and view results: **q**

Generating histogram...

Progression Outcome:-
Progress - 120, 0, 0
Progress (module trailer) - 100, 0, 20
Module retriever - 80, 20, 20
Module retriever - 60, 0, 60
Exclude – 40, 0, 80
```
