from art import * # Generate a smiley face using the 'art' library

def main():
    #print(slow(input()))
    print("\u263A")  # ☺
    print("\u263B")  # ☻
    print(":D")

    smiley_face = text2art(":)")
    print(smiley_face)


def emoticons(s):
    find_emotions = s.plit(' ')
    [x for x in find_emotions if x == ':)' ]
   # slit space and then Join the list back into a string...
    return '...'.join(s.split(' '))

main()
