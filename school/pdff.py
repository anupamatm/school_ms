import reportlab    
from reportlab.pdfgen import canvas
import os,sys
 

p = canvas.Canvas('1.pdf')               # Init a PDF object
p.drawString(200, 200, "Hello world.")   # Draw a simple String  
p.showPage()                             # Create the PDF
p.save() 
os.startfile('1.pdf', 'open')