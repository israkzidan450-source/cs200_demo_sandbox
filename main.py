def foo(x, y):
    return (x*y) + 1


def bar(x, y):
    return (x**y) - 1


def func1():
    lst = []
    print('Enter numbers one at a time. Enter 0 to stop.')
    x = int(input('num:'))
    while x != 0:
        lst.append(x)
        x = int(input('num:'))
    return lst



def func2(data):
    print('Here is the data:')
    print(data)

    option = ''
    while True:
        option = input('Select an option. 1-sum  2-min  3-max  4-quit')
        if option == '1':
            print('The sum is', sum(data))
        elif option == '2':
            print('Not supported yet')
        elif option == '3':
            print('Not supported yet')
        elif option == '4':
            print('Goodbye')
            return


def main():
    print("Hello, Mom")
    data = func1()
    func2(data)


if __name__ == "__main__":
    main()


