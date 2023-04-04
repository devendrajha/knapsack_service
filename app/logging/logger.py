import logging
import logging.config

import app.config as cfg




def yield_logger() -> logging.Logger:
    """ """
    logging.config.fileConfig(cfg.LOGGER_CONFIG)
    return logging.getLogger(cfg.APP_NAME)
