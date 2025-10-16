class CLI:
    # command line interface is intialized demo version
    def __init__(self):
        self.filepath = None
        self.flags = []
        self.parser = self._create_parser
    
    
    def _create_parser():
        parser = argparse.ArgumentParser(
            description='Static Vulnerability Scanner for python files'
            epilog='Ex. python main.py main.py yourscript.py'
        )

        parser.add_argument(
            'filepath',
            help='Path to the python file to scan'

        )

        parser.add_argument(
            '--risky',
            action='store_true'
            help='Check for risky functions (eval, execute)'
        )

        parser.add_argument(
            '--validation',
            action='store_true'
            help='Check for missing input validation'
        )

        parser.add_argument(
            '--depricated',
            action='store_true'
            help='Check for depricated functions'
        )

        return parser
    
    def partse_arguments():
        pass
    
    def run():
        pass

    def display_report():
        pass

    def prompt_for_save():
        pass

    def prompt_for_format():
        pass


# parser.add_argument(
#     'name_or_flag',           # Required: 'filepath' or '--risky'
#     action='store',           # What to do with the value
#     nargs=1,                  # How many arguments to consume
#     const=None,               # Constant value for certain actions
#     default=None,             # Default value if not provided
#     type=str,                 # Convert to this type (int, float, etc.)
#     choices=['a', 'b'],       # Limit to these choices
#     required=False,           # Force optional arg to be required
#     help='help text',         # Description for --help
#     metavar='FILE',           # Name in usage messages
#     dest='variable_name'      # Store in this variable name
# )
