# one time setup for logging
import logging
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log","a"))
def logger_decorator(func):
    def wrapper(*args, **kwargs):
        if args:
            positional_args = list(args)
        else:
            positional_args = "none"
        
        if kwargs:
            kw_params = dict(kwargs)
        else:
            kw_params = "none"
        
        logger.log(
            logging.INFO,
            f"function: {func.__name__} \n positional parameters: {positional_args}  \n keyword parameters: {kw_params}  \n return: {func(*args, **kwargs)} \n ********"
        )
        return func(*args, **kwargs)
    return wrapper


@logger_decorator
def hello_world():
    print("Hello, world!")
    return None

@logger_decorator
def args_1(*args):
    return True

@logger_decorator
def kwargs_1(**kwargs):
    return logger_decorator

hello_world()
args_1(75,92, "Jon Doe", 888)
kwargs_1(year="unknown", temp=28, sky="clear")