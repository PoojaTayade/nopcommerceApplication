import logging

class LogGen:
    @staticmethod
    def loggen():
        FORMAT = '%(asctime)s: %(levelname)s: %(message)s'
        DATEFMT ='%Y-%m-%d %H:%M:%S'
        logging.basicConfig(filename='.\\Logs\\Automation.log',format=FORMAT,datefmt=DATEFMT,encoding='utf8',filemode='w',force=True)
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger