def overlap(s1, s2):
    combined = []
    both = []
    for i in range(len(s1)):
        if s1[i:] == s2[:len(s1) - i]:
            both.append(s1[i:])
            combined.append(s1 + s2[len(s1) - i:])
            break
    for i in range(len(s2)):
        if s2[i:] == s1[:len(s2) - i]:
            both.append(s2[i:])
            combined.append(s2 + s1[len(s2) - i:])
            break
    if len(both) == 0:
        return "", ""

    combined = min(combined, key=len)
    both = max(both, key=len)
    return combined, both


def superstring(strings):
    temp = strings

    while len(temp) > 1:
        s = ""
        list_ = []
        len_ = 0

        for i in range(len(temp) - 1):
            for j in range(i + 1, len(temp)):
                a, b = overlap(temp[i], temp[j])
                # print(temp[i], temp[j], a, b)
                if len(b) > len_:
                    s = a
                    list_ = [temp[i], temp[j]]
                    len_ = len(b)

        temp.remove(list_[0])
        temp.remove(list_[1])
        temp.append(s)

    return temp


if __name__ == "__main__":
    f = open("datas/long.txt")

    raw = f.readlines()

    dict = {}

    print(raw)
    for i in range(len(raw)):
        if (raw[i][0] == '>'):
            dict[raw[i][1:-1]] = ''
            j = i + 1
            while raw[j][0] != '>':
                dict[raw[i][1:-1]] = dict[raw[i][1:-1]] + raw[j][0:-1]
                j += 1
                if j == len(raw):
                    break

    print(dict)

    name, string = [], []
    for key, value in dict.items():
        name.append(str(key))
        string.append(str(value))

    sol = superstring(string)
    print(sol)
