#!/usr/bin/env python3

import ipaddress as ip


class Router:
    """Класс для управления ip адресом и маршрутами"""

    def __init__(self, interface_name):
        """Метод для создания интерфейса, в качестве значения надо передать желаемое имя"""
        self.interface_name = interface_name
        self.interface_ip = None

    def add_ip_address(self, ip_address):
        """Метод для выставления ip адреса интерфейсу. Пример входного параметра: '192.168.0.1/24'"""
        self.interface_ip = ip.ip_interface(ip_address)
        self.gateway = self.interface_ip.ip
        self.route = {"0": (ip.ip_network(ip_address, False), self.gateway, self.interface_name)}

    def show_ip_address(self):
        """Метод для вывода информации об ip адресе интерфейса"""
        return f'Interface name = {self.interface_name},\nIP = {self.interface_ip}'

    def delete_ip_address(self):
        """Метод для удаления ip адреса у интерфейса"""
        self.interface_ip = None
        self.route.pop("0")

    def show_ip_routes(self):
        """Метод для вывода информации о существующих маршрутах"""
        routes = ""
        for key in self.route:
            routes = routes + f'{key} {self.route[key][0]} via {self.route[key][1]} dev {self.route[key][2]}\n'
        return routes

    def add_ip_route(self, destination_net, gate_for_route):
        """Метод для добавления новых маршрутов. Пример входных параметров: '192.168.0.0/24','192.168.0.1' """
        gate = ip.ip_address(gate_for_route)
        for key in list(self.route):
            if gate in self.route[key][0]:
                self.route[len(self.route)] = (ip.ip_network(destination_net, False), gate_for_route, self.interface_name)
                break
        else:
            raise Exception("Указанный gateway не доступен ни через один из существующих маршрутов")

    def delete_ip_route(self, destination_net):
        """Метод для удаления маршрута. Пример входного параметра: '192.168.0.0/24'"""
        for key in list(self.route):
            if destination_net == str(self.route[key][0]):
                self.route.pop(key)



if __name__ == "__main__":
    a = Router("eth0")
    a.add_ip_address("192.168.0.100/24")
    print(a.show_ip_routes())
    a.add_ip_route("172.16.0.0/24", "192.168.0.120")
    print(a.show_ip_routes())
    a.add_ip_route("10.10.10.0/24", "172.16.0.3")
    print(a.show_ip_routes())
    a.delete_ip_route("172.16.0.0/24")
    print(a.show_ip_routes())
