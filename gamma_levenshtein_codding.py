from base_numeral_system import base_ns


def get_first(data:list):
    return data[:1], data[1:]


def add_flags(data: list):
    result = []
    for element in data:
        result.append(0)
        result.append(element)
    return result + [1]


def encode_word(item: int):
    code = base_ns.convert(item, 2).integer[1:]
    code.reverse()
    return add_flags(code)


def encode(data: list):
    # Encode phrase
    result = []
    for item in data:
        result += encode_word(item)
    return result


def decode(k: list):
    k = k[:]

    result = []

    test = []

    while (len(k)) > 0:
        flag, k = get_first(k)
        if flag == [0]:
            data, k = get_first(k)
            test += data
        else:
            test += flag
            test.reverse()
            n = int(base_ns.convert_to_dec(base_ns.NumberBased(2, test)))
            test = []
            result.append(n)
    return result
