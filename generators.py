import time
import os
import glob
from Xlib import display
from random_words import RandomWords
import random


def chain(iterable_one, iterable_two):
    for item in iterable_one:
        yield item
    for item in iterable_two:
        yield item

def compress(iterable, mask):
    for i in range(len(iterable)):
        if mask[i]:
            yield iterable[i]

def cycle(iterable):
    idx = 0
    while True:
        time.sleep(0.1)
        yield iterable[idx]
        idx = iterate_index(idx, len(iterable))

def iterate_index(i, lngth):
    i += 1
    if i ==lngth:
        return 0
    return i

def book_parser(folderpath):
    page_idx = 1
    path = folderpath + "/" + "{0:03d}".format(page_idx, '03') + ".txt"
    files = glob.glob(folderpath + '/*.txt')
    for file in files:
        with open(file, "r") as input_data:
            content = ""
            for line in input_data:
                if line[0] == '#':
                    yield content
                    content = line
                else:
                    content += line

        page_idx += 1
        path = folderpath + "/" + "{0:03d}".format(page_idx, '03') + ".txt"

def waitforspace(f1, arg):
    if input() == " ":
        return f1(arg)
    else:
        waitforspace(f1, arg)

def book_reader(folderpath):
    book = book_parser(folderpath)
    for chapter in book:
        chapter
        # IMPORTANT! The print part only works on python >= 3
        waitforspace(print, chapter)


# IMPORTANT!
# Turns out the RandomWords library only works on python2 so this doesnt actually work on python3
def book_generator(filepath, chapters, chapter_len):
    rw = RandomWords()
    file = open(filepath, "w")
    file.write("#Chapter 0")
    file.write("\n")
    for chapt in range(2, chapters):
        for word in range(chapter_len):
            file.write(rw.random_word() + " ")
            if random.randrange(15) == 3:
                file.write("\n") 
        file.write("\n")  
        file.write("\n")
        file.write("#Chapter " + str(chapt))
        file.write("\n")
    file.close()


def wait_for_beep():
    while True:
        pointer = display.Display().screen().root.query_pointer()
        if pointer.root_x == 0 and pointer.root_y == 0:
            break
    yield "I've beeped"

def mouse_beep():
    result = wait_for_beep()
    for res in result:
        print(res)



