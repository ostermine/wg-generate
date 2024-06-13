# wg-generate
## wireguard generate clients config
----
### How to start?
- If u have docker with docker-compose: `docker compose up -d`
- Or: `pip install -r requirements.txt` `python main.py`
- Then go to `http://localhost:8055`
----
- Example of using:
  - Generate config file: `curl -X GET "YOURSITE.COM/?local_address=1.2.3.4&dns=8.8.8.8,8.8.4.4&endpoint=228.14.88.0&server_pubkey=ADmkdlsnghklsnklsdnlkh=&allowed_ips=192.168.0.0/24,127.0.0.1&interface=wg-clients" > vpn123.conf`

  - Generate QR code: `curl -X GET "YOURSITE.COM/?local_address=1.2.3.4&dns=8.8.8.8,8.8.4.4&endpoint=228.14.88.0&server_pubkey=ADmkdlsnghklsnklsdnlkh=&allowed_ips=192.168.0.0/24,127.0.0.1&interface=wg-clients" | curl -F-=\<- qrenco.de`
- Example out:
```
# /interface wireguard peer add public-key="d70LEN7123wBjdA0F5xhk=" interface=wg-clients allowed-address=172.16.1.25/32 persistent-keepalive=1m
[Interface]
PrivateKey = HONY3ahbMNW253a0fduSrYdubc=
ListenPort = 51820
Address = 172.16.1.25/32
DNS = 172.16.1.1,8.8.8.8

[Peer]
PublicKey = GxiJvk8TJKD112DoZFdJ6mUzzW0=
AllowedIPs = 0.0.0.0/0
Endpoint = 1.2.3.4:51800
```

----
## WHY?
- I needs to fast generate good config between client and Mikrotik (mikrotik's cant normal to generate clients configs)
