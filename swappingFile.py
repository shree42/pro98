def swapFileData():
    InputFileName1=input("Enter the file1 path")
    InputFileName2=input("Enter the file2 path")

    with open(InputFileName1,'r') as file1:
        data1=file1.read()
    
    with open(InputFileName2,'r') as file2:
        data2=file2.read()
    
    
    

    with open(InputFileName1,'w') as file1:
        file1.write(data2)

    with open(InputFileName2,'w') as file2:
        file2.write(data1)
    print("your text files are swapped")

swapFileData()