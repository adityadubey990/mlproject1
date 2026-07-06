from src.mlproject1.logger import logging
from src.mlproject1.exception import CustomException
import sys


if __name__=="__main__":
    logging.info("The execution has started")
    
    try:
        a=1/0
    except Exception as e:
        logging.info("Divide by zero error has occured")
        raise CustomException(e,sys)