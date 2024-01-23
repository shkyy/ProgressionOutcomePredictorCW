# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: 20220957
# Date: 11/26/2023

from w2052738_histogram import histogram
from w2052738_enum import Outcome

# Define variables
credit_range = [0, 20, 40, 60, 80, 100, 120]
total = 120
progression_data = []

# Check whether the user input is in the valid ranges
def is_valid(credits):
    return credits in credit_range

# Get the user input (a common control function)
def get_user_input(user_input):
    while True:
        try:
            credits = int(input(user_input))
            if not is_valid(credits):
                print("Credit out of range!")
                continue
            return credits
        except ValueError:
            print("Integer required!")

# Check the outcome
def get_outcome(pass_credits, defer_credits, fail_credits):
    
    if pass_credits == total:
        return Outcome.PROGRESS
    elif (pass_credits == 100 and defer_credits == 20) or (pass_credits == 100 and fail_credits == 20):
        return Outcome.TRAILER
    elif pass_credits <= 40 and fail_credits >= 80:
        return Outcome.EXCLUDE
    else:
        return Outcome.RETRIEVER

# The main funtion
def main():
    
    # Define variables for counts
    progress_count = 0
    trailing_count = 0
    module_retriever_count = 0
    exclude_count = 0

    # Main loop to identify the student and the staff member, and ensure the input validity
    while True:
        try:
            role = input("Are you a staff or a student? (type 't' for staff or 's' for student) ")
            
            if role.lower() == 't' or role.lower() == 's':
                break
            else:
                print("Invalid Input!")
                continue

        except ValueError:
            print("Invalid Input!")
            continue

    # The student and the funtionality
    if role.lower() == "s":
        while True:

            # Get user input using the funtion 'get_user_input'
            pass_credits = get_user_input("\nPlease enter your credits at pass: ")
            defer_credits = get_user_input("Please enter your credits at defer: ")
            fail_credits = get_user_input("Please enter your credits at fail: ")

            # Calculate the total credits
            total_credits = pass_credits + defer_credits + fail_credits

            # Total validation
            if total_credits != total:
                print("Total incorrect..")
                continue
            
            # Use 'get_outcome' funtion and display the outcome
            else:
                outcome = get_outcome(pass_credits, defer_credits, fail_credits)
                print("\nStored Progression Data:")
                print(f"{outcome.value}: {pass_credits}, {defer_credits}, {fail_credits}")
                break
    
    # The staff and the funtionality
    else:
        while True:
            
            # Promt the user for input using the funtion 'get_user_input'
            pass_credits = get_user_input("\nPlease enter your credits at pass: ")
            defer_credits = get_user_input("Please enter your credits at defer: ")
            fail_credits = get_user_input("Please enter your credits at fail: ")

            # Calculate the total credits
            total_credits = pass_credits + defer_credits + fail_credits

            # Total validation
            if total_credits != total:
                print("Total incorrect..")
                continue
            
            # Use the 'get_outcome' function and display the resulting outcome
            outcome = get_outcome(pass_credits, defer_credits, fail_credits)
            print(outcome.value)

            # Put data into a dictionary
            data = {'Outcome': outcome.value, 'Pass Credits': pass_credits, 'Defer Credits': defer_credits, 'Fail Credits': fail_credits}
            progression_data.append(data)

            # Get the count of outcomes (for histogram)
            if outcome == Outcome.PROGRESS:
                progress_count += 1
            elif outcome == Outcome.TRAILER:
                trailing_count += 1
            elif outcome == Outcome.RETRIEVER:
                module_retriever_count += 1
            elif outcome == Outcome.EXCLUDE:
                exclude_count += 1

            # Prompt the user for input to determine whether to continue or quit, and ensure the input validity
            print("\nWould you like to enter another set of data?")
            while True:
                try:
                    choice = input("Enter 'y' to continue, 'q' to quit: ")
                    
                    if choice.lower() == 'y' or choice.lower() == 'q':
                        break
                    else:
                        print("Invalid Input!")
                        continue

                except ValueError:
                    print("Invalid Input!")
                    continue
            
            # Quit the program
            if choice.lower() == 'q':

                # Display the Progression Data
                print("\nStored Progression Data:-")
                for data in progression_data:
                    outcome = data['Outcome']
                    pass_credits = data['Pass Credits']
                    defer_credits = data['Defer Credits']
                    fail_credits = data['Fail Credits']

                    print(f"{outcome}: {pass_credits}, {defer_credits}, {fail_credits}")

                # Create the histogram
                histogram(progress_count, trailing_count, module_retriever_count, exclude_count)
                break

if __name__ == "__main__":
    main()