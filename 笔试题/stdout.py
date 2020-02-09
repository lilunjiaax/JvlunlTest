from tqdm import tqdm
import time
import sys

for i in tqdm(range(100)):
    time.sleep(.1)
for i in range(100):
    a = (i + 1) / 5
    b = 20 - a
    # sys.stdout.write('\r>>convert image %d/%d'%(i,b))

    sys.stdout.write('\r|%s%s|%d%%' % (a * ' ', b * ' ', i + 1))
    sys.stdout.flush()
    time.sleep(.1)


