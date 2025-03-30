import hashlib
import json
from time import time
from uuid import uuid4

class Blockchain:
    def __init__(self):
        self.chain = []
        self.current_votes = []
        self.voters = set()
        self.candidates = {"Candidate A": 0, "Candidate B": 0, "Candidate C": 0}
        
        # Create genesis block
        self.new_block(previous_hash='1', proof=100)

    def new_block(self, proof, previous_hash=None):
        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'votes': self.current_votes,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        
        self.current_votes = []
        self.chain.append(block)
        return block

    def new_vote(self, voter_id, candidate):
        if voter_id in self.voters:
            return False
        
        self.voters.add(voter_id)
        self.current_votes.append({
            'voter_id': hashlib.sha256(voter_id.encode()).hexdigest(),
            'candidate': candidate
        })
        
        # Update candidate count
        if candidate in self.candidates:
            self.candidates[candidate] += 1
        
        return True

    @staticmethod
    def hash(block):
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1
        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"
