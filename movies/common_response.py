class CommonResponse:
    @classmethod
    def get_formatted_response(cls, success, response_data, message):
        return {
            "success": success,
            "message": message,
            "data": response_data,
        }
