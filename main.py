from PyPDF2 import PdfFileMerger

pdfs = ['page1.pdf', 'page2.pdf', 'sample.pdf']

def merge_pdfs(pdfs, newfilename):
	merger = PdfFileMerger()

	for pdf in pdfs:
		merger.append(pdf)

	merger.write(newfilename)
	merger.close

if __name__=="__main__":
	merge_pdfs(pdfs, newfilename="penguins.pdf")