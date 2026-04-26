import socket
from datetime import datetime

def port_scanner(target, port_range):
    print(f"Scanning target: {target}")
    print(f"Time started: {datetime.now()}")

    try:
        # Loop through each port in the provided range
        for port in port_range:
            # Create a socket object (AF_INET = IPv4, SOCK_STREAM = TCP)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Set timeout to 1 second so it doesn't hang on closed ports
            s.settimeout(1)
            
            # Try to connect to the target and port
            # connect_ex returns 0 if the connection is successful
            result = s.connect_ex((target, port))
            
            if result == 0:
                print(f"Port {port}: Open")
            else:
                # You can uncomment this line if you want to see closed ports too
                # print(f"Port {port}: Closed")
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
    # Define your target and the ports you want to scan
    target_host = "127.0.0.1" 
    ports_to_scan = [8000] # Scans ports 1 to 100
    
    port_scanner(target_host, ports_to_scan)