import configparser


class ConfHost:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("./config/host.ini")
        self.host = config["host"]

    def get_host_conf(self):
        return self.host


if __name__ == "__main__":
    host = ConfHost()

