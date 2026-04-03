def func1():
    lst = []
    print('Enter numbers one at a time. Enter 0 to stop.')
    x = int(input('num:'))
    while x != 0:
        lst.append(x)
        x = int(input('num:'))
    return new_func(lst)

def new_func(lst):
    return lst

def func2(data):
    print('Here is the data:')
    print(data)

    option = ''
    while True:
        option = input('Select an option. 1-sum  2-min  3-max  4-quit')
        if option == '1':
            print('The sum is',sum(data))
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

    def problem1(s):
    dct = {}

    for letter in s:
        if letter in dct:
            dct[letter] += 1
        else:
            dct[letter] = 1
    return dct
print(problem1('Hello'))

    
    