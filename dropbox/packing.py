
import sys
def sanitize(array):
    for idx,item in enumerate(array):
        item = item.strip("\n")
        item = item.strip()
        array[idx] = [int(num) for num in item.split(" ")]
        

def main():
    items = sys.stdin.readlines()
    items = sanitize(items)
