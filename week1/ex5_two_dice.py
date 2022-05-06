import itertools

def main():
    for i, j in itertools.product(range(1,7), range(1,7)):
        if i + j == 5:
            print(f"({str(i)},{str(j)})")

if __name__ == "__main__":
    main()
