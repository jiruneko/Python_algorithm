def mul(a, b):
    return a * b

print(mul(4, 7))

def posi_naga_zero(val):
    if val > 0:
        print(val, "正の数です")
    elif val < 0:
        print(val, "負の数です")
    else:
        print(val, "はゼロです")
        
posi_naga_zero(-5)
posi_naga_zero(0.8)

total = 0
def test_func():
    global total
    loops = 20
    for i in range(loops):
        total += 10
        
print("totalの初期値", total)
test_func()
print("関数実行後のtotalの値", total)