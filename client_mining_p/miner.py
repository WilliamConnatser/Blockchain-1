#!/usr/bin/env python3
import hashlib
import requests
import json

import sys


# TODO: Implement functionality to search for a proof 

def valid_proof(block_string, proof):
    """
    Validates the Proof:  Does hash(block_string, proof) contain 6
    leading zeroes?
    """
    guess = f'{block_string}{proof}'.encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:6] == "000000"

if __name__ == '__main__':
    # What node are we interacting with?
    if len(sys.argv) > 1:
        node = sys.argv[1]
    else:
        node = "http://localhost:5000"

    coins_mined = 0
    # Run forever until interrupted
    while True:
        # TODO: Get the last proof from the server and look for a new one
        # We run the proof of work algorithm to get the next proof...
        response = requests.get(f'{node}/last_block')
        json_response = response.json()
        last_block = json_response['last_block']
        
        """
        Find a number p such that hash(last_block_string, p) contains 6 leading
        zeroes
        """
        block_string = json.dumps(last_block, sort_keys=True).encode()
        proof = 0
        while valid_proof(block_string, proof) is False:
            proof += 1
        
        
        submission = requests.post(f'{node}/mine',data={'proof': proof})
        coins_mined += 1
        print(f'\n \U0001F4B0\U0001F4B0\U0001F4B0 Coins Mined = {coins_mined} \n')
        pass
