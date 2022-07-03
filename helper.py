from game import WordleGame

def main():
    with open("words.csv", 'r') as fr:
        datalib = fr.read().splitlines()
    game = WordleGame(datalib, datalib)

    wordlist = datalib.copy()
    while True:
        # Suggestion
        if len(wordlist) < 1000:
            scores, bw = game.findBestGuess(wordlist)
            print("Recommand Guess: ", bw[-5:])
        else:
            bw = ["share"]
            print("Recommand Guess: [store, share]")
        print("Please input guess(r to reset, blank to recommand)")
        cmd = input("> ").lower()

        if cmd == 'r':
            print("Game Reset!")
            print()
            wordlist = datalib.copy()
            continue
        elif cmd == "":
            cmd = bw[-1]
        print("Please input result list(0,1,2)")
        cmd2 = input("> ")
        result = [int(x) for x in cmd2]
        wordlist = game.findNext(cmd, result, wordlist)
        print("Result Numbers: %d" % len(wordlist))
        if len(wordlist) == 1:
            print("Final Answer! %s" % wordlist[0])
        elif len(wordlist) == 0:
            print("Bad Game! No result.")


if __name__ == "__main__":
    main()