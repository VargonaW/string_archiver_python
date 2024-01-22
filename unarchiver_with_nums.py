def unarchiver_with_nums(string: str) -> str:
    length: int = len(string)
    result: str = ""
    i: int = 0 
    word: str = ""
    index_of_word: str = 0
    len_of_word: str = 0
    while i < length:
        if string[i] == "[":
            if string[i+1] == "*":
                result += string[i]
                i += 1
            else:
                i += 1
                word = ""
                while string[i] != "]":
                    word += string[i]
                    i += 1
                index_of_word, len_of_word = word.split()
                for j in range(int(len_of_word, 16)):
                    result += result[int(index_of_word, 16) + j]
        else:
            result += string[i]
        i += 1
    return result
