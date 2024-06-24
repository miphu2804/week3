from abc import ABC, abstractmethod

class Person():
    def __init__(self, name, yob):
        self.name = name
        self.yob = yob

    @abstractmethod
    def describe(self):
        pass

class Doctor(Person):
    def __init__(self, name, yob, specialist):
        super().__init__(name = name, yob = yob)
        self.__specialist = specialist

    def describe(self):
        print(f"Doctor name: {self.name} - Yob: {self.yob} - Specialist: {self.__specialist}")

class Student(Person):
    def __init__(self, name, yob, grade):
        super().__init__(name = name, yob = yob)
        self.__grade = grade

    def describe(self):
        print(f"Student name: {self.name} - Yob: {self.yob} - Grade: {self.__grade}")

class Teacher(Person):
    def __init__(self, name, yob, subject):
        super().__init__(name = name, yob = yob)
        self.__subject = subject

    def describe(self):
        print(f"Teacher name: {self.name} - Yob: {self.yob} - Subject: {self.__subject}")

class Ward():
    def __init__(self, name):
        self.__name = name
        self.__listPeople = list()

    def addPerson(self, person:Person):
        self.__listPeople.append(person)

    def describe(self):
        print(f"Ward Name: {self.__name}")
        for p in self.__list_people:
            p.describe()

    def count_doctor(self):
        counter = 0
        for p in self.__list_people:
            if isinstance(p, Doctor):  # if type(p) is Doctor:
                counter += 1
        return counter

    def sort_age(self):
        self.__list_people.sort(key=lambda x: x.get_yob(), reverse=True)

    def compute_average(self):
        counter = 0
        total_year = 0
        for p in self.__list_people:
            if isinstance(p, Teacher):  # if type(p) is Teacher:
                counter += 1
                total_year += p.get_yob()
        return total_year / counter

if __name__ == "__main__":
    minhphu = Doctor("minh phu", "2005", "Optic")
    minhphu.describe()
