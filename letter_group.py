"""字母组"""

import pygame


class LetterGroup:
    '''字母组 就是队列'''
    
    def __init__(self, *value):
        self.values = list(value)
        self.i = 0
    
    def __iter__(self):
        '''返回迭代器 就是自己'''
        self.index = 0
        return self

    def __next__(self):
        try:
            self.index += 1
            return self.values[self.index - 1]
        except IndexError:
            raise StopIteration
    
    def add(self, value):
        '''入队'''
        self.values.append(value)

    def out(self, i:int):
        '''出队'''
        if len(self.values) > 0:
            self.i = i
            return self.values.pop(0)
    
    def need_del_(self) -> bool:
        if len(self.values) > 0:
            return self.values[0].need_del_()
        return False

    def key_doun_(self, i) -> bool:
        if len(self.values) > 0 and i-self.i >= 20:
            return self.values[0].key_doun_()
        return False