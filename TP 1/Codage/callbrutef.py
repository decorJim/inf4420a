import pickle

def main():
    "input"

    with open('temp.pkl','rb') as file:
        map=pickle.load(file)

    with open('input.bin','rb') as myFile:
        encrypted=myFile.read()
        
    print(map[encrypted])

   

if __name__ == "__main__":
    main()
