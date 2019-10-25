import PyPDF2
import sys

inputs = sys.argv[1:]


def pdf_combiner(pdf_list):
    with open("super.pdf", "rb") as input_file:
        reader = PyPDF2.PdfFileReader(input_file)
        with open("wtr.pdf", "rb") as filehandle_watermark:
            watermark = PyPDF2.PdfFileReader(filehandle_watermark)
            first_page_watermark = watermark.getPage(0)
            pdf_writer = PyPDF2.PdfFileWriter()
            for i in range(reader.getNumPages()):
                page = reader.getPage(i)
                page.mergePage(first_page_watermark)
                pdf_writer.addPage(page)

            with open("alimo.pdf", "wb") as filehandle_output:
                # write the watermarked file to the new file
                pdf_writer.write(filehandle_output)


pdf_combiner(inputs)
