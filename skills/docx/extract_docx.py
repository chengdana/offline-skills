import zipfile
import xml.etree.ElementTree as ET
import sys

def extract_text_from_docx(docx_path):
    """Extract text from a docx file"""
    try:
        with zipfile.ZipFile(docx_path, 'r') as zip_ref:
            # Read the main document
            xml_content = zip_ref.read('word/document.xml')
            root = ET.fromstring(xml_content)

            # Define namespace
            ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

            # Extract all text
            texts = []
            for t in root.findall('.//w:t', ns):
                if t.text:
                    texts.append(t.text)

            return ''.join(texts)
    except Exception as e:
        return f"Error: {str(e)}"

if __name__ == "__main__":
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    for file in sys.argv[1:]:
        print(f"\n{'='*60}")
        print(f"File: {file}")
        print('='*60)
        text = extract_text_from_docx(file)
        print(text[:8000])  # Print first 8000 chars
