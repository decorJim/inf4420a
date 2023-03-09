import pickle

def main():
    "input"
    with open('temp.pkl','rb') as file:
        map=pickle.load(file)    

    with open('input.bin','rb') as myFile:
        input=myFile.read()

    print(map[input])
        


if __name__ == "__main__":
    main()
