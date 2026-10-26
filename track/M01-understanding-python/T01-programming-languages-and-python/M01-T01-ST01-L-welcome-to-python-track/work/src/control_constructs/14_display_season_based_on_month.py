month=int(input("Enter month:"))
match month:
    case 12|1|2:
        print("Winter")
    case 3|4|5:
        print("Summer")
    case 6|7|8|9:
        print("Rainy")
    case 10|11:
        print("Autumn")
    case _:
        print("Invalid month")