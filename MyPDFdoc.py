#encoding=utf-8
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfbase import pdfmetrics
pdfmetrics.registerFont(TTFont('msyh', 'msyh.ttf'))
# from graphs import *
# from dataPackage import *
from reportlab.platypus import SimpleDocTemplate,Paragraph,PageTemplate,FrameBreak
from reportlab.lib.units import inch
from reportlab.lib.styles import getSampleStyleSheet
import time

class MyPDFdoc():
    normalStyle = getSampleStyleSheet()['Normal']
    
    def __init__(self,filename):

        self.stories=[]
        self.doc=SimpleDocTemplate(filename,pagesize=(12*inch,16*inch))
        # curr_date = time.strftime("%Y-%m-%d", time.localtime())
        # right center
    def drawpdf(self,fontSize,align,content):
        # stylesheet = 
        # normalStyle = stylesheet

        image_title='<para autoLeading="off" fontSize='+fontSize+' align='+align+'><b><font face="msyh">'+content+'</font></b><br/></para>'
        self.stories.append(Paragraph(image_title,MyPDFdoc.normalStyle))

    def buildpdf(self):
        self.doc.build(self.stories)
        pass
if __name__=="__main__":
    pdf=MyPDFdoc('my1pdf.pdf')
    pdf.drawpdf("12","center","12312")
    pdf.buildpdf();