# Q2: Write a function that calculates a block's hash using SHA-256 from all its fields

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
        block_content = (
            str(self.index)
            + str(self.timestamp)
            + str(self.data)
            + str(self.previous_hash)
        )
        encoded_content = block_content.encode()
        sha = hashlib.sha256(encoded_content)
        return sha.hexdigest()


# Quick test
block = Block(1, "Send 5 BTC to Fahim", "abc123")
print("Hash        :", block.hash)
print("Hash length :", len(block.hash))  # Always 64 characters for SHA-256