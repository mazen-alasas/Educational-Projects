# Mazen Ahmed Al-asas
# Simple Library Management System
""""""""" add libraries  """""""""
from abc import ABC, abstractmethod
import numpy as np
import matplotlib.pyplot as mp
import pandas as ps

""" as DataSet """
login_data = {'mazen': 52429,           """ using Dict to store Login Data for workers """
              'ahmed': 52427,           """ i used the dictionary because i can't handle on CSV file yet """
              'ashraf': 4524,
              'ayman': 63247,
              'ali': 7854512,
              'abdo': 557996,
              'khalid': 4632}

books = ['CS', 'IS', 'IT', 'OOP', 'C#', 'Python']       # using List to Store names of some books


def display():                                          # Get username & Password
    print(f"        Hi dear...")
    print(f"Enter your User name : ", end=' ')
    us_nm = input()
    print(f"Enter your Password : ", end=' ')
    pss = int(input())
    return us_nm, pss


class MainData(ABC):
    def __init__(self, name, password):
        self.name = name
        self.password = password

    @abstractmethod
    def get_history(self):
        pass

    def set_history(self):
        pass

    def posts(self, post):
        pass


class Worker(MainData):
    worker_post_rate = np.array([])
    # posts = np.array()

    def __init__(self, name, password, hist=None):
        self.hist = hist
        self.hist = []
        super().__init__(name, password)

    @staticmethod
    def print_choices():
        print('Enter the number corresponding to what you will to do ..')
        print('1 - Add a new book ')
        print('2 - Change name of book ')
        print('3 - Delete book ')
        print('4- Show your history ')
        print('5- Get my posts ')
        n = int(input('Your choice :  '))
        print('***********************************************************************')
        return n
    """    
    def posts(self, post):
        self.worker_post_rate = np.insert(post)

    def get_my_posts(self):
        mp.plot(self.worker_post_rate)
        mp.show()
    """

    def task(self):
        n = self.print_choices()
        if n == 1:
            new_book = input('Enter tne new book name :  ')
            books.append(new_book)
            print('updated --')
            print(books)
            print('***********************************************************************')
            agn = input('Enter yes if you have another task otherwise no :  ')
            if agn == 'yes':
                print('***********************************************************************')
                self.task()
        elif n == 2:
            old_name = input('Enter the old name of the book :  ')
            her = 0
            for i in range(len(books)):
                if old_name == books[i]:
                    her = 1
                    new_name = input('Enter the new name :  ')
                    books[i] = new_name
                    print('updated --')
                    print(books)
                    print('***********************************************************************')
                    break
            if her == 0:
                print('Not Found --')
                print('***********************************************************************')
        elif n == 3:
            d = input('Enter the name of the book you want to delete :  ')
            exist = 0
            for j in range(len(books)):
                if d == books[j]:
                    exist = 1
                    books.remove(d)
                    print('updated --')
                    print(books)
                    print('***********************************************************************')
                    break
            if exist == 0:
                print('Not Found --')
                print('***********************************************************************')
        elif n == 4:
            self.get_history()
        """
        elif n == 5:
            self.get_my_posts()
        """

        agn = input('Enter yes if you have another task otherwise no :  ')
        if agn == 'yes':
            print('***********************************************************************')
            self.task()

    # getter method to return history
    def get_history(self):
        print('Your history : ')
        for i in range(len(self.hist)):
            print(f'{i + 1}- {self.hist[i]}')

    # setter method to add task to history list
    def set_history(self, task):
        self.hist.append(task)


class Student(MainData):
    student_post_rate = np.array([])

    def __init__(self, name, id_num, histo=None):
        self.history = histo
        self.histo = []
        super().__init__(name, id_num)

    @staticmethod
    def print_choices():
        print('Enter the number corresponding to what you want ..')
        print('1 - Borrows Book ')
        print('2- Return Book ')
        print('3 - Buy Book ')
        print('4- Show your history ')
        n = int(input('Your choice :  '))
        print('***********************************************************************')
        return n

    """
    def posts(self, post):
        self.student_post_rate = np.insert(post)

    def get_my_posts(self):
        mp.plot(self.student_post_rate)         need to another array week days to x-axis ?
        mp.show()
    """

    def what_he_want(self):
        counter = 0
        x = 0
        if counter == 0:
            x = self.print_choices()
        counter += 1
        if x == 1:
            bor_book = input('Enter the name of the book you wont to borrow :  ')
            her = 0
            for i in range(len(books)):
                if bor_book == books[i]:
                    her = 1
                    print('There he is --')
                    books.remove(bor_book)
                    task = f'You borrowed a {bor_book} book'
                    self.set_history(task)
                    print(books)
                    print('***********************************************************************')
                    break
            if her == 0:
                print('Not Found --')
                print('***********************************************************************')
            agn = input('Enter yes if you have another task otherwise no :  ')
            if agn == 'yes':
                print('***********************************************************************')
                self.what_he_want()
        elif x == 2:
            return_book = input('Enter the name of the book you will return ')
            books.append(return_book)
            print('updated --')
            print(books)
            print('***********************************************************************')
        elif x == 3:
            buy_book = input('Enter the name of the book you need to buy :  ')
            exist = 0
            for b in range(len(books)):
                if buy_book == books[b]:
                    exist = 1
                    print('There he is --')
                    books.remove(buy_book)
                    print(books)
                    print('***********************************************************************')
                    break
            if exist == 0:
                print('Not found --')
                print('***********************************************************************')
        elif x == 4:
            self.get_history()
        """
        elif x == 5:
            self.get_my_posts()
        """

        agn = input('Enter yes if you have another task otherwise no :  ')
        if agn == 'yes':
            print('***********************************************************************')
            self.what_he_want()

    # getter method to return history
    def get_history(self):
        print('Your history : ')
        for i in range(len(self.histo)):
            print(f'{i + 1}- {self.histo[i]}')

    # setter method to add task to history list
    def set_history(self, task):
        self.histo.append(task)


def check_data():
    user_name, password = display()
    for name in login_data:
        if name == user_name and password == login_data[name]:
            print('***********************************************************************')
            worker_op = Worker(user_name, password)
            worker_op.task()
            break
        else:
            print('***********************************************************************')
            print('Are you a student ?')
            name = input('Enter your name :  ')
            id_card = input('Enter your ID :  ')
            print('***********************************************************************')
            student = Student(name, id_card)
            student.what_he_want()


check_data()
