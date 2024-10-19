def countstring(s):
    v = 0  
    c = 0
    w = 0
    q = 0  

    
    vs = {'a', 'e', 'i', 'o', 'u'}
    cs = {'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z'}


    w = len(s.split())

    for char in s.lower():
        if char in vs:
            v += 1
        elif char in cs:
            c += 1
        elif char == '?':
            q += 1

    print("Vowels:", v)
    print("Consonants:", c)
    print("Words:", w)
    print("Question marks:", q)


s = raw_input("Enter a string: ")
countstring(s)

