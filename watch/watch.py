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
    if 'youtube.com' not in s or '<iframe' not in s:
        return None
    pattern = r'src="(http(?:s)?[^"]+)"'

    #pattern = r'http(?:s):\/\/(?:www\.)?youtube\.com\/(?:embed/)?'
    match = re.search(pattern, s)

    # <iframe src="https://cs50.harvard.edu/python"></iframe>

    if match:
        url = match.group(1)
        pattern = r'https?:\/\/(www\.)?youtube\.com\/(embed/)?'
        page = re.sub(pattern, "", url)

        if url != page:
            return f"https://youtu.be/{page}"
        else:
            return None

if __name__ == "__main__":
    main()
