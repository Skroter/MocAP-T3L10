pets = {}

print("Добро пожаловать в ВетКлинику")

while True:
    print("Что вы хотите сделать? :")
    print("1 - Создать карточку пациента")
    print("2 - Вывести на экран карточку")
    print("0 - Ничего.")
    req = input()
    
    if req == "1":
        print("Введите кличку пациента:")
        name = input()
        pets[name] = {"Вид питомца":0,"Возраст питомца":0,"Имя владельца":0}
        
        print("Введите вид питомца: ")
        type = input()
        pets[name]["Вид питомца"] = type
        
        print("Введите возраст питомца: ")
        years = int(input())
        if (years == 1) or (years == 21):
            yearsUpd = str(years) + " год."
        elif (5 > years > 1) or (25 > years > 21) or (35 > years > 31):
            yearsUpd = str(years) + " года."
        elif (21 > years > 4) or (24 < years < 31):
            yearsUpd = str(years) + " лет."
        elif (35 < years < 1):
            print("Ваш питомец либо еще не родился либо уже слишком стар. Извините.")
            break
        pets[name]["Возраст питомца"] = yearsUpd
        
        print("Введите имя владельца: ")
        petMastrName = input()
        pets[name]["Имя владельца"] = petMastrName
        
    elif req == "2":
        print("Карточку какого питомца вы хотите просмотреть?", pets.keys(), sep="\n")
        name = input()
        print("Это", pets[name]["Вид питомца"], "по кличке", '"{}".'.format(name), "Возраст питомца:",pets[name]["Возраст питомца"],"Имя владельца:",pets[name]["Имя владельца"])
    else:
        break
print("До свидания.")