from lxml import html

class Parser:

    def __init__(self, html_content):
        self.html_content = html_content

    def __str__(self):
        return f"html_content : {self.html_content}"

    def __repr__(self):
        return f"Parser(html_content='{self.html_content}')"

    def get_title(self: str) -> str | None:

        tree = html.fromstring(self.html_content)
        query = "//head/title/text()"
        entries = tree.xpath(query)

        if entries:
            return entries[0].strip()

        return None