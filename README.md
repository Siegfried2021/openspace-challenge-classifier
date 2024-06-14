# openspace-challenge-classifier
Our repository for the openspace challenger

OPENSPACE SEATING MANAGEMENT SYSTEM

Description

Your company recently moved to a new office featuring an open space layout with 6 tables, each having 4 seats. As many employees are new, you came up with the idea of changing seats daily to foster better relationships and collaboration among colleagues. This program will run every day to re-assign everyone to a new seat randomly.

The program allows you to:

   - Import a list of colleagues from an Excel file.
   - Randomly assign colleagues to seats at different tables.
   - Display the seating arrangement.


INSTATALLATION

    1. Ensure you have Python installed on your machine. The code is 
       compatible with Python 3.x versions.

    2. Clone this repository to your local machine:
            git clone <repository-url>

    3. Navigate to the project directory:
            cd <repository-directory>

    4. Install the required dependencies using pip:        
            pip install -r requirements.txt
            

USAGE

Seat Class

The Seat class is used to represent an individual seat. It has two main attributes:

    - free : A boolean indicating whether the seat is free or occupied.
    - occupant: A string representing the name of the person occupying the seat.

Methods in the Seat class:

    - set_occupant(name): Assigns a person to the seat if it is free.
    - remove_occupant(): Removes the occupant from the seat and returns their name.

Table Class

The Table class represents a table with a certain number of seats.

Attributes:

    -capacity: An integer representing the number of seats at the table.
    -seats: A list of Seat objects.

Methods in the Table class:

    -has_free_spot(): Returns True if there is at least one free spot at the table.
    -assign_seat(name): Assigns a person to a free seat at the table.
    -left_capacity(): Returns the number of free seats left at the table.

Openspace Class

The Openspace class manages multiple tables and organizes the seating.

Attributes:

    -number_of_tables: An integer representing the number of tables.
    -tables: A list of Table objects.

Methods in the Openspace class:

    -organize(names): Randomly assigns people to seats across all tables.
    -display(): Displays the seating arrangement.     

Contributing

       