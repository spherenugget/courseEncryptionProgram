#Author: Victor R Tabuni
#CS1110 LAB09

def getCourseInfo(course_number):
    # Create dictionaries for room numbers, instructors, and meeting times
    rooms = {
        "CS101": 3004,
        "CS102": 4501,
        "CS103": 6755,
        "NT110": 1244,
        "CM241": 1411
    }

    instructors = {
        "CS101": "Haynes",
        "CS102": "Alvarado",
        "CS103": "Rich",
        "NT110": "Burke",
        "CM241": "Lee"
    }

    meeting_times = {
        "CS101": "8:00 a.m.",
        "CS102": "9:00 a.m.",
        "CS103": "10:00 a.m.",
        "NT110": "11:00 a.m.",
        "CM241": "1:00 p.m."
    }
    # Check if course number exists in dictionaries
    if course_number in rooms and course_number in instructors and course_number in meeting_times:
        print(f"Room number: {rooms[course_number]}")
        print(f"Instructor: {instructors[course_number]}")
        print(f"Meeting time: {meeting_times[course_number]}")
    else:
        print("Course not found.")

def getCapitalStates(states_and_capitals):

    import random

    # Create a dictionary containing U.S. states and their capitals
    states_and_capitals = {
        "Alabama": "Montgomery",
        "Alaska": "Juneau",
        "Arizona": "Phoenix",
        "Arkansas": "Little Rock",
        "California": "Sacramento",
        "Colorado": "Denver",
        "Connecticut": "Hartford",
        "Delaware": "Dover",
        "Florida": "Tallahassee",
        "Georgia": "Atlanta",
        "Hawaii": "Honolulu",
        "Idaho": "Boise",
        "Illinois": "Springfield",
        "Indiana": "Indianapolis",
        "Iowa": "Des Moines",
        "Kansas": "Topeka",
        "Kentucky": "Frankfort",
        "Louisiana": "Baton Rouge",
        "Maine": "Augusta",
        "Maryland": "Annapolis",
        "Massachusetts": "Boston",
        "Michigan": "Lansing",
        "Minnesota": "St. Paul",
        "Mississippi": "Jackson",
        "Missouri": "Jefferson City",
        "Montana": "Helena",
        "Nebraska": "Lincoln",
        "Nevada": "Carson City",
        "New Hampshire": "Concord",
        "New Jersey": "Trenton",
        "New Mexico": "Santa Fe",
        "New York": "Albany",
        "North Carolina": "Raleigh",
        "North Dakota": "Bismarck",
        "Ohio": "Columbus",
        "Oklahoma": "Oklahoma City",
        "Oregon": "Salem",
        "Pennsylvania": "Harrisburg",
        "Rhode Island": "Providence",
        "South Carolina": "Columbia",
        "South Dakota": "Pierre",
        "Tennessee": "Nashville",
        "Texas": "Austin",
        "Utah": "Salt Lake City",
        "Vermont": "Montpelier",
        "Virginia": "Richmond",
        "Washington": "Olympia",
        "West Virginia": "Charleston",
        "Wisconsin": "Madison",
        "Wyoming": "Cheyenne"
    }

    # Initialize counters for correct and incorrect responses
    correct_responses = 0
    incorrect_responses = 0

    # Quiz the user
    while True:
        # Randomly select a state from the dictionary
        state = random.choice(list(states_and_capitals.keys()))

        # Ask the user to enter the capital of the selected state
        user_response = input(f"What is the capital of {state}? ")

        # Check if the user's response is correct
        if user_response.lower() == states_and_capitals[state].lower():
            print("Correct!")
            correct_responses += 1
        else:
            print(f"Incorrect. The capital of {state} is {states_and_capitals[state]}.")
            incorrect_responses += 1

        # Display the current score
        print(f"Score: {correct_responses} correct, {incorrect_responses} incorrect")

        # Ask the user if they want to continue
        response = input("Do you want to continue? (yes/no) ")
        if response[0].lower() != "y":
            break

    print("Thanks for playing!")

#ENCRYPT THE FILE WITH CODES
def encrypt_file(infile, outfile, password):

    with open(infile, 'r') as f_in:
        text = f_in.read()

    encrypt_text = ''
    for char in text:
        encrypt_text += password.get(char, char)

    with open(outfile, 'w') as f_out:
        f_out.write(encrypt_text)

def decrypt_file(infile, password):
    with open(infile, 'r') as f_in:
        decrypt_text = f_in.read()
        print('Decrypting....' + '\n' +'\nDecrypted version: \n'+ str(decrypt_text))

def main():
    #COURSE INFORMATION

    # Get user input for course number
    course_number = input("Enter a course number: ")
    getCourseInfo(course_number)

    #CAPITAL QUIZ
    print('\nCAPITAL QUIZ')
    states_and_capitals = {}
    getCapitalStates(states_and_capitals)

    #FILE ENCRYPTION AND DECRYPTION
    print('\nENCRYPTING AND DECRYPTING CODES')
    # Define the code dictionary
    codes = {
        'A': '%', 'a': '9', 'B': '@', 'b': '#', 'C': '$', 'c': '0', 'D': '^', 'd': '!', 'E': '&', 'e': '*',
        'F': '(', 'f': ')', 'G': '-', 'g': '_', 'H': '+', 'h': '=', 'I': '[', 'i': ']', 'J': '{', 'j': '}',
        'K': '|', 'k': '', 'L': ';', 'l': ':', 'M': "'", ' ': '"', 'N': '<', 'n': '>', 'O': '.', 'o': '/',
        'P': ',', 'p': '?', 'Q': '~', 'q': '`', 'R': '1', 'r': '2', 'S': '3', '': '4', 'T': '5', 't': '6',
        'U': '7', 'u': '8', 'V': 'x', 'v': 'y', 'W': 'z', 'w': 'X', 'X': 'Y', 'x': 'Z', 'Y': 'w', 'y': 'v',
        'Z': 'u', 'z': 't'
    }

    password = codes
    input_file = 'original.txt'
    output_file = 'encrypted.txt'
    #encrypting the file
    encrypt_file(input_file, output_file, password)
    #decrypting the file
    decrypt_file(input_file, password)


if __name__ == "__main__":
    main()


#SORRY THIS IS TOO LENGHTY, I hope I can safe more lines as I continue practice my coding