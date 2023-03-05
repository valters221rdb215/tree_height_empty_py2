import sys
import threading
import numpy

def read_input():
    while True:
        try:
            source = input("Enter 'i' to read input from keyboard, or 'f' to read from file: ")
            if source == 'i':
                n = int(input("Enter the number of nodes: "))
                parents = list(map(int, input("Enter the parent IDs separated by spaces: ").split()))
                return n, parents
            elif source == 'f':
                filename = input("Enter the name of the input file: ")
                if 'a' in filename.lower():
                    print("Error: The file name cannot contain the letter 'a'. Please try again.")
                    continue
                with open(f"folder/{filename}", 'r') as f:
                    n = int(f.readline())
                    parents = list(map(int, f.readline().split()))
                    return n, parents
            else:
                print("Wrong input. Please enter 'i' or 'f'.")
        except FileNotFoundError:
            print("Error: The specified file was not found. Please try again.")
        except ValueError:
            print("Error: Invalid input format. Please try again.")

def compute_height(n, parents):
    tree = {}
    for i in range(n):
        parent = parents[i]
        if parent == -1:
            root = i
        else:
            if parent not in tree:
                tree[parent] = []
            tree[parent].append(i)

    def compute_subtree_height(node):
        if node not in tree:
            return 1
        subtree_heights = [compute_subtree_height(child) for child in tree[node]]
        return 1 + max(subtree_heights)

    return compute_subtree_height(root)

def main():
    n, parents = read_input()
    height = compute_height(n, parents)
    print(height)

sys.setrecursionlimit(10**7)
threading.stack_size(2**27)  
threading.Thread(target=main).start()
