import logging


class Logger:
    def __init__(self, message, errors):
        file_name = "Logs_data"
        if len(errors) == 0:
            logging.basicConfig(
                format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
                level=logging.INFO,
            )
            logging.info(message)
            
            logging.basicConfig(
                format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
                level=logging.INFO,
            )
        else:
            logging.basicConfig(
                format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
                level=logging.INFO,
            )
            logging.error(errors + ": " + message)
