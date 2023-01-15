import pickle

def ADD():
    f=open("shoes.dat","ab")
    s_id=int(input("Enter shoes id: "))
    name=input("Enter the name: ")
    brand=input("Enter the brand: ")
    typ=input("Enter the type: ")
    price=int(input("Enter shoes price: "))
    l=[s_id,name,brand,typ,price]
    pickle.dump(l,f)
    print("record added sucessfully")
    f.close()

def Display():
    
    f=open("shoes.dat","rb")
    while True:
        try:
            data=pickle.load(f)
            print(data)
        except Exception:
            break
    f.close()
    
def Search():
    f=open("shoes.dat","rb")
    search=int(input("Enter the shoes id to search: "))
    while True:
        try:
            data=pickle.load(f)
            found="false"
            if data[0]==search:
                print("record found")
                print("name of shoes :",data[1])
                print("brand of shoes :",data[2])
                print("type of shoes :",data[3])
                print("price of shoes :",data[4])
                found="true"
                break
        except Exception:
            if found=="false":
                print("record not found")
    f.close()
while True:
    print("1:Add record\n2:Display record\n3:Search record\n4:Exit")
    choice=int(input("Enter the choice :"))
    if choice==1:
        ADD()
    elif choice==2:
        Display()
    elif choice==3:
        Search()
    elif choice==4:
        break
    else:
        print("invalid choice")
