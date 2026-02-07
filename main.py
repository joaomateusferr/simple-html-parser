from html_parser.Parser import Parser
from pathlib import Path

#Page = '<!DOCTYPE html><html><head><title>Título da Página</title></head><body><h1>Olá Mundo</h1><p>Este é o corpo da página em uma única linha.</p></body></html>'
Page = Path('/home/john/Desktop/site.html').read_text(encoding='utf-8')
Parser = Parser(Page)
print(Parser)