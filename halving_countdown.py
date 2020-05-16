import requests
import telepot
import time

token="" #insert bot token here
channel="" #destination channel numeric id Ex. -100xxxxxxxxxxx

old=0
block=0
halvingBlock=630000
rocket=u'\U0001F680'
customMessage="https://www.youtube.com/watch?v=PDJLvF1dUek" #Text, url etc.

bot=telepot.Bot(token=token)


while (block < (halvingBlock+2)):
    r=r = requests.get('https://blockchain.info/q/getblockcount')
    block=int(r.text)
    print (str(block))
    less=block-halvingBlock
    if old!=block:
        if less<0:
            txt="Block " + str(block) + " mined!\n\n" + str(abs(less)) + " blocks to Halving!" 
            print (txt)
            try:
                bot.sendMessage(channel, text=txt, parse_mode= 'HTML') #Send message
            except Exception as e:
                print("Error:\n" + str(e))
        if block==halvingBlock:  
            txt=rocket + rocket + rocket + rocket + rocket + rocket + "\n\nBlock " + str(block) + " mined!\n\n Happy Halving!\n\n" + rocket + rocket + rocket + rocket + rocket + rocket + "\n\n" + customMessage
            try:
                bot.sendMessage(channel, text=txt, parse_mode= 'HTML') #Send message
            except Exception as e:
                print("Error:\n" + str(e))
    old=block
    time.sleep(abs(less)+2)