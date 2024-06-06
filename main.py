import nacl.public
from flask import Flask, request

app = Flask(__name__)

def generate_keypair() -> tuple[str]:
    # *Генерация ключевой пары*
    private_key = nacl.public.PrivateKey.generate()
    public_key = private_key.public_key

    # *Преобразование ключей в строковый формат*
    private_key_str = private_key.encode(encoder=nacl.encoding.Base64Encoder).decode('utf-8')
    public_key_str = public_key.encode(encoder=nacl.encoding.Base64Encoder).decode('utf-8')
    return (private_key_str, public_key_str)

@app.route('/')
def hello_world():
    keypair = generate_keypair()
    # dnses = ""
    local_address = request.args.get(key = "local_address", default = "")
    dns = request.args.get(key = "dns", default = "")
    # dns2 = request.args.get(key = "dns2", default = "")
    endpoint = request.args.get(key = "endpoint", default = "")
    server_pubkey = request.args.get(key = "server_pubkey", default = "")
    allowed_ips = request.args.get(key = "allowed_ips", default = "")

    if not all([
        local_address,
        dns,
        endpoint,
        server_pubkey,
        allowed_ips
    ]):
        return "not enough args ._.<br><br>example GET request with args: <b>/?local_address=1.2.3.4&dns=8.8.8.8,8.8.4.4&endpoint=228.14.88.0&server_pubkey=ADmkdlsnghklsnklsdnlkh=&allowed_ips=192.168.0.0/24,127.0.0.1</b>"
    
    # if all([dns1, dns2]):
    #     dnses = f"{dns1}, {dns2}"
    # else:
    #     dnses = dns1

    return \
        f"""
[Interface]
# public key = {keypair[1]}
PrivateKey = {keypair[0]}
ListenPort = 51820
Address = {local_address}
DNS = {dns}

[Peer]
PublicKey = {server_pubkey}
AllowedIPs = {allowed_ips}
Endpoint = {endpoint}
        """.replace("\n", "<br>")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8055)
    # print(generate_keypair())