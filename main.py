from html_parser.Parser import Parser

Page = '<!DOCTYPE html><html><head><title>Título da Página</title></head><body><h1>Olá Mundo</h1><p>Este é o corpo da página em uma única linha.</p></body></html>'
Parser = Parser(Page)
print(Parser.get_title())