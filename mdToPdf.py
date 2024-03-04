from markdown2pdf import convert

# Replace "your_file.md" with the actual file path
markdown_file = "your_file.md"

# Optional: Customize output filename and CSS stylesheet
pdf_file = "output.pdf"
css_file = "custom_styles.css"

# Convert Markdown to PDF
convert(markdown_file, output_filename=pdf_file, css=css_file)

print(f"Markdown file converted to PDF: {pdf_file}")
