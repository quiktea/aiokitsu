from datetime import datetime

def log_as_client(msg : str, sub_msg : str = None):
    if sub_msg is None:
        print("[Kitsu Client] :: Logged :: {}".format(msg))
    else:
        print("[Kitsu Client] :: {} :: {}".format(sub_msg, msg))



class Runtime:
    def __init__(self):
        self.__start = None
        self.__end = None

    def start(self):
        self.__start = datetime.utcnow()

    def end(self):
        self.__end = datetime.utcnow()

    def calculate(self):
        delta_uptime = self.__end - self.__start
        hours, remainder = divmod(int(delta_uptime.total_seconds()), 3600)
        minutes, seconds = divmod(remainder, 60)
        days, hours = divmod(hours, 24)
        log_as_client(f"{days}d | {hours}h | {minutes}m | {seconds}s", "Runtime Calculation")
