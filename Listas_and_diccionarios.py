def run():
    # my_List = [1,"Hello", 5 ,4.5]
    # my_dicc = {"FirstName": "Facundo", "LastName": "Garcia"}
    # Super_Lista = [
    #     {"FirstName": "Manuel", "LastName": "Zevallos"},
    #     {"FirstName": "Gabriel", "LastName": "Zevallos"},
    #     {"FirstName": "Miguel", "LastName": "Torres"}
    # ]

    # super_dic = {
    #     "natural": [1,2,3],
    #     "integer": [-1,0,1],
    #     "floating": [1.1,4.5,3.1416]
    # } 

    # for key, value in super_dic.items():
    #     print(key,"-",value)

    # for element in Super_Lista:
    #     print(element)    
    LC = [i for i in range(1,101) if i%3 != 0]
    DC1 = {i : i**3 for i in range(1,101) if i%3!=0}
    palindromo = lambda string: string ==string[::-1]

    # print(DC1)
    print(palindromo("ana"))

if __name__ =='__main__':
    run()

