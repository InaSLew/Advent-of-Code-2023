import re

NUMBER_LITERALS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

with open('input.txt') as f:
    sum = 0
    raw = f.read()
    temp = ''
    for line in raw.split("\n"):
        for letter in line:
            temp += letter
            if (any(nl in temp for nl in NUMBER_LITERALS)):
                for n in NUMBER_LITERALS:
                    p = re.compile(n)
                    t = p.search(temp)
                    if (t):
                        temp = t.group()
                        startIdx = line.index(temp)
                        line = line.replace(temp, str(NUMBER_LITERALS.index(temp) + 1), 1)
                        temp = ''
                
        # ready for calculation
        digitsOnly = list(filter(lambda x: x.isdigit(), line))
        sum += int(f"{digitsOnly[0]}{digitsOnly[0]}") if len(digitsOnly) == 1 else int(f"{digitsOnly[0]}{digitsOnly[-1]}")
    
    print(sum)