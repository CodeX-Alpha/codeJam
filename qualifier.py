from typing import Any, List, Optional

charList = ['│', '─', '┌', '┬', '┐', '├', '┼', '┤', '└', '┴', '┘']


def make_table(rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False) -> str:
    if not lencheck(rows, labels):
        return "Error with Information"
    lengthCheck(rows, labels)
    String, Label = "", ""

    if labels is not None:
        for k in range(len(labels)):
            if not centered:
                Label += charList[0] + " " + str(labels[k]) + \
                         (" " * ((lengthCheck(rows, labels)[k] - len(str(labels[k]))) + 1))
            else:
                Label += centre(lengthCheck(rows, labels)[k], str(labels[k]))
        Label += charList[0] + "\n"

    for i in range(len(rows)):
        Start, End = charList[2], charList[8]
        if labels is not None:
            Mid = charList[5]

        for j in range(len(rows[i])):
            if not centered:
                Element = charList[0] + " " + str(rows[i][j]) + \
                          (" " * ((lengthCheck(rows, labels)[j] - len(str(rows[i][j]))) + 1))
            else:
                Element = centre(lengthCheck(rows, labels)[j], str(rows[i][j]))

            String += Element
            if j != len(rows[i]) - 1:
                Start += charList[1] * (len(Element) - 1) + charList[3]
                End += charList[1] * (len(Element) - 1) + charList[9]
                if labels is not None:
                    Mid += charList[1] * (len(Element) - 1) + charList[6]
            else:
                Start += charList[1] * (len(Element) - 1) + charList[4]
                End += charList[1] * (len(Element) - 1) + charList[10]
                if labels is not None:
                    Mid += charList[1] * (len(Element) - 1) + charList[7]

        String += charList[0] + "\n"

    if labels is not None:
        String = Start + "\n" + Label + Mid + "\n" + String + End
    else:
        String = Start + Label + "\n" + String + End
    return String


def lengthCheck(r, l=None):
    Maximum = []
    for a in range(len(r[0])):
        Maximum += [0]
        for b in range(len(r)):
            if len(str(r[b][a])) > Maximum[a]:
                Maximum[a] = len(str(r[b][a]))

    if l is not None:
        for c in range(len(l)):
            if len(str(l[c])) > Maximum[c]:
                Maximum[c] = len(str(l[c]))
    return Maximum


def centre(max_len, ele):
    Centred = ""
    space = max_len - len(ele)

    if space % 2 == 0:
        Centred += charList[0] + (" " * ((space // 2) + 1)) + ele + (" " * ((space // 2) + 1))
    else:
        Centred += charList[0] + (" " * ((space // 2) + 1)) + ele + (" " * ((space // 2) + 2))

    return Centred


def lencheck(main, side):
    if len(main) > 1:
        for i in range(len(main) - 2):
            if len(main[i]) != len(main[i + 1]):
                return False
            else:
                return True
        print(side)
        if side is not None:
            if len(main[0]) != len(side):
                return False
            else:
                return True
    else:
        return True


table = make_table(rows=[['Apple', 5, 70, 'Red', 76], ['Banana', 3, 5, 'Yellow', 8], ['Cherry', 7, 31, 'Red', 92],
                         ['Kiwi', 4, 102, 'Green', 1], ['Strawberry', 6, 134, 'Red', 28]],
                   labels=['Fruit', 'Tastiness', 'Sweetness', 'Colour', 'Smell'],
                   centered=True)

print(table)
