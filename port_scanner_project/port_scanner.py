import socket
from datetime import datetime

def port_scanner(target, port_range):
    print(f"Scanning target: {target}")
    print(f"Time started: {datetime.now()}")

    try:
        for port in port_range:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            result = s.connect_ex((target, port))
            if result == 0:
                print(f"Port {port}: Open")
            else:
                pass  
            s.close()  
    except KeyboardInterrupt:
        print("\nExiting Program.")
    except socket.gaierror:
        print("\nHostname could not be resolved.")
    except socket.error:
        print("\nCould not connect to server.")
    print(f"Time finished: {datetime.now()}")

if __name__ == "__main__":
    target_host = "127.0.0.1" 
    ports_to_scan = [8000] 
    port_scanner(target_host, ports_to_scan)
