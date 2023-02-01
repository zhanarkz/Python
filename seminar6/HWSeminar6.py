import os
import time
from sys import platform 

# creating a .txt file to store contact details 
filename = "tel.txt" 
myfile = open(filename, "a+") 
myfile.close 

# defining main menu 
def main_menu(): 
    print( "\nГлавное меню\n") 
    print( "1. Показать все контакты") 
    print( "2. Добавить новый контакт") 
    print( "3. Поиск контакта")
    print( "4. Удаление контакта")
    print( "5. Изменить номер телефона у контакта") 
    print( "6. выход") 
    choice = input("Введите команду: ") 
    if choice == "1": 
        myfile = open(filename, "r+") 
        filecontents = myfile.read() 
        if len(filecontents) == 0: 
            print( "Никого нет") 
        else: 
            print(filecontents) 
        myfile.close 
        main_menu() 
    elif choice == "2": 
        newcontact()      
        main_menu() 
    elif choice == "3": 
        searchcontact()  
        main_menu() 
    elif choice == "4": 
        delcontact()
        main_menu() 
    elif choice == "5":
        changenumber()
        main_menu()
    elif choice == "6":
        print("До свидания!")
    else: 
        print( "неправильный ввод!\n") 
        main_menu() 
 
# defining search function         
def searchcontact(): 
    searchname = input( "Введите имя: ") 
    remname = searchname[1:] 
    firstchar = searchname[0] 
    searchname = firstchar.upper() + remname 
    myfile = open(filename, "r+") 
    filecontents = myfile.readlines() 
      
    found = False 
    for line in filecontents: 
        if searchname in line: 
            print( "Ваш контакт:", end = " ") 
            print( line) 
            found = True 
            break 
    if found == False: 
        print( "никого нет", searchname) 
 
# first name 
def input_firstname(): 
    first = input( "Имя: ") 
    remfname = first[1:] 
    firstchar = first[0] 
    return firstchar.upper() + remfname 
 
# Family name 
def input_lastname(): 
    last = input( "Фамилия: ") 
    remlname = last[1:] 
    firstchar = last[0] 
    return firstchar.upper() + remlname 
 
# storing the new contact details 
def newcontact(): 
    firstname = input_firstname() 
    lastname = input_lastname() 
    phoneNum = input( "номер телефона: ") 
    contactDetails =("[" + firstname + " " + lastname + ", " + phoneNum + "]\n") 
    myfile = open(filename, "a") 
    myfile.write(contactDetails) 
    print( "Следующий контакт:\n " + contactDetails + "\nуспешно сохранен!") 

def delcontact():
    answer = input("Порядковый номер для удаления: ")
    answer = int(answer)
    with open(filename, "r+") as fp:
        lines = fp.readlines()
        fp.seek(0)
        fp.truncate()
        for number, line in enumerate(lines):
            if number not in [answer - 1]:
                fp.write(line)

def changenumber():
    return

main_menu() 