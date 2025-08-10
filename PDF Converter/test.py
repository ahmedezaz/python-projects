from fpdf import FPDF
print("PDF CONVERTER")
with open("example.txt", "r") as file:
    for line in file:
        print(line.strip())
        print(f"PDF saved as {output_pdf}")

