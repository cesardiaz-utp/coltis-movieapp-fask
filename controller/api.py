class ApiResponse:
    def __init__(self, data = None, message = None) -> None:
        self.data = data
        self.message = message

    def json(self):
        return {
            "error": self.message != None,
            "data": self.data,
            "error_message": self.message
        }