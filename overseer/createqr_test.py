#!/usr/bin/python3
from fpdf import FPDF
import qrcode

img = qrcode.make('OLALALA')
img.save('test.png')

cardW = 76
cardH = 127
globalOffsetX = 0
#a4Height = 297
#globalOffsetY = a4Height - cardH
globalOffsetY = 0
#card = FPDF(format='A4')
card = FPDF(format=(76, 127))
card.add_page()

qrDesiredW = 40
qrDesiredH = 40
qrX = globalOffsetX + cardW / 2 - qrDesiredW / 2
qrY = globalOffsetY + 2
card.image('test.png', x=qrX, y=qrY, w=qrDesiredW, h=qrDesiredH)
card.set_font('Arial', 'B', 16)
card.text(globalOffsetX + 40, globalOffsetY + 60, 'OLALALA')
card.set_font('Arial', '', 8)
card.text(globalOffsetX + 40, globalOffsetY + 80, 'OLALALA')
card.output('test.pdf', 'F')
