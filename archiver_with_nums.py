def archiver_with_nums(string: str) -> str:
    DIF_STEP: int = 2 #точность шага (во сколько раз уменьшатся размеры выборок)
    DIF_I: int = 1 #точность шага (проверка каждой i-той выборки)
    length: int = len(string) 
    arr: List[str] = ["0"]*length #соответствует каждому символу строки
    step: int = length//2 # шаг
    first: str = "" #выборка для сравнения 
    second: str = "" #выборка для сравнения 
    current: int = 0 #индекс текущей выборки
    i: int = 0 #индекс выборки
    while step > 5:
        i = 0
        while i + step <= length:
            current = i + step
            if not inner_arr(arr, i, i+step):
                first = string[i : i+step]
                while current + step <= length:
                    if not inner_arr(arr, current, current+step):
                        second = string[current : current+step]
                        if first == second:
                            if not inner_arr(arr, i, i+step):
                                for j in range(i, i+step):
                                    arr[j] = f"1"
                            for j in range(current, current+step):
                                    arr[j] = f"{i} {step}"
                    current += 1
            i += DIF_I
        step = step//2
    j: int = 0
    result: str = ""
    curren_char: str = "" 
    index_of_word: int = 0
    len_of_word: int = 0
    while j < length:
        curren_char = arr[j]
        if curren_char == "0" or curren_char == "1":
            if string[j]=="[":
                result += string[j] + "*"
            else:
                result += string[j]
        else:
            index_of_word, len_of_word = map(int, curren_char.split())
            result += f"[{hex(index_of_word)[2:]} {hex(len_of_word)[2:]}]"
            j += len_of_word - 1
        j += 1
    return result


def inner_arr(arr: List[str], left: int, right: int) -> bool:
    for num in range(left, right):
        if arr[num] != "0":
            return True
    return False


