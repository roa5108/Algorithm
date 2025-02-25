while True:
    a, b, c = map(int, input().split())

    if a == b == c == 0:
        break

    slides = [a, b, c]
    max_slide = max(slides)
    remain_slides = sum(slides) - max_slide

    if a == b == c:
        print("Equilateral")
    elif max_slide >= remain_slides:
        print("Invalid")
    elif a == b or a == c or b == c:
        print("Isosceles")
    else:
        print("Scalene")