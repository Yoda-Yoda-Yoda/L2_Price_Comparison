# Functions go here
def make_statement(statement, decoration):
    """Emphasises headings by adding decoration
    at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")

def instructions():
    make_statement("Heading", "💰")

    print('''
Instructions 


    ''')
instructions()