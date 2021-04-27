import logging


class LogGen:

    @staticmethod
    def loggen():
        # logging.basicConfig(filename=".\\Logs\\automation.log",
        #                     format='%(asctime)s: %(levelname)s: %(message)s',
        #                     datefmt='%m/%d/%Y %I:%M:%S %p')

        formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
        handler = logging.FileHandler(filename='.\\Logs\\automation.log')
        handler.setFormatter(formatter)

        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
