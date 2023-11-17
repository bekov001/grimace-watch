import requests



WEI = 1000000000000000000

def get_grimace_balance(address):
    def get_token_amount(api_endpoint, token, address):
        url = f"{api_endpoint}?module=account&action=tokenbalance&contractaddress={token}&address={address}"
        response = requests.get(url)
        print(response.text)
        data = response.json()
        return data['result']

    api_endpoint = 'https://explorer.dogechain.dog/api'
    token = '0x2f90907fd1dc1b7a484b6f31ddf012328c2bab28'
    amount = get_token_amount(api_endpoint, token, address)
    return float(amount) / WEI


# from web3 import Web3

# infura_url = ' https://explorer.dogechain.dog/api/eth-rpc '
# web3 = Web3(Web3.HTTPProvider(infura_url))

# # ERC20 Token Contract ABI
# abi = """[{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"type":"function"}]"""

# Replace 'Your_Token_Contract_Address' and 'Your_Address' with actual values
# contract_address = Web3.to_checksum_address('0x2f90907fd1dc1b7a484b6f31ddf012328c2bab28')
# wallet_address = '30031087c042cbb5607c7c687b8b831427daf35ef3c011a805bb6a2d17730083'

# contract = web3.eth.contract(address=contract_address)
# token_balance = contract.functions.balanceOf(wallet_address).call()

# print(f"The amount of tokens in the address is {token_balance}")
