from typing import Callable, Any
import math


def bg_red(s): return("\033[41m" + str(s) +"\033[00m")
def bg_cyan(s): return("\033[46m" + str(s) +"\033[00m")
def bg_green(s): return("\033[42m" + str(s) +"\033[00m")



class CombinationBisect:
    def __init__(self, items: list, test: Callable[[list], bool]):
        """CombinationBisect returns the smalles set of variables that returns True in test"""

        self.items = items.copy()
        self.items_dict = {}
        self.len_items = len(items)

        for item in items:
            self.items_dict[item] = True

        self.test = test
        self.check_index = 0
        self.check_depth = 0
    

    def step(self) -> bool:
        """Step over the possibilities, returns True when still need to step and False when finished"""

        while True:

            width = self.len_items / pow(2, self.check_depth)
            items = math.ceil(width)

            skip = False
            for idx, i in enumerate(self.items_dict.keys()):
                if idx in range(self.check_index,self.check_index+items) and self.items_dict[i]:
                    break
            else:
                skip = True

            test_list = self.items[:self.check_index] + self.items[self.check_index+items:]
            for i in self.items_dict.keys():
                if test_list.__contains__(i) and not self.items_dict[i]: test_list.remove(i)

            if len(test_list) == 0: skip = True
            if not skip:

                # print(f'Checking {items=} {width=} {self.check_depth=} {self.check_index=}')
                # print(f'So {test_list}')
                resp = self.test(test_list)
                # print(f'received {resp}')
                if resp:
                    for idx, i in enumerate(self.items_dict.keys()):
                        if idx in range(self.check_index,self.check_index+items):
                            self.items_dict[i] = False

                # print(self.items_dict)
                for i in self.items_dict.keys():
                    n_chars = (math.floor(50/self.len_items))
                    if self.items_dict[i]: print(bg_cyan(' '*(n_chars)+'?'+' '*(n_chars)), end='')
                    else: print(bg_red(' '*(n_chars)+'X'+' '*(n_chars)), end='')
                print()

            if width <= .5:
                for i in self.items_dict.keys():
                    n_chars = (math.floor(50/self.len_items))
                    if self.items_dict[i]: print(bg_green(' '*(n_chars)+'✓'+' '*(n_chars)), end='')
                    else: print(bg_red(' '*(n_chars)+'X'+' '*(n_chars)), end='')
                print()
                return False
            self.check_index += items
            depth_step = (self.check_index+items)/width > pow(2, self.check_depth)
            if depth_step:
                # print('increasing depth')
                self.check_depth += 1
                self.check_index = 0
            if not skip: return True


    def result(self) -> list[Any]:
        items = []
        for i in self.items_dict.keys():
            if self.items_dict[i]: items.append(i)
        return items
