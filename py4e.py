def computepay(h, r):
    if fhrs > 40:
        return ((h-40)*r*1.5 + (40*r))
    else:
        return h*r

hrs = input("Enter Hours:")
rate= input("Enter Rate:")
fhrs=float(hrs)
frate=float(rate)
p = computepay(fhrs, frate)
print("Pay", p)

######################################################################

largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    try:
        if num == "done":
            break
        num=int(num)
        if largest is None:
            largest= num
        elif num > largest:
            largest=num
        elif smallest is None:
            smallest=num
        elif num < smallest:
            smallest=num
    except:
        print('Invalid input')
        continue
    

    
print("Maximum is", largest)
print("Minimum is", smallest)

###########################################################

# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
fh = open(fname)

total= 0
cnt=0
#numlist= []
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    f_val= float(line.strip()[19:])
    total= total+f_val
    cnt= cnt+1
    #numlist.append(f_val)

print('Average spam confidence:', total/cnt)
#print(sum(numlist)/len(numlist))

####################################################################

fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    pre_lst= line.split()
    for word in pre_lst:
        if word not in lst:
            lst.append(word)
        else:
            continue
lst.sort()
print(lst)

####################################################################

fname = input("Enter file name: ")
fh = open(fname)

count=0
lst=[]
for line in fh:
    if not line.startswith("From") or line.startswith("From:"):
        continue
    lst= line.split()
    print(lst[1])
    count= count+1

print("There were", count, "lines in the file with From as the first word")

##################################################

fname = input("Enter file:")
fh = open(fname)

counts={}
for line in fh:
    if not line.startswith("From") or line.startswith("From:"):
        continue
    words= line.split()
    email=words[1]
    counts[email]= counts.get(email, 0) +1

bigcount= None
bigword= None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword=word
        bigcount=count

print(bigword, bigcount)

###############################################################
fname = input("Enter file:")
fh = open(fname)

counts={}
for line in fh:
    if not line.startswith("From") or line.startswith("From:"):
        continue
    words= line.split()
    times=words[5]
    hours= times[0:2]
    counts[hours]= counts.get(hours, 0) +1

counts = sorted([(k,v) for k,v in counts.items()])
for k,v in counts:
    print(k, v)