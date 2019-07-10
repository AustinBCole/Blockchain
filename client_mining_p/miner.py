import hashlib
import requests
import time
import json
import sys

url = "http://localhost:5000/"
# TODO: Implement functionality to search for a proof 
def proof_of_work(last_proof):
    
    print("\nWe have started the proof of work process.\n")
    time_start = time.time()
    proof = 0
    while valid_proof(last_proof, proof) is False:
        proof += 1
    time_end = time.time()
    print("\nThe proof of work process is over\n")
    print(time_end - time_start)
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
        get_url = f"{url}lastproof"
        r = requests.get(url = get_url)
        data = r.json()
        last_proof = data['last_proof']
        new_proof = proof_of_work(last_proof)
        
        # TODO: When found, POST it to the server {"proof": new_proof}
        post_url = f"{url}mine"
        data = {
                'valid_proof': new_proof
                }
        request = requests.post(url = post_url, json = data)
        print(request.text)
        # TODO: If the server responds with 'New Block Forged'
        # add 1 to the number of coins mined and print it.  Otherwise,
        # print the message from the server.
