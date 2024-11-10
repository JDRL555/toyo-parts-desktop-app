from jinja2 import Environment, FileSystemLoader

import pdfkit
import os

class Report():
  def config_pdf(self):
    path        = r"{}".format(os.environ.get("WKHTMLTOPDF_PATH"))
    self.config = pdfkit.configuration(wkhtmltopdf=path)

  def export_pdf(self, data):
    self.config_pdf()
    env       = Environment(loader=FileSystemLoader("src/template"))
    template  = env.get_template("report.html")
    html      = template.render(data)

    pdfkit.from_string(html, "reporte.pdf", configuration=self.config)

    return os.path.isfile("reporte.pdf")