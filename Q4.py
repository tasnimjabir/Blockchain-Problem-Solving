# Q4: Create a Genesis Block (the first block of the chain, whose previous_hash is "0")

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
        return hashlib.sha256(block_content.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "Genesis Block", "0")

genesis = create_genesis_block()
print("Index        :", genesis.index)
print("Data         :", genesis.data)
print("Previous Hash:", genesis.previous_hash)  # "0"
print("Hash         :", genesis.hash)