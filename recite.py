#!/usr/bin/env python3
import csv
import random
import argparse

parser = argparse.ArgumentParser(description="recite")
parser.add_argument("-a", dest="a", default=0, type=int, help="begin")
parser.add_argument("-b", dest="b", default=0, type=int, help="end")
parser.add_argument("-f", dest="file", default="all.csv", type=str, help="word file")
parser.add_argument(
    "-o", dest="wrong", default="wrong.csv", type=str, help="wrong answer output"
)
args = parser.parse_args()

with open(args.file, newline="", encoding="utf-8") as csvfile:
    reader = csv.reader(csvfile)
    data = list(reader)

if args.a and args.b:
    data = data[args.a : args.b]
elif args.b:
    data = data[: args.b]
elif args.a:
    data = data[args.a :]

while len(data) > 0:
    print(f"Number of words: {len(data)}")
    print("Type 'exit' to quit")
    print("")
    wrong = []
    random.shuffle(data)
    for idx, row in enumerate(data):
        word = row[0]
        chinese = row[1]
        english = row[2]
        ipt = input("\033[1;34;48m%03d \033[0m %s: " % (idx + 1, word))
        if ipt.lower() in ["exit", "quit"]:
            exit()
        print("\033[1;32;48m+\033[0m %s" % chinese)
        # print("\033[1;32;48m+\033[0m %s" % english)
        print("\033[1;31;48m-\033[0m %s" % ipt)

        if input("Correct? [y]/n: ").lower() == "n":
            wrong.append(row)
            print("Added to %s" % args.wrong)
        print("")

    if wrong:
        print(
            f"\033[1;31;48mWriting {len(wrong)} wrong answers into {args.wrong} \033[0m"
        )
        with open(args.wrong, "w", newline="", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(wrong)
        data = wrong
    else:
        print("\033[1;32;48mCongrats! All answers correct!\033[0m")

    if input("Repeat? [y]/n: ").lower() == "n":
        break
    print("")
