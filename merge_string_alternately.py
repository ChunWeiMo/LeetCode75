def mergeAlternately(word1: str, word2: str) -> str:
    """
    Description
    -
    You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

    Return
    -
    Merged string.    
    """
    if len(word1) < 1 or len(word2) < 1:
        raise ValueError("Length must be greater or equal to 1.")

    position_1 = 0
    position_2 = 0
    merge_string = ""

    while position_1 < len(word1) or position_2 < len(word2):
        if position_1 == len(word1):
            merge_string += word2[position_2:]
            break
        elif position_2 == len(word2):
            merge_string += word1[position_1:]  
            break
        elif position_1 <= position_2:
            merge_string += word1[position_1]
            position_1 += 1
        else:
            merge_string += word2[position_2]
            position_2 += 1
    return merge_string


def main():
    word1 = "abc"
    word2 = "pqr"
    try:
        print(mergeAlternately(word1, word2))
    except ValueError as e:
        print(e)
    
    word1 = "ab"
    word2 = "pqrs"
    try:
        print(mergeAlternately(word1, word2))
    except ValueError as e:
        print(e)
    except IndexError:
        print("out of range")

    word1 = "abcd"
    word2 = "pq"
    try:
        print(mergeAlternately(word1, word2))
    except ValueError as e:
        print(e)
    except IndexError:
        print("out of range")


if __name__ == "__main__":
    main()
    