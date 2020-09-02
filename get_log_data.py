import os
import re
import csv
import time
from pathlib import Path

rootdir = 'C:/Users/victor/Desktop/AwdLSTM/'

count = 0
minloss = 500
minppl = 500
lossargs = 'error'
pplargs = 'error'

def getparams(args):
    name = (re.findall("save=.*?.*'", args)[0]).replace("save=","")
    batchsize = int(re.findall("batch_size.*?(\d+)", args)[0])
    bptt = int(re.findall("bptt.*?(\d+)", args)[0])
    clip = float(re.findall("clip.*?(\d+.\d+)", args)[0])
    dropout = float(re.findall("dropout.*?(\d+.\d+)", args)[0])
    emsize = int(re.findall("emsize.*?(\d+)", args)[0])
    epochs = int(re.findall("epochs.*?(\d+)", args)[0])
    lr = int(re.findall("lr.*?(\d+)", args)[0])
    nhid = int(re.findall("nhid.*?(\d+)", args)[0])
    nlayers = int(re.findall("nlayers.*?(\d+)", args)[0])
    return name,batchsize,bptt,clip,dropout,emsize,epochs,lr,nhid,nlayers

date = time.strftime("%Y%m%d-%H%M%S")
f = open("stats-" + date + ".csv", 'w+')
fieldnames = ['name','batchsize','bptt','clip','dropout','emsize','epochs','lr','nhid','nlayers','modeltotalparam','lastepoch','validloss','validppl','testloss','testppl','generatedtext']
writer = csv.DictWriter(f, fieldnames=fieldnames)
writer.writeheader()

for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        filename = Path(os.path.join(subdir, file)).resolve().stem
#        print("FILE: " + filename)
        if(filename == "log"):
            print("PATH: " + os.path.join(subdir, file))
            count = count + 1
            f = open(os.path.join(subdir, file))
            txt = f.read()
            args = re.findall("^Args.*", txt)
            name,batchsize,bptt,clip,dropout,emsize,epochs,lr,nhid,nlayers = getparams(args[0])
            modeltotalparam = int(re.findall("Model total parameters:.*?(\d+)", txt)[0])
            validloss = float(re.findall("valid loss.*?(\d+.\d+)", txt)[-1])
            validppl = float(re.findall("valid ppl.*?(\d+.\d+)", txt)[-1])
            testloss = float(re.findall("test loss.*?(\d+.\d+)", txt)[0])
            testppl = float(re.findall("test ppl.*?(\d+.\d+)", txt)[0])
            lastepoch = re.findall("end of epoch.*?(\d+)", txt)[-1]
            generatedtextlist = re.findall("GENERATED:.*", txt)
            if not generatedtextlist:
                generatedtext = "No text generated!"
            else:
                generatedtext = generatedtextlist[0]
#                print("YAAAAAAY: " + generatedtext)
            writer.writerow({'name' : name,'batchsize' : batchsize,'bptt':bptt,'clip':clip,'dropout':dropout,'emsize':emsize,'epochs':epochs,'lr':lr,'nhid':nhid,'nlayers':nlayers,'modeltotalparam':modeltotalparam,'lastepoch':lastepoch,'validloss':validloss,'validppl':validppl,'testloss':testloss,'testppl':testppl,'generatedtext':generatedtext})

            if testloss < minloss:
                minloss = testloss
                lossargs = args[0]
            if testppl < minppl:
                minppl = testppl
                pplargs = args[0]
                
#            print ('TestLoss: ' + str(testloss))
#            print ('TestPPL: ' + str(testppl))

print ('COUNT: ' + str(count))
print ('MINLOSS: ' + str(minloss))
print ('ARGSLOSS: ' + lossargs)
print ('MINPPL: ' + str(minppl))
print ('ARGSPPL: ' + pplargs)

f.close()
#print("FILENAME: " + os.path(file)[0])