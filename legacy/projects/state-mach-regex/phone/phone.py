import re  # module for processing regular expressions https://docs.python.org/3/library/re.html

# Initial prompt to user
line = input("Enter a phone number to validate or 'exit' when done. ")

# Define regex
numbers = r'([(]*[0-9]{3}[)]*)[-\s]?([0-9]{3})[-\s]?([0-9]*)'

while line != "exit":
    # Find matches
    matches = re.findall(numbers, line)
    match = matches[0]

    # If no match found, print that no number was found
    if not matches:
        print('Number was not found')
    # TODO Else, break number up into area code, prefix, and suffic
    else:
        print(
            f'Area code: {match[0]}\nPrefix: {match[1]}\nSuffix: {match[2]}\n')
    # As a stretch goal, you can modify your regex to search for country codes
    # too and print that out as well!

    # Done validating, read in a new line
    line = input("Enter a phone number to validate or 'exit' when done. ")
