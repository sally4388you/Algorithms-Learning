# Python program for KMP Algorithm
def KMPSearch(pattern, text):
    lenText = len(text)
    lenPattern = len(pattern)
    
    # create lps[] that will hold the longest prefix suffix
    # Preprocess the pattern (calculate lps[] array)
    lps = computeLPSArray(pattern)
    print(lps)
    # indices
    i = 0 # index for text[]
    j = 0 # index for pattern[]

    while i < lenText:
        if text[i] == pattern[j]:
            i += 1
            j += 1
 
            if j == lenPattern:
                print ("Found pattern at index", str(i-j))
                j = lps[j-1]

        # mismatch after j matches
        else:
            # Do not match lps[0..lps[j-1]] characters,
            # they will match anyway
            if j != 0:
                j = lps[j-1]
            else:
                i += 1

        # if text[i] == pattern[j]:
        #     i += 1
        #     j += 1
 
        # if j == lenPattern:
        #     print ("Found pattern at index", str(i-j))
        #     j = lps[j-1]
 
        # # mismatch after j matches
        # elif i < lenText and pattern[j] != text[i]:
        #     # Do not match lps[0..lps[j-1]] characters,
        #     # they will match anyway
        #     if j != 0:
        #         j = lps[j-1]
        #     else:
        #         i += 1

    return
 
def computeLPSArray(pattern):
    lps = [0] * len(pattern)
    length = 0 # length of the previous longest prefix suffix
 
    i = 1
    # the loop calculates lps[i] for i = 1 to M-1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            # This is tricky. Consider the example.
            # AAACAAAA and i = 7. The idea is similar
            # to search step.
            if length != 0:
                length = lps[length-1]
 
                # Also, note that we do not increment i here
            else:
                lps[i] = 0
                i += 1

    return lps
 
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
KMPSearch(pattern, text)