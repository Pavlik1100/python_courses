"""

    Напишите функцию check_password, которая проверяет переданный ей пароль на сложность и печатает на экран результат проверки.

    Сложным паролем будет считаться комбинация символов, в которой :

        1. Есть хотя бы 3 цифры;
     
        2. Есть хотя бы одна заглавная буква;
     
        3. Есть хотя бы один символ из следующего набора "!@#$%*";

        4. Общая длина не менее 10 символов.

    Если пароль прошел все проверки, функция должна вывести на экран фразу "Perfect password", в противном случае - "Easy peasy"
     

"""

def check_password(s):
    
    ch1 = False
    ch2 = False
    ch3 = False
    ch4 = False
    digs = 0
    li = 0

    for c in s:

        if c.isdigit():
            digs += 1

        if c == c.upper() and c.isalpha():
            ch2 = True

        if c in '!@#$%*':
            ch3 = True

    if len(s) >= 10:
        ch4 = True

    if digs >= 3:
        ch1 = True

    # print(ch1, ch2, ch3, ch4)

    if ch1 and ch2 and ch3 and ch4:
        print('Perfect password')
    else:
        print('Easy peasy')

check_password(input())        
    # if s != s.lower() and len(s)