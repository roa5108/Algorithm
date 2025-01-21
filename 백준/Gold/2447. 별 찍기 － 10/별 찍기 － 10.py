def star(n):
    result = []
    if n == 1:
        return "*"

    smaller_pattern = star(n // 3)
    result = []

    for line in smaller_pattern:
        result.append(line * 3)

    for line in smaller_pattern:
        result.append(line + " " * (n // 3) + line)

    for line in smaller_pattern:
        result.append(line * 3)

    return result

print("\n".join(star(int(input()))))
