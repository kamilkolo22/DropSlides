import PyPDF2
import os


def delete_slides(input_path, output_path):
    if not os.path.isfile(input_path):
        raise OSError(f'file: {input_path} not found')
    if not isinstance(output_path, str):
        output_path = output_path.name

    # creating a pdf file object
    pdf_file_obj = open(input_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file_obj)

    # select pages that are not duplicated
    n = pdf_reader.numPages
    pages_to_keep = [n - 1]
    page0 = pdf_reader.getPage(n - 1).extractText()
    for page in range(n - 2, -1, -1):
        page1 = pdf_reader.getPage(page).extractText()
        if page1 not in page0:
            pages_to_keep.append(page)
        page0 = page1
    pages_to_keep.reverse()

    # create output file with unique pages
    output = PyPDF2.PdfFileWriter()
    for i in pages_to_keep:
        p = pdf_reader.getPage(i)
        output.addPage(p)

    with open(output_path, 'wb') as f:
        output.write(f)
