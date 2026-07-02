# Q1: Create a simple Block class with index, timestamp, data, previous_hash, and hash

import time
import hashlib

class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def __repr__(self):
        return f"Block(index={self.index}, timestamp={self.timestamp}, data={self.data}, previous_hash={self.previous_hash}, hash={self.hash})"
    
block = Block(1, "Sample Data", "0")
print(block)