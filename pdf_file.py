from fpdf import FPDF
class PDF(FPDF):
    def header(self):
        self.image('manu.png',10,8,25)
        self.set_font('helvetica','B',20)
        self.set_text_color(178,34,34)
        pdf_width=self.w
        title_width=self.get_string_width("Manchester United")+ 10
        self.set_x((pdf_width-title_width)/2)
        self.cell(title_width,10,"Manchester United",border=1,ln=1,align='C')
        self.set_text_color(178,34,34)
        self.ln(20)

    def maketable(self,header,value):

        self.set_font('times','',10.0)
        #epw=self.w-2.5*self.l_margin
        cw=self.epw/6              #columnwidth
        rh=self.font_size * 12  #rowheight
        for h in header:
            self.set_fill_color(244, 245, 173)
            self.multi_cell(cw,rh,str(h),border=1,ln=3,align='C',max_line_height=self.font_size,fill=True)
        self.ln(rh)
        for element in value:
            for j in element:
                self.multi_cell(cw,rh,str(j),border=1,ln=3,align='C',max_line_height=self.font_size)
            self.ln(rh)

    def footer(self):
        self.set_font("helvetica","I",10)
        self.set_text_color(88,88,88)
        self.set_y(-15)
        self.cell(0,10,f'Page{self.page_no()}/{{nb}}',align='C')