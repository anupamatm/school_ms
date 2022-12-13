import logging
logging.basicConfig(filename="log_msg.log", format=' %(asctime)s  %(message)s' , filemode='w')
# logger=logging.getLogger()
# logger.setLevel(logging.DEBUG)

a=10
b=0
try:
    c=a/b
except Exception as e:
    logging.error("exeption occured",exc_info=True)

# logging.debug("the debug message is displaying")
# logging.info("the info message is displaying")
# logging.warning("the warning message is displaying")
# logging.error("the error message is displaying")
# logging.critical("the critical message is displaying")
