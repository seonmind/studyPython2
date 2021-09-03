'''
function: general purpose
method: belongs to specific object or type

string method

[]로 문자열의 특정 인덱스의 캐릭터 접근 가능
find(): 문자열이나 캐릭터를 찾아줌
index(): find랑 같지만 찾는게 없을때 -1 대신 error 띄움
count(a,b,c): 문자열에서 b와 c 인덱스 사이에 a가 몇번 등장하는지

replace(a,b): 문자열의 a부분을 b로 바꿔줌
strip(): 문자열 앞 뒤의 공백 제거  lstrip()
strip(a)
split(a): a를 seperator로 하여 문자열을 잘라서 리스트로 반환
splitlines()
rpartition(a): a 기준으로 문자열을 세덩이로 잘라 튜플로 반환


a in b: a의 문자열이 b에 포함되어 있으면 참 거짓으로 답함

center(a,b): 문자열을 a 길이로 만들어서 공백을 b로 체워줌
ljust(숫자): 문자열을 숫자 길이로 만든뒤 공백


format(a): {}내부를 a를 포맷해서 변환한 string으로 체워줌
        formatting type: {:?} ?에 따라 어떤식으로 formatting하는지가 바뀜
        -정렬(좌우 중앙)
            <숫자: 숫자만큼 칸을 마련한뒤 좌로정렬 / >숫자
            ^숫자: 가운데 정렬
        -부호/천단위 숫자/소숫점
            +: 플마 다 표시
            -: 음수만 표시
            , / _
            .숫자
        zfill: 0으로 정해진 만큼 체움
        
is? : ?에따라 특정한 조건을 만족하는 캐릭터들로 이루어졌는지 확인 가능

'''
