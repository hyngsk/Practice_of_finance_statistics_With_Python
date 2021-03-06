# %% [과제 3-1] 주사위를 두 번 던져서 생성된 값을 저장하고 두 숫자의 최대공약수를
# 계산하고 다음을 출력하는 코드를 작성하세요. "첫번째 수를 입력해주세요: 3
# 두번째 수를 입력해주세요: 6
# 3와 6의 최대공약수는 3입니다."
# hint: 최대공약수는 영어로 Greatest Common Divisor라고 합니다.
# 최대공약수를 반환하는 파이썬 함수를 인터넷 검색하세요.

# math 의 gcd(?, ?)함수를 사용하기 위함
import math

# 입력
x = int(input("첫 번째 수를 입력해주세요. : "))
y = int(input("두 번째 수를 입력해주세요. : "))

# 출력
print(x, ", ", y, "의 최대공약수는", math.gcd(x, y), "입니다. ")
