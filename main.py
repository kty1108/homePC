# Even & Odd number
def L1_evenOdd():

    print(10 / 3)
    print(101 % 2)

    print('even') if ((10) % 2) == 0 else print('odd')


# Multiple of 3 & 5, and summarized
# i++ ++i -> not supported in Python
def L1_multipleSummarization():

    user_input = input()

    MAX = int()
    MAX = int(user_input) + 1

    m3, m5 = list(), list()
    tmp = list()

    for i in range(1, MAX):
        m3.append(i) if ((i % 3) == 0) else tmp.append(i)
        m5.append(i) if ((i % 5) == 0) else tmp.append(i)

    m3.extend(m5)
    m3 = set(m3)

    print(sum(m3))

# Average & Grade of subjects
def L1_scoreReturn():
    user_input = '90 61 72' #input()

    usr_split = user_input.split(' ')
    usr_num = list(map(int, usr_split))

    sum_val = float(sum(usr_num))
    f_avg_val = round((sum_val / 3.0), 2)

    if f_avg_val > 89:
        grade = 'A'
    elif (90 > f_avg_val) and (f_avg_val >= 80):
        grade = 'B'
    elif (80 > f_avg_val) and (f_avg_val >= 70):
        grade = 'C'
    elif (70 > f_avg_val) and (f_avg_val >= 60):
        grade = 'D'
    elif (60 > f_avg_val) and (f_avg_val >= 0):
        grade = 'F'
    else:
        exit()

    print('{:.2f}'.format(f_avg_val), grade)

# to print Divisor list
# Slicing string
def L1_divisor():
    # user_input = int(input())     Very very important format to code on Goorm platform (Variable casting)
    user_input = 100
    divisorList = list()

    for i in range(1, user_input + 1):
        if user_input % i == 0:
            divisorList.append(i)

    str1 = str(divisorList)
    print(str1[1:-1].replace(', ',' '), '')

# Bit operator, Shift operator
def L1_shift():

    # print(hex(num1))      16진수 형 변환
    # print(bin(num1))      2진수 형 변환
    # print(int('1111', 2))   10진수 형 변환
    # print(int('0xf', 16))   10진수 형 변환

    # AND &, OR |, XOR ^, NOT ~

    # a >> b

    user_input_1, user_input_2 = map(int, input('입력 : ').split())
    #print(user_input_1)
    #print(type(user_input_1))
    #print(bin(user_input_1), bin(user_input_2))

    #print(bin(user_input_1 >> user_input_2))
    #print(bin(user_input_1 << user_input_2))

    print(user_input_1 >> user_input_2)
    print(user_input_1 << user_input_2)

def primeDiscriminant():
    user_input = int(input())
    primeList = list()

    for i in range(1, user_input + 1):
        if user_input % i == 0:
            primeList.append(i)

    if len(primeList) == 2:
        print('True')
    else:
        print('False')

def factorial_N(N):
    if (1 == N):
        return 1
    else:
        return N * factorial_N(N - 1)

# https://www.acmicpc.net/help/rte/RecursionError (여기부터 다시)
# Big-O, Factorial!
def big_O():
    # 1. Library math (Time exceed!)
    # import math
    # fac_str = str(math.factorial(int(input())))

    # 2. Recursive way (Time exceed!)
    # N = int(input())
    # result, j = 1, 1
    # for j in range(N, N == j, -1):
    #    result = result * j
    import sys
    print(sys.getrecursionlimit())
    # 3. Iterative way (Time exceed!)
    N = int(input())
    result = factorial_N(N)

    cnt = 0
    fac_str = str(result)

    for i in range(-1, (len(fac_str) * -1), -1):
        if fac_str[i] == '0':
            cnt += 1
        elif fac_str[i] != '0':
            break
    print(cnt)

if __name__ == '__main__':
    big_O()