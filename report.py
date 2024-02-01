from fpdf import FPDF
import pygal
from pygal.style import Style
import cairosvg
def Gen_rep(project_name, project_details, project_progress, resources_util, budget, days):
    pdf = FPDF()
    pdf.add_page()

    # Set font to Times New Roman, bold, size 20
    pdf.set_font("Helvetica", "B", 26)
    pdf.cell(0, 10, txt=project_name, ln=True, align='C')

    # Set font to Times New Roman, size 15
    pdf.set_font("Helvetica", size=12)

    # First subheading: Details
    pdf.ln(10)
    pdf.set_font("Helvetica", "B", size=12)
    pdf.cell(0, 10, txt="Project Details", ln=True, align='C')
    pdf.set_font("Helvetica", size=12)
    pdf.multi_cell(0, 10, txt=project_details, align='C')

    gauge = pygal.SolidGauge(inner_radius=0.70,
        style=pygal.style.styles['default'](value_font_size=80),
        show_legend=False)
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge.value_formatter = percent_formatter
    gauge.add("Resource Utilisation", [{'value': resources_util, 'max_value': 100}])
    gauge.render_to_png('res_util.png')

    pdf.ln(10)
    pdf.set_font("Helvetica", "B", size=12)
    pdf.cell(0, 10, txt="Resource Utilisation", ln=True, align='C')
    pdf.image('res_util.png', x=75, y=70, w=60)

    # Second subheading: Billing/Utilisation
    pdf.ln(60)  # Add a line break
    pdf.set_font("Helvetica", "B", size=12)
    pdf.cell(0, 10, txt="Project Progress", ln=True, align='C')
    pdf.set_font("Helvetica", "B", size=12)
    gauge2 = pygal.SolidGauge(inner_radius=0.70,
                             style=pygal.style.styles['default'](value_font_size=80),
                             show_legend=False)
    percent_formatter = lambda x: '{:.10g}%'.format(x)
    gauge2.value_formatter = percent_formatter
    gauge2.add("Project Progress", [{'value': project_progress, 'max_value': 100}])
    gauge2.render_to_png('proj_progress.png')
    pdf.image('proj_progress.png', x=75, y=140, w=60)

    pdf.ln(60)
    pdf.cell(0, 10, txt="Budget", ln=True, align='C')
    pdf.set_font("Helvetica", size=12)
    pdf.multi_cell(0, 10, txt=budget, align= 'C')


    pdf.ln(20)

    pdf.set_font("Helvetica", "B", size=12)
    pdf.cell(0, 10, txt="Ongoing Time", ln=True, align='C')
    pdf.set_font("Helvetica", size=12)
    pdf.multi_cell(0, 10, txt=f'{days} Days', align='C')

    # Save the PDF to a file
    pdf_output_path = f"{project_name}_report.pdf"
    pdf.output(pdf_output_path)
    return pdf_output_path


# Example usage
project_name = "Instagram"
project_details = "Social Media Platform"
project_progress = 79
resources_util = 65
budget = "$1,000,000"
days = 20

Gen_rep(project_name, project_details, project_progress, resources_util, budget, days)
