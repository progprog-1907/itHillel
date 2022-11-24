"""У вас есть список(list) IP адресов. Вам необходимо создать
класс, который сможет:
1) Получить и изменить список IP адресов
2) Получить список IP адресов в развернутом виде
(10.11.12.13 -> 13.12.11.10)
3) Получить список IP адресов без первых октетов
(10.11.12.13 -> 11.12.13)
4) Получить список последних октетов IP адресов
(10.11.12.13 -> 13)"""


class IpHandler:
    """Handles a list of IPs, each IP must be a string"""

    def __init__(self, ipList):
        self._ipList = ipList

    @property
    def ipList(self):
        return self._ipList

    @ipList.setter
    def ipList(self, newList):
        self._ipList = newList

    def reverse_IP(self):
        """Return it is IPs reversed"""
        reverse = self._ipList.split(".")
        reverse.reverse()
        return ".".join(reverse)

    def get_oct_1_3(self):
        """Returns a list of IPs without first octets (127.0.0.1 -> .0.0.1)"""
        without_first_octets = self._ipList[self._ipList.find(".")::]
        return without_first_octets

    def get_oct_3(self):
        """Returns a list of last octets of each IP (127.0.0.1 -> .1)"""
        last_octets = self._ipList[self._ipList.rfind(".")::]
        return last_octets