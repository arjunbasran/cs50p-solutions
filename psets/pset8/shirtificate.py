from fpdf import FPDF

def main():
    name = input("Name: ").strip()

    pdf = FPDF()
    pdf.set_auto_page_break(False)
    pdf.add_page()

    pdf.set_font("Helvetica", size=36)
    pdf.cell(0, 20, "CS50 Shirtificate", align="C", ln=1)

    page_w = pdf.w
    img_w = page_w - 30
    img_x = (page_w - img_w) / 2
    img_y = 40
    pdf.image("shirtificate.png", x=img_x, y=img_y, w=img_w)

    pdf.set_font("Helvetica", size=24)
    pdf.set_text_color(255, 255, 255)
    chest_y = img_y + 50
    pdf.set_xy(0, chest_y)
    pdf.cell(page_w, 12, f"{name} took CS50", align="C")

    pdf.output("shirtificate.pdf")

if __name__ == "__main__":
    main()


