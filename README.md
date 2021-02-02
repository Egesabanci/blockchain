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

##### Sample Bitcoin structure (Created with Blockchain infastructure)
![Sample Bitcoin Structure](https://github.com/Egesabanci/blockchain/blob/master/images/bitcoin_structure.png)

### Installation
Firstly, clone this repository with the following command and go into it:
```
>>> git clone https://github.com/Egesabanci/blockchain
>>> cd blockchain
```

After cloning, create virtual environment with the following commands:
```
>>> virtualenv .
>>> cd Scripts
>>> activate
>>> cd .. 
```

**If there is an error**, you probably don't have a `virtualenv` package.
Download `virtualenv` with the command below and try the previous commands again:
```
>>> pip install virtualenv
```

Install required packages:
```
>>> cd build
>>> pip install -r requirements.txt
>>> cd ..
```

### Run the server
**NOTE** make sure you are in the base folder (`blockchain`)
You can run the server on `localhost` with following command:
```
python run.py
```
Also, you can specify the options from `src/config.yml` file.
Config file looks like this:
```yaml
config:
    port: 8080
    host: 127.0.0.1
    debug: True
    db_name: "blockchain.db"
    track_modifications: True
```
`port`: `localhost` port for running the server
`host`: host specification
`debug`: debug mode specification for Flask environment
`db_name`: database name specification
`track_modifications`: database option for `SQLAlchemy` database