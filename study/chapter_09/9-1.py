# 9장 오류를 방지하고 해결하기
# 9.1 오류의 종류

# 구문오류 : syntax error
# 실행오류 : runtime error
# 논리오류 : logical error

field_animal = {'사자', '박쥐', '늑대', '곰'}
fly_animal = {'독수리', '매', '박쥐'}
# land_animal = fly_animal + field_animal

# print('육지생물: ', land_animal)
# TypeError: unsupported operand type(s) for +: 'set' and 'set'

# 에러 수정
land_animal = fly_animal | field_animal
# print('육지생물: ', land_animal)

def half_and_half(s):
    center = len(s) // 2
    return (s[:center], s[center:])

# print(half_and_half('코드'))
# print(half_and_half('코드리스'))

# print(half_and_half(''))
# print(half_and_half('?'))
# print(half_and_half('코드리'))


# 테스트 주도 개발
def frequency(s, c):
    """문자열 s와 문자 c를 입력받아, c가 s에 등장하는 빈도를 구한다.
    테스트:
        * 'banana', 'a'     => 0.5
        * 'code', 'c'       => 0.25
        * '파이썬', '프'    => 0
        * '파이썬', '파이'  => None
        * '', 'a'           => 0
    """

    if len(c) != 1:
        return None

    if len(s) == 0:
        return 0

    count = s.count(c)
    return count / len(s)

print(frequency('banana', 'a') == 0.5)
