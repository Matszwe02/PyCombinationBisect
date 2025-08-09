import time

from main import CombinationBisect
if __name__ == '__main__':
    total_items = 0
    def test(a: list):
        global total_items
        total_items += len(a)
        time.sleep(.5)
        return 4 in a and 10 in a

    a = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    cb = CombinationBisect(a, test)

    iterations = 0
    while cb.step(): iterations += 1

    print(f'Program finished with a resulting list of {cb.result()}')

    print(f'took {iterations} iterations with total tested items {total_items}')