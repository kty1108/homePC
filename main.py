# July 31th 2021, by Ted
# Accounts for substituting capital alphabet characters to small one.

'''
> 변수 초기화
0. None          : var_none = None      -> None Type
1. Numeric 변수   : var_num = int(), var_num = 0, var_num = int(0x00)
2. Boolean 변수   : var_bool = bool(), var_bool = bool(False), var_bool = bool(0)
3. String 변수    : var_str = str(), var_str = 'test str', var_str = ('test str')
4. List 변수      : var_list = list(), var_list = []                                                    -> Mutable
5. Tuple 변수     : var_tuple = tuple(), var_tuple = (), var_tuple = 'test string',(쉼표)               -> Immutable
    list() 함수로 형변환 가능 (Tuple형 -> List형)
6. Set 변수       : var_set = set()
7. Dict 변수      : var_dict = dict()

> 리스트 변수의 조작
1. 객체 추가         : var_list.append([3, 4])  -> [1, 2, [3, 4]]
2. 요소 추가         : var_list.insert([3, 4])  -> [1, 2, 3, 4]
3. 특정 위치에 추가   : var_list.insert(-1, 100) -> [1, 2, 3, 100, 4]

> 사전형 변수의 조작
1. 초기화          : var_dict = dict()
2. Key:값 추가     : var_dict['black'] = 100, var_dict = {'red': 101, 'green':102}
3. Key:값 제거     : del var_dict['black']

> 패킹 & 언패킹
- index가 있는 쪽에 *로 표시함
- 함수의 매개변수로 인수 값을 보낼 때, 리스트형/사전형을 각각 묶어서(packing)/풀어서(un-packing) 전달해주는 기능
- 언패킹 -> 만약 numbers = [1, 2, 3] 리스트 변수가 있다고 가정할 때,
sum(*numbers)
sum(*[1, 2, 3])
sum(1, 2, 3)

> 사용자 입출력 처리
1. 2개 숫자 입력
len_A, len_b = map(int, input().split())

2. str 분할 입력 (list형)
array_A = input().split()

3. str 배열의 int형 변환 (연산 처리용)
array_C = list(map(int, array_C))

4. int 배열의 str형 변환
tmp_str = str(array_C)

5. str 배열의 괄호 및 쉼표 제거
print(tmp_str[1:-1].replace(', ', ' '), '')


'''


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

# GCD, Greatest Common Divisor between A and B
def euclideanAlgorithm():
    a, b = map(int, input().split())

    r = int()
    r = 1

    while (r):
        r = a % b

        if (r == 0):
            print(b)
            break

        a = b
        b = r

def mergeArrays():
    # len_A, len_b = map(int, input().split())
    array_A = input().split()
    array_B = input().split()
    array_C = list()

    # print(type(array_A))
    # print(type(array_B))

    array_C = array_A + array_B
    # print(type(array_C[0]))

    array_C = list(map(int, array_C))
    # print(array_C)

    array_C.sort()
    # print(array_C)

    tmp_str = str(array_C)
    print(tmp_str[1:-1].replace(', ', ' '), '')

# Binary Search, O(logN) mean better performance, than Linear Search, O(N)
def binarySearch():
    len_A = int(input())        # length of the list
    array_A = input().split()   # a list provided
    target = int(input())       # a value to search

    array_A = list(map(int, array_A))
    array_A.sort()
    # print(array_C)

    low, mid, high = 0, 0, 0
    high = len_A - 1

    while low <= high :
        mid = int((high + low) / 2)
        print('low: ', low, '\tmid: ', mid, '\thigh: ', high)
        #input()

        if array_A[mid] == target :
            print(mid + 1)
            break
        elif array_A[mid] < target :
            low = mid + 1
        elif array_A[mid] > target :
            high = mid - 1

    if array_A[mid] != target :
        print('X')


if __name__ == '__main__':
    binarySearch()