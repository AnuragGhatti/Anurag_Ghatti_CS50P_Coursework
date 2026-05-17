# shirtificate.py

from fpdf import FPDF


def main():
    name = input("Name: ").strip()

    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    # Title
    pdf.set_font("Helvetica", "B", 24)
    pdf.cell(0, 30, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

    # Shirt image
    pdf.image("shirtificate.png", x=10, y=60, w=190)

    # Name on shirt
    pdf.set_font("Helvetica", "B", 20)
    pdf.set_text_color(255, 255, 255)

    pdf.set_xy(0, 140)
    pdf.cell(210, 10, f"{name} took CS50", align="C")

    # Save PDF
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
