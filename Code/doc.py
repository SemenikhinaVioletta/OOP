from fpdf import FPDF
import xml.etree.ElementTree as ET

def do_doc():
    tree = ET.parse("Status_klient.xml")
    root = tree.getroot()
    s = []
    s.append("# Status\n".split())
    for elem in root.iter():
        if str(elem.text)[0].isalpha() or str(elem.text)[0].isdigit():
            if str(elem.text)[0].isalpha():
                text += str(elem.text)
                text += "\n"  
                s.append(text.split())
            else:
                text = str(elem.text)
                text  += " "

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)

    col_width = pdf.w / 4.5
    row_height = pdf.font_size
    spacing = 1
    for row in s:
        for item in row:
            pdf.cell(col_width, row_height*spacing,
                     txt=item, border=1)
        pdf.ln(row_height*spacing)

    pdf.output("Otchet.pdf")   
