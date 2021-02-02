# Blockchain Implementation

### **What's inside?**
This repository contains, simple implementation of Blockchain structure
with the Flask backend for publishing purposes.

### **What is 'Blockchain'?**
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

##### **Sample Bitcoin structure** (Created with Blockchain infastructure)
![Sample Bitcoin Structure](https://github.com/Egesabanci/blockchain/blob/master/images/bitcoin_structure.png)

### **Installation**
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

### **Run the server**
You can run the server on `localhost` with following command
(Make sure you are in the base folder `blockchain`):
```
>>> python run.py
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

### **Usage**
**Use on browser:**    
After running the server, you can go to the `localhost` link (default: `http://127.0.0.1:8080/`) and use it with a simple graphical interface:  
![Web Browser GUI](https://github.com/Egesabanci/blockchain/blob/master/images/example.png)

**Use from command-line:**    
You can also, use it from command-line with some simple commands
(Make sure you are in the base folder `blockchain`):

**Adding new blocks to the chain:**  
```
>>> python add.py
```
This command adds a new block with default data (Default data: `"No Data."`)  
You can specify the data that you want to attach to the block, you can use the `--data` flag:
```
>>> python add.py --data "Some data for my block"
```

**Get information from chain:**   
There are some flags for getting information from chain:    
`num_blocks`: returns number of blocks of the chain  
`final_id`: returns the last block's ID  
`final_hash`: returns the last block's hash  
`final_data`: returns the data of the last block  
`final_date`: returns the creation time of the last block  
`genesis_hash`: returns the genesis block's hash  
`genesis_date`: returns the creation time of the genesis block  

Example for getting information:
```
>>> python info.py --num_blocks --final_hash
```
This command returns `number of blocks` and `last block's hash`