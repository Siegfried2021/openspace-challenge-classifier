# main.py

import sys
from utils.file_utils import load_names_from_excel
from utils.openspace import Openspace

def main(filepath: str):
    names = load_names_from_excel(filepath)
    openspace = Openspace()
    openspace.organize(names)
    openspace.display()
    openspace.store("seating_arrangement.xlsx")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <path_to_excel_file>")
        sys.exit(1)
    
    filepath = sys.argv[1]
    main(filepath)
