start = input ("what is the start number?")
end = input ("What is the end number?")

def generatenumbers(start,end):
    while start < end:
        print (start)
        start= start + 1


generatenumbers(int(start),int(end))
