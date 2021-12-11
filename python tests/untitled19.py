def ortalama(vize,final):
     ort = (vize*4/10)+(final*6/10)
     return ort
 
def harfdegeribul(ort):
    if ort>=70 :
        print("geçtiniz ve ort :",ort )
        
    else :
        print("kaldın ve ort :",ort)

def veda():
    print("Sınıf not hesaplama işlemi bitti,bb")



mevcut = int(input("mevcudu giriniz :"))

for i in range(mevcut):
    vize=float(input("vize girin"))
    final=float(input("final girin"))
    hesaplananOrt=ortalama(vize,final)
    harfdegeribul(hesaplananOrt)
    
veda()
    
    
"""  
    if ort >=70 :
        print("geçtiniz ve ort",ort)
    else :
        print("kaldın ve ort",ort)
    
"""   