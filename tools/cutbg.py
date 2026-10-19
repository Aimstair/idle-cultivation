import sys
from collections import deque
from PIL import Image, ImageFilter
def cut(src,dst,mode):
    im=Image.open(src).convert('RGB'); w,h=im.size; px=im.load()
    if mode=='light': isbg=lambda c: min(c)>=212 and max(c)-min(c)<=14
    else: isbg=lambda c: max(c)<=10
    bg=bytearray(w*h); q=deque()
    for x in range(w):
        for y in (0,h-1): q.append((x,y))
    for y in range(h):
        for x in (0,w-1): q.append((x,y))
    while q:
        x,y=q.popleft(); i=y*w+x
        if bg[i] or not isbg(px[x,y]): continue
        bg[i]=1
        if x>0: q.append((x-1,y))
        if x<w-1: q.append((x+1,y))
        if y>0: q.append((x,y-1))
        if y<h-1: q.append((x,y+1))
    a=Image.frombytes('L',(w,h),bytes(0 if b else 255 for b in bg))
    a=a.filter(ImageFilter.MinFilter(3)).filter(ImageFilter.GaussianBlur(0.8))
    out=im.convert('RGBA'); out.putalpha(a); out.save(dst,optimize=True)
cut(sys.argv[1],sys.argv[2],sys.argv[3])
