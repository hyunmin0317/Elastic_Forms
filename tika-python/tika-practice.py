from tika import parser

pdf_path = "input.pdf"

# PDF 파일에서 텍스트를 추출
raw_pdf = parser.from_file(pdf_path)
contents = raw_pdf['content']
contents = contents.strip()

print(contents)
