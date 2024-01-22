class Log:
    @classmethod
    def info(cls, message: str):
        print("INFO: [" + message + "]")

    @classmethod
    def exception(cls, ex: Exception):
        # 5 onward chops "tuple"
        print("ERROR: [" + str(ex.args) + "]")
