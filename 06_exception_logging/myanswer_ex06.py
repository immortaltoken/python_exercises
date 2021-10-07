from logging import getLogger, StreamHandler, DEBUG


def create_logger(name, log_level):
    """create logger"""
    logger = getLogger(name if name else __file__)
    handler = StreamHandler()
    handler.setLevel(log_level)
    logger.setLevel(log_level)
    logger.addHandler(handler)
    return logger


def main():
    """show how to handle and log the exception"""

    logger = create_logger("my_logger", DEBUG)
    logger.info("Now try to open file that does not exist!")

    #WRITE YOUR CODE HERE: below script will cause the Exception!
    try:
        with open("not_exist_file.txt") as f:
            lines = f.readlines()
    except IOError as identifier:
        logger.critical("You faced Exception! {}".format(identifier))


    #WRITE YOUR CODE HERE: handle the exception

if __name__ == "__main__":
    main()
