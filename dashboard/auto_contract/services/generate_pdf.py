import weasyprint
from jinja2 import Template


def generate_pdf(contract: dict, template_html: str, base_url: str, stylesheets_path: str) -> bytes:
    """Gera um arquivo PDF a partir do layout HTML e CSS do documento.

    Args:
        contract: O contrato preenchido com os dados JSON.
        :param base_url:
        :param template_html:
        :param contract:
        :param stylesheets_path:

    Returns:
        O arquivo PDF gerado.
    """

    # Read the content of the HTML file
    with open(template_html, "r") as f:
        template = Template(f.read())

    # Render the content of the HTML file using the Jinja2 library, replacing values with contract information
    html = template.render(document=contract["documento"], data=contract["data"])

    # Create a WeasyPrint document with the rendered HTML and the CSS file
    document = weasyprint.HTML(string=html, encoding="utf-8", base_url=base_url).render(stylesheets=[stylesheets_path])

    # Return the rendered PDF document
    return document.write_pdf()
