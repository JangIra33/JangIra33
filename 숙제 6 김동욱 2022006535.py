def digit_ranking_board(file):
    infile = open(file,"r")
    outfile = open("ranking.txt", "w")
    ds = infile.read()
    sum = 0
    def digit_frequencies(ds):
        digits_count = [0 for _ in range(10)]
        for d in ds:
            digits_count[int(d)] += 1
        paired = []
        i = 0
        for dc in digits_count:
            paired.append([i,dc])
            i += 1
        return paired
    paired = digit_frequencies(ds)
    for i in paired:
        sum += i[1]
    paired.sort(key=lambda x: x[1], reverse=True)
    for i in paired:
        outfile.write("%d %d %.1f%%\n" %(i[0],i[1],i[1]/sum*100))
    infile.close()
    outfile.close()
digit_ranking_board("digits.txt")
