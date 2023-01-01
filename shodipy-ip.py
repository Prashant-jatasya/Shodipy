import shodan
import sys
import colorama
import prettytable
import re
from tqdm import tqdm

# Initialize the colorama library to enable colored output on Windows
colorama.init()

# Prompt the user for an IP address
ip_address = input("Enter an IP address: ")

# Validate the IP address using a regular expression
pattern = r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
if not re.match(pattern, ip_address):
    print(colorama.Fore.RED + "Error: Invalid IP address")
    sys.exit()

# Set up the Shodan API client
api_key = "API KEY HERE"
api = shodan.Shodan(api_key)

try:
    # Search for information about the IP address
    with tqdm(desc="Searching", unit="ip") as pbar:
        host = api.host(ip_address)
        pbar.update()

    # Create a table to display the results
    table = prettytable.PrettyTable()
    table.field_names = ["Organization", "Operating System", "Port", "Banner"]
    table.add_row([colorama.Fore.GREEN + (host.get("org") or "unknown"), 
                   colorama.Fore.RED + (host.get("os") or "unknown"),
                   "",
                   ""])
    for item in host["data"]:
        table.add_row(["", "", item["port"], item["data"]])
    print(table)

except shodan.APIError as e:
    print(colorama.Fore.RED + "Error: {}".format(e))
