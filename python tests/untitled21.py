def topla(degerler):
    if (len(degerler))==0:
        return 0
    else:
        return degerler[0]+(topla(degerler[1:]))
    
    
print(topla([1,2,3,4,5]))


