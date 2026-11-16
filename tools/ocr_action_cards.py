"""One-off helper used to read the Action cards (A01-A50) from the Vassal images.
OCR was only reliable for the combat table and hit effects; the rest was read visually.
Kept for re-checks: FOF_IMAGES=assets python3 tools/ocr_action_cards.py 1 2 3
"""
import sys, json, re, pytesseract
from PIL import Image, ImageOps
import os
D=os.environ.get('FOF_IMAGES','assets')+'/'
def crop(im,box,scale=4,inv=False,thr=None):
    c=im.crop(box).convert('L'); c=c.resize((c.width*scale,c.height*scale),Image.LANCZOS)
    if inv: c=ImageOps.invert(c)
    if thr: c=c.point(lambda p:255 if p>thr else 0)
    return c
def ocr(c,cfg='--psm 6'): return pytesseract.image_to_string(c,config=cfg).strip()
def card(n):
    im=Image.open(f'{D}A{n:02d}.jpg').convert('RGB')
    r={}
    r['cmd']=ocr(crop(im,(8,8,62,58),thr=128),'--psm 8 -c tessedit_char_whitelist=0123456789')
    r['init']=ocr(crop(im,(58,62,98,105),thr=100),'--psm 8 -c tessedit_char_whitelist=0123456789')
    r['title']=ocr(crop(im,(100,22,268,55),inv=True,thr=120),'--psm 7')
    r['table']=ocr(crop(im,(18,112,100,333),inv=True,thr=110),'--psm 6')
    r['hit']=ocr(crop(im,(100,298,270,334),thr=120),'--psm 6')
    r['rn']=ocr(crop(im,(0,336,274,384),thr=110),'--psm 6')
    r['at']=ocr(crop(im,(170,236,262,272),inv=True,thr=110),'--psm 7')
    return r
if __name__=='__main__':
    for n in map(int,sys.argv[1:]): print(n,json.dumps(card(n)))
