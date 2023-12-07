test = [1,2,3,1,2,3,1,2,3]

source = []
dest = []
counter = []


def tester():
    count = 0
    for x in range(len(test)):
        
        if count == 0:
            source.append(test[x])
            count +=1
        elif count == 1:
            dest.append(test[x])
            count +=1
        else:
            counter.append(test[x])
            count=0
    lister = [source,dest,counter]
    return list(lister)

print(tester())