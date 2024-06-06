# wg-generate
## wireguard generate clients config
----
### How to start?
- If u have docker with docker-compose: `docker compose up -d`
- Or: `pip install -r requirements.txt` `python main.py`
----
- Example of using: `YOURSITE.COM/?local_address=1.2.3.4&dns=8.8.8.8,8.8.4.4&endpoint=228.14.88.0&server_pubkey=ADmkdlsnghklsnklsdnlkh=&allowed_ips=192.168.0.0/24,127.0.0.1`
----
## WHY?
- I needs to fast generate good config between client and Mikrotik (mikrotik's cant normal to generate clients configs)
