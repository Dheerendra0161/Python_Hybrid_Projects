import os
import logging
from logging.handlers import RotatingFileHandler


class LoggerCustom:
    _loggers = {}

    def __init__(self, log_dir="../loggers"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def setup_logger(self, log_file, max_bytes, backup_count,
                     log_level=logging.DEBUG,mode='a'):  # determines how many of these rotated log files to retain
        # Check if logger with log_file name already exists
        if log_file in LoggerCustom._loggers:
            return LoggerCustom._loggers[log_file]

        # Configure logging
        logging.basicConfig(level=log_level,
                            format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')

        # Create console handler
        # console_handler = logging.StreamHandler()
        # console_handler.setLevel(log_level)
        # console_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s',
        #                                       datefmt='%d/%m/%Y %I:%M:%S %p')
        # console_handler.setFormatter(console_formatter)
        # Create rotating file handler
        handler = RotatingFileHandler(os.path.join(self.log_dir, log_file), maxBytes=max_bytes,
                                      backupCount=backup_count)
        handler.setLevel(log_level)
        file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
        handler.setFormatter(file_formatter)

        # Get the logger for this page
        logger = logging.getLogger(log_file)
        logger.setLevel(log_level)  # Set logger level
        # logger.addHandler(console_handler)  # Add console handler to logger
        logger.addHandler(handler)  # Add rotating file handler to logger
        return logger
