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


