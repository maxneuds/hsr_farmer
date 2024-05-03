import logging
import logging.config
from datetime import datetime as dt

# def setup_logger():
#     logging.basicConfig(filename='logs/app.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

# Define a custom formatter
class CustomFormatter(logging.Formatter):
    def format(self, record):
        record.function_name = record.funcName  # Get the function name
        return super().format(record)

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# Create a stream handler
handler = logging.StreamHandler()
handler.setLevel(logging.DEBUG)

# Set the custom formatter
# '[%(asctime)-s] [%(levelname)-8s]  %(message)-s'
# formatter = CustomFormatter('%(asctime)s - %(levelname)s - %(function_name)s - %(message)s')
formatter = CustomFormatter('[%(asctime)-s] [%(levelname)-5s] [%(function_name)s]  %(message)-s', datefmt='%H:%M:%S')
handler.setFormatter(formatter)

# Enable to set path in logger
def logger_set_path(path_num):
    formatter = CustomFormatter(f'[%(asctime)-s] [%(levelname)-5s] [Path: {path_num}] [%(function_name)s]  %(message)-s', datefmt='%H:%M:%S')
    handler.setFormatter(formatter)

def log_runtime(t0):
    logger_set_path('TIME')
    t1 = dt.now()
    runtime = t1 - t0
    seconds = runtime.total_seconds()
    logger.debug(f'{seconds:.0f}s')

# Add the handler to the logger
logger.addHandler(handler)


