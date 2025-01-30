import re
import sys

# sample input:
# <iframe src="http://www.youtube.com/embed/xvFZjo5PgG0"></iframe>
# <iframe width="560" height="315" src="https://www.youtube.com/embed/xvFZjo5PgG0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

# return value:
# https://youtu.be/xvFZjo5PgG0

def main():
    print(parse(input("HTML: ")))


def parse(s):
    pattern = r'src="([^"]+)"'
    match = re.search(pattern, s)

    # <iframe src="https://cs50.harvard.edu/python"></iframe>

    if match:
        url = match.group(1)
        pattern = r'https?:\/\/(www\.)?youtube\.com\/(embed/)?'
        page = re.sub(pattern, "", url)
        return f"https://youtu.be/{page}"

if __name__ == "__main__":
    main()
