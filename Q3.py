# Q3: Prove that changing one character in the block's data completely changes the hash (avalanche effect)

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


def hash_of(data):
    content = "1" + "1700000000.0" + data + "0"
    return hashlib.sha256(content.encode()).hexdigest()

hash1 = hash_of("Send 5 BTC to Fahim")
hash2 = hash_of("Send 6 BTC to Fahim")  # only "5" -> "6", a single character

print("Data 1 hash:", hash1)
print("Data 2 hash:", hash2)
print("Are they equal? ", hash1 == hash2)

diff = sum(1 for a, b in zip(hash1, hash2) if a != b)
print(f"Different characters: {diff} out of 64")