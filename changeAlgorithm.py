n = int(input('금액을 적어주세요: '))
arr = [ 500, 100, 50, 10]
count = 0

print('     거스름돈')
print(f'{n}원을 500원, 100원, 50원, 10원으로 거스름돈을 반환 합니다.')
for coin in arr:
    count += n // coin
    print(f'{coin}원\t=>\t{n // coin}개')
    n %= coin

    
