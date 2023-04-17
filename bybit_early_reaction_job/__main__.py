import logging.config

from bybit_early_reaction_job.bybit_early_reaction_job import BybitEarlyReactionJob
from bybit_early_reaction_job.constants import LOGGER_CONFIG_FILE_PATH, CONFIG_FILE_PATH, __logo__
from bybit_early_reaction_job.utils import load_config

if __name__ == "__main__":
    logging.config.fileConfig(fname=LOGGER_CONFIG_FILE_PATH, disable_existing_loggers=False)
    logging.info(__logo__)

    try:
        config = load_config(CONFIG_FILE_PATH)

        job = BybitEarlyReactionJob(config)
        job.run()
    except:
        logging.exception("Error in app: ")
