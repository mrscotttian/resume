import markdown

SOURCE_PATH = 'resume.md'
OUTPUT_PATH = 'dist/resume.html'

sourceFile = open(SOURCE_PATH, 'r', encoding='utf-8')
outputFile = open(OUTPUT_PATH, 'w', encoding='utf-8')

sourceString = sourceFile.read()
htmlSting = markdown.markdown(sourceString)
outputFile.write(htmlSting)

outputFile.close()
sourceFile.close()
