# You have a non-empty set , and you have to execute  commands given in  lines.
# The commands will be pop, remove and discard.

n = int(input())
s = set(map(int, input().split()))
x = int(input())
commands = []
for _ in range(x):
    commands.append(input().split())
for item in commands:
    if item[0] == 'pop':
        s.pop()
    elif item[0] == 'discard':
        s.discard(int(item[1]))
    elif item[0] == 'remove':
        s.remove(int(item[1]))
    else:
        print("Invalid")
print(sum(s))
