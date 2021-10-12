def run():
    my_List = [1,"Hello", 5 ,4.5]
    my_dicc = {"FirstName": "Facundo", "LastName": "Garcia"}
    Super_Lista = [
        {"FirstName": "Manuel", "LastName": "Zevallos"},
        {"FirstName": "Gabriel", "LastName": "Zevallos"},
        {"FirstName": "Miguel", "LastName": "Torres"}
    ]

    super_dic = {
        "natural": [1,2,3],
        "integer": [-1,0,1],
        "floating": [1.1,4.5,3.1416]
    } 

    for key, value in super_dic.items():
        print(key,"-",value)

if __name__ =='__main__':
    run()

