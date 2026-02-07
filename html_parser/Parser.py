from lxml import html
from bs4 import BeautifulSoup

class Parser:

    title: str | None
    content: str | None

    def __init__(self, html_content):

        self.title = self.parse_title(html_content)

        body = self.parse_body(html_content)

        if body :
            self.content = self.parse_content(body)
        else :
            self.content = None

    def __str__(self):
        return f"title : {self.title}, content : {self.content}"

    def __repr__(self):
        return f"Parser(title='{self.title},content='{self.content}')"

    @staticmethod
    def parse_title(html_content : str) -> str | None:

        tree = html.fromstring(html_content)
        query = "//head/title/text()"
        entries = tree.xpath(query)

        if entries:
            return entries[0].strip()

        return None

    @staticmethod
    def parse_body(html_content : str) -> str | None:

        result = None

        soup = BeautifulSoup(html_content, 'html.parser')
        body = soup.find('body')

        if body:
            result = "".join(str(child) for child in body.contents)

        return result

    @staticmethod
    def parse_content(body: str) -> str:

        soup = BeautifulSoup(body, "html.parser")

        for script_or_style in soup(["script", "style"]):
            script_or_style.decompose()

        return " ".join(soup.get_text().split())

    def get_title(self) -> str | None:
        return self.title

    def get_content(self) -> str | None:
        return self.content