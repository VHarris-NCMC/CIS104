#name = input("Enter file:")
## This is the same thing as 9.3, I think I did what this section is wanting me to do without meaning to? 
name = 'mbox.txt'
senders = dict()
if len(name) < 1:
    name = "mbox.txt"
handle = open(name)

for line in handle:
    
    if line.startswith('From '):
        splat = line.split()
        
           
        sender = splat[1]
        if sender not in senders:
            senders[sender] = 1
        else:
            senders[sender] += 1

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
        max = a
        most = b
   else:
        continue

print(max, most)

 