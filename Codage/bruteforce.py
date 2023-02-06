import os
import pickle

map={}

def main():

    for i in range(10000):
       nip=str(i)
       if i<10:
         nip="000"+nip
       
       elif i<100:
         nip="00"+nip
        
       elif i<1000:
         nip="0"+nip

       if i%1000==0:
          print(i)

       os.system('python3 transBase.py '+nip+' > temp.bin')
       with open('temp.bin','rb') as myFile:
           encrypted=myFile.read()
       map[encrypted]=i
    
    with open('temp.pkl','wb') as file:
        pickle.dump(map,file)

    print("completed")



    

if __name__ == "__main__":
    main()
