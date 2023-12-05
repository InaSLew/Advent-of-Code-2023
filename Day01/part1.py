with open('input.txt') as f:
    raw = f.read()
    result = sum([int(f"{numbers[0]}{numbers[0]}") if len(numbers) == 1 else int(f"{numbers[0]}{numbers[-1]}") for numbers in [list(filter(lambda x: x.isdigit(), list(line))) for line in raw.split("\n")]])
    print(result)