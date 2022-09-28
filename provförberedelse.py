# class Aeroplane:
#     def __init__(self):
#         self.max_altitude = 0
#     def fly(self):
#         print("Flyger!")
#         self.max_altitude = 10000
# boeing = Aeroplane()

# print(boeing.fly())
# print(boeing.max_altitude)



# class Student:
#     def __init__(self):
#         self.name = "Monty"
#     def get_grade(self):
#         return self.__grade
#     def set_grade(self, grade):
#         if grade == "A" or grade == "B" or grade == "C" or grade == "D" or grade == "E" or grade == "F":
#             self.__grade = grade
#         else:
#             self.__grade = "-"
# student = Student()
# student.set_grade("B")
# print(student.get_grade())


antal = input()

king, queen, rooks, bishops, knights, pawns = antal.split()
king = int(king)
queen = int(queen)
rooks = int(rooks)
bishops = int(bishops)
knights = int(knights)
pawns = int(pawns)


king = 1 - king
queen = 1 - queen
rooks = 2 - rooks
bishops = 2 - bishops
knights=  2 - knights
pawns = 8 - pawns


print(king, queen, rooks, bishops, knights, pawns)