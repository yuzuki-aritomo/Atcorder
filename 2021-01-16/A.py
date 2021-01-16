import io
import sys

_INPUT = """\
20
715806713 926832846 890153850 433619693 890169631 501757984 778692206 816865414 50442173 522507343 546693304 851035714 299040991 474850872 133255173 905287070 763360978 327459319 193289538 140803416
974365976 488724815 821047998 371238977 256373343 218153590 546189624 322430037 131351929 768434809 253508808 935670831 251537597 834352123 337485668 272645651 61421502 439773410 621070911 578006919
"""
sys.stdin = io.StringIO(_INPUT)

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

C = [0]*n

ans = A[0]*B[0]
for i in range(n):
    
    if((i !=0 and A[i-1]<A[i]) or (i !=0 and B[i-1]<B[i])):
        for k in range(i+1):
            if(ans < A[k] * B[i]):
                ans = A[k] * B[i]
    
    C[i] = ans

for item in C:
    print(item)

