

def main():
    filename = raw_input("enter a file name ")
    with open(filename) as f:
        data = f.readlines()
    out = ""
    for idx,line in enumerate(data[1:]):
        words = line.split()
        words.reverse()
        y = " ".join(words)
        out+="Case #"+str(idx+1)+": "+y+"\n"
    with open(filename.split(".")[0]+".out", 'w') as fi:
        fi.write(out)

if __name__ == "__main__":
    main()
