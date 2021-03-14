from psutil import process_iter
from os import system
from time import sleep


def get_active_connections(process):
    connections = [x.raddr[0] for x in process if x.raddr]
    if not connections:
        return
    return connections


def refresh_ip_addresses(connections):
    system("cls")
    print()
    print(f" IP addresses:")
    print("    " + "\n    ".join(ip for ip in connections))
    print("    ...")


def main():
    system("title AnyDesk IP resolver")
    system("color a")
    system("mode 40,20")
    print()
    processes = [p for p in process_iter() if "AnyD" in p.name()]
    if not processes:
        print(" Unable to find an AnyDesk instance")
        system("pause>nul")
        return 1

    connections = []
    try:
        while True:
            AnyDesk = [process.connections() for process in processes if process.connections(kind="tcp")]
            if AnyDesk:
                new_connections = get_active_connections(AnyDesk[0])
                for ip_address in new_connections:
                    if ip_address not in connections:
                        connections.append(ip_address)
                refresh_ip_addresses(connections)
            sleep(2.5)
    except KeyboardInterrupt:
        print(" Stopped listening for new connections")
        system("pause>nul")


if __name__ == "__main__":
    main()
