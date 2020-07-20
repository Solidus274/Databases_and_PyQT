import ipaddress
import subprocess
import platform
from tabulate import tabulate


def host_ping(host_list):
    for host in host_list.hosts():
        output = subprocess.run("ping -{} 1 {}".format('n' if platform.system().lower(
        ) == "windows" else 'c', host), stdout=subprocess.DEVNULL)
        if output.returncode == 0:
            print(f"Узел {host} доступен")
        else:
            print(f"Узел {host} недоступен")


def host_range_ping(ip_range):
    for ip in range(ip_range):
        host = f'192.168.5.{ip}'
        output = subprocess.run("ping -{} 1 {}".format('n' if platform.system().lower(
        ) == "windows" else 'c', host), stdout=subprocess.DEVNULL)
        if output.returncode == 0:
            print(f"Узел {host} доступен")
        else:
            print(f"Узел {host} недоступен")


def host_range_ping_tab(ip_range):
    columns_r = ['Reachable']
    columns_u = ['Unreachable']
    reachable_list = []
    unreachable_list = []

    for ip in range(ip_range):
        host = f'192.168.5.{ip}'
        output = subprocess.run("ping -{} 1 {}".format('n' if platform.system().lower(
        ) == "windows" else 'c', host), stdout=subprocess.DEVNULL)
        if output.returncode == 0:
            reachable_list.append(host)
        else:
            unreachable_list.append(host)
    print(tabulate(reachable_list, headers=columns_r))
    print(tabulate(unreachable_list, headers=columns_u))


ip_list = ipaddress.ip_network('192.168.5.0/28')
host_ping(ip_list)
host_range_ping(int(input('Введите верхнее значение ip адреса: ')) + 1)
host_range_ping_tab(int(input('Введите верхнее значение ip адреса: ')) + 1)
