import logging

logger = logging.getLogger("my_cli_app")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("app.log")
file_handler.setLevel(logging.INFO)

console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

file_formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(filename)s:%(lineno)d - %(message)s")
file_handler.setFormatter(file_formatter)

console_formatter = logging.Formatter("%(message)s")
console_handler.setFormatter(console_formatter)

if not logger.handlers:
  logger.addHandler(file_handler)
  logger.addHandler(console_handler)