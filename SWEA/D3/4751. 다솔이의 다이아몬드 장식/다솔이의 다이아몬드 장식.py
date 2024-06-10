for t in range(1, int(input())+1):
    word = input()

    line1 = ""
    line2 = ""
    line3 = ""
    line4 = ""
    line5 = ""

    for i in range(len(word)):
        line1 += "..#."
        line2 += ".#.#"
        line3 += f"#.{word[i]}."
        line4 += ".#.#"
        line5 += "..#."

    print(line1+'.')
    print(line2+'.')
    print(f"{line3}#")
    print(line4+'.')
    print(line5+'.')
