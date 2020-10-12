import markdown


def generateHTML(markdownString, outputPath):
    outputFile = open(outputPath, 'w', encoding='utf-8')
    htmlString = markdown.markdown(markdownString)
    outputFile.write(htmlString)
    outputFile.close()
    return htmlString


def generatePDF(htmlString, outputPath):
    return


if __name__ == "__main__":

    SOURCE_PATH = 'resume.md'
    OUTPUT_HTML_PATH = 'dist/resume.html'
    OUTPUT_PDF_PATH = 'dist/resume.pdf'

    sourceFile = open(SOURCE_PATH, 'r', encoding='utf-8')
    sourceString = sourceFile.read()

    htmlString = generateHTML(sourceString, OUTPUT_HTML_PATH)
    generatePDF(htmlString, OUTPUT_PDF_PATH)

    sourceFile.close()
