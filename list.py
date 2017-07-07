list1 =[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
maximum =list1[0]
def getbiggernumber(list1):
    for k in list1:
        if maximum<list1[k]:
            maximum=list1[k]
        print (maximum)
getbiggernumber(list1)
