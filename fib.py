def fib():
    fibs = [1, 2]
    for i in range(1,99):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs

def main():
    print('OUTPUT', fib())

if __name__ == "__main__":
    main()
