class Connect:
    def __init__(self, unit_name, mac_address, ip_address, login, password):
        self.unit_name = unit_name
        self.mac_address = mac_address
        self.ip_address = ip_address
        self.login = login
        self.password = password

    @property
    def unit_name(self):
        return self.unit_name
    @unit_name.setter
    def unit_name(self, value):
        self.unit_name = value
    @unit_name.deleter
    def unit_name(self):
        del self.unit_name

    @property
    def mac_address(self):
        return self.mac_address
    @mac_address.setter
    def mac_address(self, value):
        self.mac_address = value
    @mac_address.deleter
    def mac_address(self):
        del self.mac_address

    @property
    def ip_address(self):
        return self.ip_address
    @ip_address.setter
    def ip_address(self, value):
        self.ip_address = value
    @ip_address.deleter
    def ip_address(self):
        del self.ip_address
