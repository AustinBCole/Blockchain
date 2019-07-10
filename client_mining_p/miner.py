import hashlib
import requests
from threading import Timer

import sys

url = "http://localhost:5000"
# TODO: Implement functionality to search for a proof 
def proof_of_work():
    
    print("\nWe have started the proof of work process.\n")
    print(time.time())
    # Use GET requet to get proof of last block from the server
    r = requests.get(url = url)
    data = r.json()
    last_proof = data["last_proof"]
    
    proof = 0
    while self.valid_proof(last_proof, proof)is false:
        proof += 1
    print("\nThe proof of work process is over\n")
    print(time.time())
    return proof

def valid_proof(last_proof, proof):

    guess = f'{last_proof}{proof}'.encode()
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
        # TODO: When found, POST it to the server {"proof": new_proof}
        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
        pass
