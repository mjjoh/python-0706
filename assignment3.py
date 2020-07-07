target = input()
rule = (int(input()), str(input()))

if len(target) <= rule[0]:
    print("The number you gave is too large")
else:
    print(target[:rule[0]] + rule[1] + target[rule[0]+1:])
    # 모두 성공