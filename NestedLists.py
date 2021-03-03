if __name__ == '__main__':
    grades = []
    n = int(input())
    for _ in range(n):
        name = input()
        score = float(input())
        grades.append([name, score])
    if n >= 2 and n <= 5:
        grades.sort(key=lambda x: x[1])
        people = []
        for i in grades:
            if i[1] != grades[0][1]:
                if len(people) == 0:
                    people.append(i)
                elif len(people) != 0 and i[1] == people[0][1]:
                    people.append(i)
        people.sort(key=lambda x: str(x[0]))
        for i in people:
            print(i[0])
