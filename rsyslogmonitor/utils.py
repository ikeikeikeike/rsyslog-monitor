import time


def modify_message(message):
    return message.lower()


def follow(thefile):
    """ Go to the end of the file """
    thefile.seek(0, 2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.3)
            continue
        yield line.strip()


# vim: set et fenc=utf-8 ft=python ff=unix sts=4 sw=4 ts=4 :
