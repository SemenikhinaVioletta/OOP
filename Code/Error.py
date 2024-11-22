class ErrorStatus(Exception):
    def __init__(self, *args):
        if args:
            self.message = args[0]
        else:
            self.message = None
    
    def __str__(self) -> str:
        print("calling str")
        if self.message:
            return "Error status, message: {0}".format(self.message)
        else:
            return "Error status, raised"
