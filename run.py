import requests
import multiprocessing
import random
from rich import print
from rich.panel import Panel
from rich.console import Console
from hdwallet import HDWallet
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet as Cryptocurrency
from hdwallet.utils import is_mnemonic
from mnemonic import Mnemonic
from multiprocessing import Process

console = Console()

with open('list.txt', 'r', encoding="utf8") as f:
    listt = [s.strip() for s in f.readlines()]

def hack() :
    z = 1
    w = 0
    while True :
        z += 1
        api = random.choice(listt)
        langrnd = ['english']
        sellan = random.choice(langrnd)
        mne = Mnemonic(str(sellan))
        listno = ["128" , "256"]
        rnd = random.choice(listno)
        words = mne.generate(strength = int(rnd))
        STRENGTH = int(rnd)
        LANGUAGE: str = (sellan)
        MNEMONIC = words
        PASSPHRASE: str = None
        assert is_mnemonic(mnemonic = words , language = sellan)

        bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency = Cryptocurrency , account = 0 , change = False ,
                                                      address = 0)
        bip44_hdwallet.from_mnemonic(mnemonic = MNEMONIC , passphrase = PASSPHRASE , language = LANGUAGE)
        mixword = words[:32]
        addr = bip44_hdwallet.p2pkh_address()
        priv = bip44_hdwallet.private_key()

        # =======================================

        z += 1
        try:
            url = 'https://api.ethplorer.io/getAddressInfo/' + addr + '?apiKey=' + api
            amount = requests.get(url).json()['ETH']['balance']
            #print('Total Scan Checking -----  =', str(z*40), 'Address --- =', addr , 'Amout --- = ', amount, end='\r')
            if (amount > 0) :
                w += 1
                f1 = open('WalletWinner.txt' , 'a')
                f1.write(f'\nAddress     === {addr}')
                #f1.write(f'\nPrivateKey  === {priv}')
                #f1.write(f'\nMnemonic    === {words}')
                #f1.write(f'\nBalance === {amount}')
                #f1.write(f'\n            -------[ Nhat Vuong ]------                   \n')
                f1.close()
        except:
            continue

        # ============================


processes = []
for i in range(40): 
    p = multiprocessing.Process(target = hack)
    if __name__ == '__main__' :
        p.start()
        processes.append(p)
for p in processes:
    p.join()