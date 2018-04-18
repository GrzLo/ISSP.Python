import requests
import netaddr
import dns.resolver

# import listy adresow z pliku, w przykladowym pliku sa 2 adresy 156.17.4.0/24 oraz 156.17.86.0/24
with open('ip_networks', 'r') as ipNetworkFile:
    ipNetworkArray = [netaddr.IPNetwork(i) for i in ipNetworkFile.readlines()]

for ipNetwork in ipNetworkArray:
    # ponizsza linijka sluzy uzyskaniu informacji z rekordu SOA dns
    soaAnswers = dns.resolver.query(ipNetwork.cidr.network.reverse_dns.strip('0.'), 'SOA')
    # wyluskanie danych dotyczacych maila -> zamiana '.' na '@'
    email = str([rdata.rname for rdata in soaAnswers][0]).replace('.', '@', 1)
    for i, ipAddress in enumerate(ipNetwork):
        ip = str(ipAddress)
        try:
            # wykorzystanie metody head w celu sprawdzenia czy na danym IP postawiony jest serwer www
            # timeout ustawiony na 0.5s, ciezko okreslic jaka jest rozsadna bezpieczna wartosc
            request = requests.head('http://' + str(ip), timeout=0.5)
        except requests.exceptions.RequestException:
            # jesli nie udalo sie nawiazac polaczenia to przejdz do nastepnego adresu
            pass
        else:
            try:
                # ustalenie domeny/domen dla danego IP
                reversedDns = dns.resolver.query(ipAddress.reverse_dns, 'PTR')
                domains = [str(i)[:-1] for i in reversedDns]
            except dns.exception.DNSException:
                # jezeli serwer www nie ma domeny to uzyj po prostu adresu IP
                domains = [ip]
            # uporzadkowanie wszystkich danych (nazwa domeny/domen, adres IP:port, typ serwera, email z reokrdu SOA)
            output = domains
            output.extend([ip + ":80", str(request.headers.get('Server')), email])
            print(';'.join(output))
