#name = input("Enter file:")
name = 'mbox.txt'
senders = dict()
if len(name) < 1:
    name = "mbox.txt"
handle = open(name)

for line in handle:
    
    if line.startswith('From '):
        splat = line.split()
        
           
        atSign = splat[1].index('@')
        senderDomain = splat[1][atSign:]        
        if senderDomain not in senders:
            senders[senderDomain] = 1
        else:
            senders[senderDomain] += 1

max = ''
most = 0
for a, b in senders.items():
   if b > most:
        max = a
        most = b
   else:
        continue
max = ''
most = 0
for a, b in senders.items():
   if b > most:
        max = str(a)
        most = b
   else:
        continue

print (senders.items())



 