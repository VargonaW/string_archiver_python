def archiver(string: str) -> str:
    result: str = ""
    first: str = string[0]
    counter: int = 1
    second: str = ""
    if first in "0123456789":
        return ""
    for i in range(1,len(string)):
        second = string[i]
        if second in "0123456789":
            return ""
        if first == second:
            counter += 1
        else:
            result += first
            if counter != 1 and first != " ":
                result += str(counter)
            counter = 1
        first = second
    result += second
    if counter != 1 and first != " ":
        result += str(counter)
    return result

