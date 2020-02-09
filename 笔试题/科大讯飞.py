import sys


def digui(count, count1):
    if count1 == count:
        return 0
    a_muti = 1
    for i in range(1, count1+1):
        a_muti *= i
    a_muti += 1
    a_muti *= count1
    return sum((a_muti, digui(count, count1+1)))




if __name__ == "__main__":
    count = int(sys.stdin.readline().strip())
    num = int(sys.stdin.readline().strip())
    print(num*count + digui(count, 1))

