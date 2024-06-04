import logging
import os 
import datetime

time_for_log_record=datetime.datetime.now().strftime("%Y-%m-%d %H")
logs_filename=f"{time_for_log_record}.log"
LOG_directory_path=os.path.join(os.getcwd(),"logs")
os.makedirs(LOG_directory_path,exist_ok=True)
logging.basicConfig(
    filename=os.path.join(LOG_directory_path,logs_filename),
    level=logging.INFO,
    format='[%(asctime)s]:%(levelname)s: %(lineno)s %(message)s'
)


