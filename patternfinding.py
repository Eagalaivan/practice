def search(pat, txt):
    count=0
    M = len(pat)
    N = len(txt)
    for i in range(N- M + 1):
        j = 0
        while(j < M):
            if (txt[i + j] != pat[j]):
                break
            j += 1
        if (j == M):
            count+=1
    print("Patternfound "+str(count)+" times")
txt = "weliveinsociety"
pat = "live"
search(pat, txt)