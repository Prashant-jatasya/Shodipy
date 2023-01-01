import shodan
from shodan import Shodan
import requests
from prettytable import PrettyTable

# Replace YOUR_API_KEY with your actual API key
api_key = "FyKjwfA8URdLrF4t6JBOiW0pcyy1o3eU"
api = Shodan(api_key)

# Get the API info
info = api.info()
print("API Info:")
print(f'Plan: {info["plan"]}')
print(f'Scan Credits: {info["scan_credits"]}')
print(f'Queries Left: {info["query_credits"]}')

# Prompt the user for a search query
query = input("Enter a search query: ")

# Perform the search
results = api.search(query)

# Create a table to display the results
table = PrettyTable()
table.field_names = ["IP", "Port", "Banner"]

# Add the results to the table
for result in results['matches']:
    table.add_row([result["ip_str"], result["port"], result["data"]])

# Display the table
print("\nSearch Results:")
print(f'Total Results: {results["total"]}')
print(table)

# Get the list of tags for the search query

# Perform the search and get the results
results = api.search(query)

# Extract the tags from the search results
tags = [match.get("tags", []) for match in results["matches"]]

# Flatten the list of tags
tags = [tag for sublist in tags for tag in sublist]

# Remove duplicates from the list of tags
tags = list(set(tags))

# Print the list of tags
print("\nTags:")
for tag in tags:
    print(tag)







# Get the list of services (ports) that Shodan crawls


# Extract the services from the search results
services = [match.get("name", "") + ": " + match.get("description", "") for match in results["matches"]]

# Remove duplicates from the list of services
services = list(set(services))

# Print the list of services
print("\nServices:")
for service in services:
    print(service)



# Get the list of protocols that Shodan crawls
# Get the list of protocols that Shodan crawls
protocols = api.protocols()

# Print the list of protocols
print("\nProtocols:")
for protocol in protocols:
    print(protocol)



# Look up an IP address
ip = "8.8.8.8"
host = api.host(ip)
print(f"\nHost Info: {ip}")
for key in host:
    print(f'{key}: {host[key]}')

# Get a list of all the IPs that Shodan is aware of
# Perform the search and get the results
results = api.search(query)

# Extract the IPs from the search results
ips = [match["ip_str"] for match in results["matches"]]

# Remove duplicates from the list of IPs
ips = list(set(ips))

# Print the list of IPs
print("\nIPs:")
for ip in ips:
    print(ip)


# Get a list of all the ASNs that Shodan is aware of

# Extract the ASNs from the search results
asns = [match["asn"] for match in results["matches"]]

# Remove duplicates from the list of ASNs
asns = list(set(asns))

# Print the list of ASNs
print("\nASNs:")
for asn in asns:
    print(asn)


# Create a table to display the results
table = PrettyTable()
table.field_names = ["IP", "Port", "Banner"]

# Display the table
print(table)

# Use the Shodan API to retrieve the IP addresses that have the most open ports
# Perform the search and get the results
results = api.search(query)

# Extract the IPs from the search results
ips = [match["ip_str"] for match in results["matches"]]

# Count the number of times each IP appears in the list
ip_counts = {}
for ip in ips:
    if ip in ip_counts:
        ip_counts[ip] += 1
    else:
        ip_counts[ip] = 1

# Sort the IPs by the number of open ports
sorted_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)

# Print the list of IPs
print("\nIPs with the most open ports:")
for ip, count in sorted_ips:
    print(f'{ip}: {count} open ports')




