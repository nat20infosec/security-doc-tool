from fpdf import FPDF

# Function to generate PDF report
def generate_pdf_report(results, framework):
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, f'{framework.upper()} Compliance Report', ln=True, align='C')

    pdf.set_font('Arial', '', 12)
    for result in results:
        pdf.cell(200, 10, f"Control: {result['control']}", ln=True)
        pdf.cell(200, 10, f"Resource: {result['resource']}", ln=True)
        pdf.cell(200, 10, f"Status: {result['status']}", ln=True)
        pdf.cell(200, 10, f"Detail: {result['detail']}", ln=True)
        pdf.ln(10)

    pdf.output(f'reports/generated_reports/{framework}_compliance_report.pdf')

# Function to generate Markdown report
def generate_markdown_report(results, framework):
    report_lines = [f"# {framework.upper()} Compliance Report\n\n"]

    for result in results:
        report_lines.append(f"## Control: {result['control']}\n")
        report_lines.append(f"**Resource:** {result['resource']}\n")
        report_lines.append(f"**Status:** {result['status']}\n")
        report_lines.append(f"**Detail:** {result['detail']}\n")
        report_lines.append("\n---\n")

    markdown_content = "\n".join(report_lines)

    # Save the markdown content to a file
    report_path = f'reports/generated_reports/{framework}_compliance_report.md'
    with open(report_path, 'w') as f:
        f.write(markdown_content)

    print(f"Markdown report generated at {report_path}")