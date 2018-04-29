import random
import sys
import shutil
import os
from multiprocessing import Process


def filler(src, dst):
    print("Started filler...")
    try:
        while 1:
            filename = random.randint(1, 999999)
            try:
                shutil.copy(src, os.path.join(dst, str(filename)))
            except FileExistsError:
                continue
    except OSError:
        print("Destination has no more space left. Done")
        sys.exit(0)


if __name__ == '__main__':
    if sys.version_info[0] < 3:
        print("Requires python 3+ to run")
        sys.exit(1)
    print("Starting to fill destination with source file. Please wait...")
    src = sys.argv[1]
    dst = sys.argv[2]

    p1 = Process(target=filler, args=(src, dst))
    p2 = Process(target=filler, args=(src, dst))
    p3 = Process(target=filler, args=(src, dst))
    p4 = Process(target=filler, args=(src, dst))

    p1.start()
    p2.start()
    p3.start()
    p4.start()

    p1.join()
    p2.join()
    p3.join()
    p4.join()
