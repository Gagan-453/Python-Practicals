# importing ip_address from 
# ip address module 
from ipaddress import ip_address 

def IPAddress(IP: str) -> str: 
    return "Private" if (ip_address(IP).is_private) else "Public"
    
if __name__ == '__main__' : 

    # Public IP 
    print(IPAddress('216.58.196.67')) 

    # Private IP 
    print(IPAddress('202.83.16.167')) 

# GETTING PUBLIC IP ADDRESS
import publicip

publicip.get()