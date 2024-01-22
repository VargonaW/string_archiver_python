def unarchiver(string:str) -> str:
    result: str = ""
    numbers: str = "0123456789"
    first: str = string[0]
    counter: str = ""
    second: str = ""
    for i in range(1, len(string)):
        second = string[i]
        if second in numbers:
            counter += second
            second = first
        elif counter != "":
            result += first*int(counter)
            counter = ""
        else:
            result += first
        first = second
    result += second
    if counter != "":
        result += first*(int(counter) - 1)
        counter = ""
    return result
