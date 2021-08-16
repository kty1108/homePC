
'''
# Even & Odd number
if __name__ == '__main__':

    print(10 / 3)
    print(101 % 2)

    print('even') if ((10) % 2) == 0 else print('odd')


# Multiple of 3 & 5, and summarized
# i++ ++i -> not supported in Python
if __name__ == '__main__':

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

'''

# Average & Grade of subjects
if __name__ == '__main__':
    user_input = '0 1 2' #input()

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