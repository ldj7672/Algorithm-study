"""
@문제 문자열 재정렬

알파벳 대문자와 숫자로만 구성된 문자열이 입력으로 주어진다.
이때 모든 알파벳을 오름차순으로 정렬하여 이어서 출력한 뒤에, 그 뒤에 모든 숫자를 합친 값을 이어서 출력한다.
예를 들어 K1KA5CB7 이 입력되며 ABCKK13을 출력한다.

@풀이
입력받은 str에서 하나씩 보면서 알파벳인지 숫자인지 확인해서 따로 저장하고,
알파벳은 정렬하고, 숫자는 더해서 뒤에 연결해준다.

아래 2개 활용

str.isalpa() : 알파벳인지 아닌지
''.join(str) : 리스트 에서 '' 떼고 전부 연결해서 문자열로 만듬
"""

data = input()
result = []
value = 0

for x in data:
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

result.sort()

if value != 0:
    result.append(str(value))

print(''.join(result))
