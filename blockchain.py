# Initializing our blockchain list
genesis_block = {
    'previous_hash': '', 
    'index' : 0, 
    'transactions' : []
}
blockchain = [genesis_block]
open_transactions = []
owner = 'mitch'
participant = {'mitch'}

def get_last_blockchain_value():
    """ Return the last value of the current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transaction(recipient, sender=owner, amount=1.0):
    """Append a new value as well as the last blockchain value to the blockchain

    Arguments:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amout of coins sent (default = 1.0)
    """
    transactions = {
        'sender': sender, 
        'recipient' : recipient, 
        'amount' : amount
        }
    open_transactions.append(transactions)
    participant.add(sender)
    participant.add(recipient)

        
def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    for keys in last_block:
        value = last_block[keys]
        hashed_block = hashed_block
    #print(hashed_block)
        
    block = {
        'previous_hash': hashed_block, 
        'index' : len(blockchain), 
        'transactions' : open_transactions
    }
    blockchain.append(block)
    return True


def hash_block(last_block): 
    return '_'.join([str(last_block[key]) for key in last_block])


def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain]
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent += tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received += tx[0]
    return amount_received - amount_sent

def get_transaction_value():
    """Get the user input as a float number value"""
    tx_recipient = input('Enter the recipient of the transaction:')
    tx_amount = float(input('Your transaction amount please: '))
    return (tx_recipient, tx_amount)

def get_user_choice():
    user_input = input('Your choice: ')
    return user_input

#Output the blockchain list to the console
def print_blochain_elements():
    """ Print each block of the blockchain """
    for block in blockchain:
        print('Outputting Block')
        print(block)


def verify_chain():
    """ Verify the current blockchain and return True if it's valid, False if not"""
    for (index,block) in enumerate(blockchain):
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index -1]):
            return False
    return True
    
        
waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participant')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transaction_value()
        recipient, amount = tx_data
        # Add the transaction amount to the blockchain
        add_transaction(recipient,amount=amount)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
    elif user_choice == '3':
        print_blochain_elements()
    elif user_choice == '4':
        print(participant)
    elif user_choice == 'h':
        if len(blockchain) >=1:
            blockchain[0] = {
                'previous_hash': '', 
                'index' : 0, 
                'transactions' : [{'sender': 'Chris','recipient': 'Max', 'amount': 100}]
            }
    elif user_choice == 'q':
        # Loop exit
        waiting_for_input = False
    else: 
        print('Invalid input')
    if not verify_chain():
        print_blochain_elements()
        print('Invalid blockchain!')
        break
    print( get_balance('mitch'))
else:
    print("user left")

