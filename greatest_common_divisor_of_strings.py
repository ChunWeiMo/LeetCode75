def gcdOfStrings(str1: str, str2: str) -> str:
    """
    Description
    -
    Find the largest string X such that X divides str1 and X divides str2.
    
    Parameters
    -
    str1: str
    str2: str
    
    return
    -
    str: greatest common divisor
    """
    str1_divisor = ""
    greatest_common_divisor = ""
    for str1_divisor_len in range(1, len(str1)+1):
        if len(str1) % str1_divisor_len == 0:
            concatenate_time = len(str1) // str1_divisor_len
            if str1[0:str1_divisor_len]*concatenate_time == str1:
                str1_divisor = str1[0:str1_divisor_len]
                if len(str2) % str1_divisor_len == 0:
                    concatenate_time = len(str2) // str1_divisor_len
                    if str1_divisor*concatenate_time == str2:
                        greatest_common_divisor = str1_divisor
    return greatest_common_divisor


if __name__ == "__main__":
    print(gcdOfStrings("ABCABC", "ABC"))
    print(gcdOfStrings("ABABAB", "AB"))
    print(gcdOfStrings("LEET", "CODE"))
    
    str1 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    str2 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    
    print(gcdOfStrings(str1, str2))
    print(gcdOfStrings("AA", "A"))
    
    