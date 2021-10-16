#Ordenador de Listas

#este programa recibe una lista como parametro y devuleve otra sin repoetidas
def remove_duplicates(Lista):
    without_duplicates = []
    for element in Lista:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

def run():
    random_List = [1,1,2,2,3,4,5,6,6]

    print(remove_duplicates(random_List))


if __name__ == "__main__":
    run()