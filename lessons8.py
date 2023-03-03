
import logging
logging.basicConfig(level=logging.DEBUG)
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")

format="We have next logging message: "#

try:
    print(10/0)except Exception:
    logging.exception("Exception")
""">>> 
2+25"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()


    def adder(*args, **kwargs):
        result = 0


    for _ in args:        result += _
    for _ in kwargs.values():        result += _
    return result

