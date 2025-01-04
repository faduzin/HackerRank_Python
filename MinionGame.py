# def minion_game(string):
    # word_set = set(string)
    # char_list = list(string.strip())
    # if not char_list:
    #     return
    
    # for i in range(0, len(string)):
    #     word = ''
    #     for j in range(i, len(string)):
    #         word += char_list[j]
    #         word_set.add(word)
    
    # kevin_score = 0
    # stuart_score = 0

    # for word in word_set:
    #     count = 0
    #     for i in range(len(string) - len(word) + 1):
    #         if string[i:i+len(word)] == word:
    #             count += 1

    #     vowel_list = ['A', 'E', 'I', 'O', 'U']
    #     if word[0] in vowel_list:
    #         kevin_score += count
    #     else:
    #         stuart_score += count
    
    # if kevin_score == stuart_score:
    #     print("Draw")
    # elif kevin_score > stuart_score:
    #     print(f"Kevin {kevin_score}")
    # else:
    #     print(f"Stuart {stuart_score}")
    
    # Optimized version

def minion_game(string):
    kevin_score = 0
    stuart_score = 0
    length = len(string)

    for i in range(length):
        if string[i] in 'AEIOU':  
            kevin_score += (length - i)
        else:
            stuart_score += (length - i)

    if kevin_score > stuart_score:
        print(f"Kevin {kevin_score}")
    elif stuart_score > kevin_score:
        print(f"Stuart {stuart_score}")
    else:
        print("Draw")


if __name__ == '__main__' :
    s = input()
    minion_game(s)

# What I learned:
# 1. My first implementation worked but its complexity
# was innefficient, so I had to search for a way to 
# optimized it
# 2. The way to optimize was more related to finding
# the logic than to know functions