def user(list1):
    while 1:
            if option == '1':
                print(list1.upper())
            elif option == '2':
                print(list1.lower())
            elif option == '3':
                x = input('What to change?:')
                y = input('What to change to?:')
                list2 = list1.replace(x, y)
                print(list2)
            elif option == '4':
                print(list1.capitalize())
            elif option == '5':
                print(list1.title())
            elif option == '6':
                print(list1.isdigit())
            elif option == '7':
                print(list1.split())
            elif option == '8':
                print(list1.join())
            return list1
list1 = input("Hi! Enter your last name and first name ")
while 2:
        option = input(" Nice to meet you, " + list1 + ". What do you want to change in your name? \
        Select the method: 1-upper 2-lower 3-replace 4-capitalize 5-title 6-isdigit 7-split 8-join 9-exit")
        list1 = user(list1)
        if option == '9':
            exit = input('Do you want to get out? y/n')
        if exit == 'y':
            break
        elif exit == 'n':
            continue
