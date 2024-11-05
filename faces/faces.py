

def main():
    #print(slow(input()))
    print("\u263A")  # ☺
    print("\u263B")  # ☻
    print(":D")
    print("\U0001F642")
    print("\U0001F641")


def emoticons(s):
    find_emotions = s.plit(' ')
    [x for x in find_emotions if x == ':)' ]
   # slit space and then Join the list back into a string...
    return '...'.join(s.split(' '))

main()
