def SentarGente(Seats:list, Students:list, Movements: int = 0):
    Seats.sort()
    Students.sort()
    i = 0
    while seats != students:
        if Seats[i] == Students[i]:
            i+= 1
            continue
    
        if Seats[i] < Students[i]:
            Students[i] -=1
            Movements += 1
        elif Seats[i] > Students[i]:
            Movements += 1
            Students[i] += 1
    print(seats)
    print(students)
    return Movements


seats = [2,2,6,6]
students = [1,3,2,6]

print(SentarGente(seats,students))