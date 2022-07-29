import os
import time
os.system("cls")
print ("#===========================================================================#")
print ("#         █████╗ ██╗  ██╗████████╗██╗██╗   ██╗ █████╗ ███████╗██╗           #")
print ("#        ██╔══██╗██║ ██╔╝╚══██╔══╝██║██║   ██║██╔══██╗██╔════╝██║           #")
print ("#        ███████║█████╔╝    ██║   ██║██║   ██║███████║███████╗██║           #")
print ("#        ██╔══██║██╔═██╗    ██║   ██║╚██╗ ██╔╝██╔══██║╚════██║██║           #")
print ("#        ██║  ██║██║  ██╗   ██║   ██║ ╚████╔╝ ██║  ██║███████║██║           #")
print ("#        ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═══╝  ╚═╝  ╚═╝╚══════╝╚═╝           #")
print ("#===========================================================================#\n\n")
print ("                1. Lamo               6.  Sarolangun      11. Jambi-Old")
print ("                2. Ruko               7.  Kuamang")
print ("                3. Candika            8.  Somel")
print ("                4. Rimbo              9.  Tebo")
print ("                5. Bulian             10. Jambi-new\n\n")
xs = int(input("       Inputkan Port = "))
if(xs==1):
    os.system("cls")
    os.system("python3 conf/lamo.py")
    time.sleep(30)
    os.system("python3 start.py")


elif(xs==2):
    os.system("cls")
    os.system("python3 conf/ruko.py")
    time.sleep(30)
    os.system("python3 start.py")


elif(xs==3):
    os.system("cls")
    os.system("python3 conf/candika.py")
    time.sleep(30)
    os.system("python3 start.py")


elif(xs==4):
    os.system("cls")
    os.system("python3 conf/rimbo.py")
    time.sleep(30)
    os.system("python3 start.py")


elif(xs==5):
    os.system("cls")
    os.system("python3 conf/bulian.py")
    time.sleep(30)
    os.system("python3 start.py")


elif(xs==6):
    os.system("cls")
    os.system("python3 conf/sarolangun.py")
    time.sleep(30)
    os.system("python3 start.py")


elif(xs==7):
    os.system("cls")
    os.system("python3 conf/kuamang.py")
    time.sleep(30)
    os.system("python3 start.py")


elif(xs==8):
    os.system("cls")
    os.system("python3 conf/somel.py")
    time.sleep(30)
    os.system("python3 start.py")


elif(xs==9):
    os.system("cls")
    os.system("python3 conf/tebo.py")
    time.sleep(30)
    os.system("python3 start.py")


elif(xs==10):
    os.system("cls")
    os.system("python3 conf/jambinew.py")
    time.sleep(30)
    os.system("python3 start.py")


elif(xs==11):
     os.system("cls")
     os.system("python3 conf/jambi.py")
     time.sleep(30)
     os.system("python3 start.py")

else:
    os.system("python3 start.py")
