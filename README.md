# Blockchain Implementation

### What's inside?
This repository contains, simple implementation of Blockchain structure
with the simple Flask backend for publishing purposes.

### What is 'Blockchain'?
A blockchain, originally block chain, is a growing list of records, 
called blocks, that are linked using cryptography. Each block contains 
a cryptographic hash of the previous block, a timestamp, and transaction 
data (generally represented as a Merkle tree).

By design, a blockchain is resistant to modification of its data. This 
is because once recorded, the data in any given block cannot be altered
retroactively without alteration of all subsequent blocks. For use as a
distributed ledger, a blockchain is typically managed by a peer-to-peer 
network collectively adhering to a protocol for inter-node communication
and validating new blocks.
[(Wikipedia Article about Blockchain)](https://en.wikipedia.org/wiki/Blockchain)

##### Sample Bitcoin structure
(Bitcoin is created with Blockchain systems. It is the first practical usage of Blockchain strcuture)
![Sample Bitcoin Structure](https://github.com/Egesabanci/blockchain/blob/master/images/blockchain_structure.png)