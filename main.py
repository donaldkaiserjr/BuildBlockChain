#blockchains consists of blockchains
#blocks consists of transactions
# blocks are connected through hashing. 
# Each block has a unique fingerprint (a hash) 
        # It's based on transactions in that block and on previous blocks
        # If you change a transaction way back in the blockchain, it'll affect
        #all hashes going forward

from Block import Block

blockchain = []


#genesis block doesn't have a hash since it's the first block
# so this previous hash (text) is just b.s. text
genesis_block = Block("Chancellor on the brink...", ["Satoshi sent 1 BTC to Ivan",
                                                        "Maria sent 5 BTC to Jenny",
                                                        "Satoshi sent 5 BTC to Hal Finney"])


second_block = Block(genesis_block.block_hash, ["Ivan sent 5 BTC to Liz",
                                                "John sent 5 BTC to Jenny"])

third_block = Block(genesis_block.block_hash, ["A to C 5 BTC", "G to D 4 BTC"])

print(second_block.block_hash)
