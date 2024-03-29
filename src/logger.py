import logging
import logging.config
import yaml

def setup_logger():
    logging.basicConfig(filename='logs/app.log', format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)

with open('./conf/logging.yaml') as f:
    config_logging = yaml.load(f, Loader=yaml.FullLoader)
    logging.config.dictConfig(config_logging)
    logger = logging.getLogger('app')

logger = logging.getLogger(__name__)

