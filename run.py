import os
import random

#dropout = 0.66
#emsize = 600
#lr = 35
#nhid = 600
#nlayers = 3

def runrandom():
    cliplist = []
    for i in range(1,81):
        cliplist.append(i/100)
    nhidlist = []
    for i in range(1,21):
        nhidlist.append(i*100)
    emsizelist = []
    for i in range(10,81):
        emsizelist.append(i*10)
    lrlist = []
    for i in range(1,21):
        lrlist.append(i*5)
    dropoutlist = []
    for i in range(5,50):
        dropoutlist.append((i*2)/100)
        
    delist = []
    for i in range(0,65,5):
        delist.append(i/100)
    de = random.choice(delist)
    
    dhlist = []
    for i in range(0,10,1):
        dhlist.append(i/10)
    dh = random.choice(dhlist)
    
    dilist = []
    for i in range(0,100,10):
        dilist.append(i/100)
    di = random.choice(dilist)
    
    wdlist = []
    for i in range(0,11,2):
        wdlist.append(i/10)
    wd = random.choice(wdlist)

    alphlist = []
    for i in range(0,50,5):
        alphlist.append(i/10)
    alph = random.choice(alphlist)
    
    betlist = []
    for i in range(0,50,5):
        betlist.append(i/10)
    bet = random.choice(betlist)
    
    optlist =['sgd','adam']
    opt = random.choice(optlist)

    clip = random.choice(cliplist)
    dropout = random.choice(dropoutlist)
    lr = random.choice(lrlist)
    nhid = random.choice(nhidlist)
    emsize = random.choice(emsizelist)
    command = 'python main.py'+' --dropout '+str(dropout)+' --lr '+str(lr)+' --nhid '+str(nhid)+' --emsize '+str(emsize)+' --clip '+str(clip)+' --dropouth '+str(dh)+' --dropouti '+str(di)+' --dropoute '+str(de)+' --wdrop '+str(wd)+' --alpha '+str(alph)+' --beta '+str(bet)+' --optimizer '+str(opt)
    return command
    

for i in range(500):
    print("-"*89)
    print("-" *40 + "ITER NO " + str(i) + "-"*40)
    print("-"*89)
    command = runrandom() + ' --epochs 80 --batch_size 20 --bptt 35'
    print(command)
    os.system(command)
    