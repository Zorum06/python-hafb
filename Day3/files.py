#!/usr/bin/env python3
"""
Author : t23 <me@wsu.com>
Date   : 8/11/2021
Purpose:
"""


import sys



# --------------------------------------------------
def main():
    """Make your noise here"""
    print(sys.getdefaultencoding())
    f = open('wasteland.txt', mode='wt', encoding='utf-8')
    f.write('This is the first line\n')
    f.write('But, I can write more lines if I need to')
    f.close()

    g = open('wasteland.txt', mode='rt', encoding='utf-8')
    info = g.read(27)
    print(f'[{info}]')
    info = g.read()
    print(f'[{info}]')
    info = g.readlines()
    print(f'{info}')
    g.close()

    # appending text to files
    f = open('wasteland.txt', mode='at', encoding='utf-8')
    f.writelines(['Son of man',
                  'for you know only',
                  'this is the end'])
    f.close()



# --------------------------------------------------
if __name__ == '__main__':
    main()
