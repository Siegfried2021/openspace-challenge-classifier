### OPENSPACE SEATING MANAGEMENT SYSTEM

**Project Overview**

Our company has recently moved to a new office featuring an open space layout with 6 tables, each equipped with 4 seats, totaling 24 seats in all. To encourage better relationships and teamwork among team members, we have decided to rotate seating arrangements daily.

This project aims to automate the daily re-assignment of seats with the following objectives:

- **Load Colleagues List:** Load a list of colleagues from an Excel file.
- **Random Seat Assignment:** Randomly distribute colleagues to the available seats.
- **Display Seating Arrangement:** Display the seating arrangement in a user-friendly format.
- **Handle Overcapacity:** Manage cases where the number of people exceeds the available seats.
- **Save Arrangement:** Save the seating arrangement to an Excel file for record-keeping.

**Features**

- **Load Colleagues List:** The program accepts a file path to an Excel file containing a list of colleagues.
- **Random Seat Assignment:** Colleagues are randomly assigned to the available seats at the tables.
- **Display Seating Arrangement:** The seating arrangement is presented in a clear and organized format.
- **Handle Overcapacity:** If there are more people than available seats, the program will manage this scenario effectively.
- **Save Arrangement:** After seat assignment, the seating arrangement is saved to an Excel file.

**File Structure**

- `main.py`: Main script to execute the program.
- `utils/file_utils.py`: Contains functions to handle Excel file operations, specifically loading colleague names.
- `utils/openspace.py`: Implements the `Openspace` class responsible for organizing and displaying the seating arrangement.
- `utils/table.py`: Defines the `Table` and `Seat` classes, which represent the structure of tables and seats within the office layout.

This system enhances office dynamics by promoting daily interaction among team members in our new open space environment.

## Installation & Usage

To get started with the project, follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/Siegfried2021/openspace-challenge-classifier
    cd openspace-challenge-classifier
    ```

2. Install the required dependencies using `pip`:

    ```bash
    pip install -r requirements.txt
    ```

3. Make sure you have Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

4. Prepare your Excel file containing the list of colleagues. Ensure it has the correct format and column names as expected by the program.
    * The names should be listed under the column named `Colleagues`.

5. Run the main script with the path to your Excel file as an argument:

    ```bash
    python main.py <path_to_your_excel_file.xlsx>
    ```

6. Follow the on-screen instructions to see the seating arrangement and save the results.

This will set up the project on your local machine and allow you to run it with your own data.

## Contributors

**Project Discussion and Setup:** Alper, Mathieu, Racheal, Hui
**Task Assignment and Trello Setup:** Alper
**Creating a complete GitHub repository:** Mathieu
***Code writing:**
**Seats_assignment:** Hui, Racheal
**Table_assignment:** Alper
**Openspace:** Mathieu, Hui
**file_utils:** Alper
**main:** Alper
**Debugging:** Mathieu, Alper, Hui, Racheal
**README:** Mathieu, Alper, Hui, Racheal

Tabii, işte günler ve milestone'lar olarak düzenlenmiş bir timeline:

---

## Project Timeline

### Day 1

- **Project Initialization and Setup**
  - Project discussion and task assignment
  - Trello setup and task management
  - GitHub repository setup

- **Code Implementation**
  - Implement `Seats_assignment.py` (Seat management)
  - Implement `Table_assignment.py` (Table management)

- **Milestone:** Basic seat and table management implemented

### Day 2

- **Openspace Implementation**
  - Implement `Openspace.py` (Manage multiple tables)
  - Implement `file_utils.py` (File operations)

- **Main Script Development**
  - Write `main.py` for project execution

- **Testing and Debugging**
  - Test all components
  - Debug and ensure functionality

- **Documentation**
  - Write comprehensive README.md file

- **Milestone:** Project complete and ready for review
