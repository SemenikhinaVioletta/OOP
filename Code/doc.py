from fpdf import FPDF
import xml.etree.ElementTree as ET

def do_doc():
    """
    This function reads data from an XML file, processes it, and generates a PDF report.

    Parameters:
    None

    Returns:
    None

    The function performs the following steps:
    1. Parses the XML file "Status_klient.xml" using the ElementTree module.
    2. Retrieves the root element of the XML tree.
    3. Prints "Make array" to the console.
    4. Initializes an empty list 's' and appends a split version of the string "# Status\n" to it.
    5. Iterates over all elements in the XML tree.
    6. Checks if the first character of the element's text is an alphabetic or numeric character.
    7. If the first character is alphabetic, appends the text to the 'text' variable, adds a newline character, and appends the split version of 'text' to 's'.
    8. If the first character is numeric, assigns the text to the 'text' variable and appends a space character.
    9. Prints "Enter array to pdf" to the console.
    10. Initializes a FPDF object 'pdf'.
    11. Adds a new page to the PDF.
    12. Sets the font to Arial with a size of 15.
    13. Calculates the column width as the width of the PDF divided by 4.5.
    14. Calculates the row height as the font size of the PDF.
    15. Sets the spacing variable to 1.
    16. Iterates over each row in the 's' list.
    17. For each item in the row, adds a cell to the PDF with the specified column width, row height, text, and border.
    18. Adds a line break to the PDF.
    19. Outputs the generated PDF to a file named "Otchet.pdf".
    20. Prints "Stop make pdf" to the console.
    """
    tree = ET.parse("Status_klient.xml")
    root = tree.getroot()
    print("File doc. Method do_doc: Make array")
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

    print("File doc. Method do_doc: Enter array to pdf")
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
    print("File doc. Method do_doc: Stop make pdf")
   
