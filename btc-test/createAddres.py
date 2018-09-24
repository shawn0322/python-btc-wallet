# create_btc_wallet.py

from pywallet import wallet

import sqlite3

conn = sqlite3.connect("/home/gaoxun/sqlite/btc-hot-wallet.db")  #创建sqlite.db数据库

def create(password=None,coinType=None,network="btctest",number=1):

    '''create main wallet'''
    # generate 12 word mnemonic seed
    seed = wallet.generate_mnemonic()
    # create bitcoin wallet
    w = wallet.create_wallet(network=network, seed=seed, children=1)

    statement = "INSERT INTO account VALUES(?,?,?,?,?,?)"
    data = [(1,"main", w['address'], w['private_key'], coinType,seed)]
    conn.executemany(statement, data)
    conn.commit()

    WALLET_PUBKEY = w['xpublic_key']
    print(WALLET_PUBKEY)


    for index in range(number):
        print(index)
        child_id = wallet.generate_child_id()
        # generate address for specific user (id = 10)
        user_addr = wallet.create_address(network=network, xpub=WALLET_PUBKEY, child=child_id)

        statement = "INSERT INTO account VALUES(?,?,?,?,?,?)"
        data = [(index+2, "child", user_addr['address'], None, coinType, None)]
        conn.executemany(statement, data)
        conn.commit()

        print("User Address\n", user_addr)

        print("============================")