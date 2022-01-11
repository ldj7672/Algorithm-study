"""문제
각 자리가 숫자로만 이루어진 문자열 S가 주어질 때, 왼쪽부터 오른쪽으로 하나씩 모든 숫자를 확인하며 숫자 사이에 'x' 또는 '+'연산자를 넣어
결과적으로 만들 수 있는 가장 큰 수를 구하는 프로그램을 작성하세요. (단, 모든 연산은 왼쪽에서부터 순서대로 이루어짐)
"""
"""해설
두 수 중에서 하나라도 1이하(0,1) 이면 더하고 나머지 경우엔 곱하면 된다
"""

data = input()
result = int(data[0])

for i in range(1,len(data)):
    num = int(data[i])
    if num<=1 or result <=1 :
        result+=num
    else :
        result*=num

print(result)
