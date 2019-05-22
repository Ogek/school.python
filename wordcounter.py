from collections import defaultdict
import sys


def count_words(text):
    words = defaultdict(int)
    for w in text.split():
        words[w] += 1
    return words


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print('Usage:', sys.argv[0], '<text_file>')
        exit(-1)

    try:
        fo = open(sys.argv[1], mode='r', encoding='utf-8')
    except IOError:
        print('The input file does not exist')
        exit(-1)
    except OSError:
        print('The input file cannot be open')
        exit(-1)
    except UnicodeDecodeError:
        print('The input file cannot be decoded in UTF-8')
        exit(-1)
    d = count_words(fo.read())
    fo.close()
    for w in sorted(d, key=d.get, reverse=True)[:10]:
        print('Occurrences: {:>3} Word: {} '.format(d[w], w))
