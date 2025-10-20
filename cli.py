import argparse
import sys 
import os

class CLI:
    # command line interface is intialized demo version
    def __init__(self):
        self.filepath = None
        self.flags = []
        self.parser = self._create_parser()
    
    
    def _create_parser(self):
        parser = argparse.ArgumentParser(
            description='Static Vulnerability Scanner for python files',
            epilog='Ex. python main.py main.py yourscript.py'
        )

        parser.add_argument(
            'filepath',
            help='Path to the python file to scan'

        )

        parser.add_argument(
            '--risky',
            action='store_true',
            help='Check for risky functions (eval, execute)'
        )

        parser.add_argument(
            '--validation',
            action='store_true',
            help='Check for missing input validation'
        )

        parser.add_argument(
            '--deprecated',
            action='store_true',
            help='Check for deprecated functions'
        )

        return parser
    
    # parser to take in positional argument of file path and flags
    def parse_arguments(self, args=None):
        parsed = self.parser.parse_args(args)
        self.filepath = parsed.filepath

        if parsed.risky:
            self.flags.append('risky')
        if parsed.validation:
            self.flags.append('validation')
        if parsed.deprecated:
            self.flags.append('deprecated')

        if not self.flags:
            self.flags =['risky', 'validation', 'deprecated']
        
        return self.filepath, self.flags


        
    
    def validate_file(self):
        #checks if the file is a file and that the path points to 
        # a python file
        if not os.path.isfile(self.filepath):
            return False
        if not self.filepath.lower().endswith('.py'):
            return False
        return True
    

    def run(self):
        try:
            self.parse_arguments()
            #Decorators and Title print out
            print(f"\n{'-'*70}")
            print(f"Static Vulnerability Scanner - DEMO VERSION")
            print(f"{'-'*70}\n")
            print(f"Scanning: {self.filepath}")
            print(f"Flags enabled: {', '.join(self.flags)}\n")

            #Validate file
            if not self.validate_file():
                print("Error: Invalid file, must be a .py file that exist")
                sys.exit(1)
            
            print("File validation successful")

            print("Scanning file...")

            self.display_mock_report()

            # calling the format choice function
            format_choice = self.prompt_for_format()
            print(f"\n Report saved as {format_choice}")
            
            print(f"\n{'-'*70}")
            print("End of Demo")
            print(f"{'-'*70}\n")

        # Exit on user input and print exception
        except KeyboardInterrupt:
            print("\n\nSession Interuppted by user. Exiting...")
            sys.exit(1)
        except Exception as e:
            print(f"Error: {str(e)}")
            sys.exit(1)


            



    def display_mock_report(self):
        print(f"\n{'-'*70}")
        print("Vulnerability Report(Example)")
        print(f"{'-'*70}\n")
        print(f"file: {self.filepath}")
        print(f"Timestamp :[Monday, October 20th 4pm]")

        #mock issues
        print("Issues Found: 1")

        print("1. line 19: Use of eval() function")
        print("   Severity: HIGH")
        print("   Category: Risky Function")
        print("   Recommendation: Use ast.literal_eval() instead\n")

        print(f"{'-'*50}")


    def prompt_for_format(self):
        while True:
            print("\nChoose output format:")
            print("  1. Plain text (.txt)")
            print("  2. HTML (.html)")
            response = input("Enter the number of your choice: ").strip()
            if response == "1":
                return "txt"
            elif response == "2":
                return "html"
            else:
                print("Invalid choice Please enter 1 or 2")

if __name__ == "__main__":
    cli = CLI()
    cli.run()




