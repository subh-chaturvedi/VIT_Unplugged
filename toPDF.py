from reportlab.pdfgen import canvas

# Create a new PDF document
pdf = canvas.Canvas("xyz.pdf")

# Set the font and font size
pdf.setFont("Helvetica", 12)

# Draw the text "Hello" at a specific position
pdf.drawCentredString(300, 500, "Hello")

# Save the PDF document
pdf.save()

print("PDF file created successfully!")