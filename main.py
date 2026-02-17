#Project Euler Problem 81

#You need to evauluate a all ahead paths not just the  beacuse you want the least value

import pandas as pd


class Shortest_Path():
    def __init__(self):
        self.matrix = pd.read_table('0081_matrix.txt')
        self.a_value = 0 #will use to count value of path



