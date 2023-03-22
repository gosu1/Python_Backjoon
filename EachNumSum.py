"""
def sumOfDigits():
    
    입력받은 값을 리스트에 넣고싶을 때
    a = input()-> list = [] -> list.append(a)
    
    n = input
    n_list = list(map(int, str(n)))
    print(n_list)
    
    return
"""

n = input()
n_list = list(map(int, str(n)))
print(n_list)
print(sum(n_list))

#sum() 리스트 안에 있는 원소 모두 더하기
#리스트안에 있는 원소들을 하나씩 더해가기
#for 문으로 n_list[0:i+1]

'''
리스트를 만들어서 -> 하나씩 잘라서 -> 그변수들을 다 더한값을 출력
'''
