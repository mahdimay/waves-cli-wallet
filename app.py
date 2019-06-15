import pywaves as pw
import random
import sys

def generateWallet():
    alphabets = ['A', 'a', 'B', 'b', 'C', 'c', 'D', 'd', 'E', 'e', 'F', 'f' 'G', 'g', 'H', 'h', 'I', 'i', 'J', 'j', 'K', 'k', 'L', 'l', 'M', 'm', 'N', 'n', 'O', 'o', 'P', 'p', 'Q', 'q', 'R', 'r', 'S', 's', 'T', 't', 'U', 'u', 'V', 'v', 'W', 'w', 'X', 'x', 'Y', 'y', 'Z', 'z']
    seed = ""
    for i in range(15):
        length = random.randint(4, 8)
        word = ""
        for x in range (length):
            num = random.randint(0,50)
            seed += alphabets[num]
            word += alphabets[num]
        print (word)
        if (i != 14):
            seed += " "
    return pw.Address(seed=seed)

def optionCheck(option):
    if option == '1':
        print("Here's is your account information (WRITE THESE INFORMATION DOWN!!!): \n")
        print (generateWallet())

    if option == '2':
        seed = input("Please enter your seed (space between words): ")
        recipient = input("\n Enter the recepient address: ")
        amount = int(input("\n Enther the amount: "))
        attachment = input("\n Enter the attachment: ")
        pw.Address(seed=seed).sendWaves(recipient, amount, attachment=attachment, timestamp=0)
    if option == '3':
        seed = input("Please enter your seed (space between words): ")
        recipient = input("\n Enter the recepient address: ")
        asset = pw.Asset(input("\n Enter the asset ID: "))
        amount = int(input("\n Enther the amount: "))
        attachment = input("\n Enter the attachment: ")
        pw.Address(seed=seed).sendAsset(recipient, asset, amount, attachment=attachment, timestamp=0)
    if option == '4':
        seed = input("\nPlease enter your seed (space between words): ")
        print("\nSend waves or other tokens to the address below: \n")
        print(pw.Address(seed=seed).address)
    if option == '5':
        sys.exit(0)
print("\/\/\/\/ WAVES CLI WALLET \/\/\/\/ \n OPTIONS: \n \t 1. Generate New Wallet \n \t 2. Send Waves \n \t 3. Send Tokens \n \t 4. Receive Assets \n \t 5. Quit")
while True:
    option = input("\n \n \n Your selection (1, 2, 3, 4, 5): ")
    optionCheck(option)
