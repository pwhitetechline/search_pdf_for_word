import os
from pdfminer.high_level import extract_text

def search_word_in_pdf(folder_path, word):
    results = []

    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(folder_path, filename)

            try:
                # Use pdfminer to extract text
                text = extract_text(pdf_path)
                
                # Split the text by page breaks to get individual pages
                pages = text.split('\f')

                for page_num, page_content in enumerate(pages):
                    if word.lower() in page_content.lower():
                        results.append((filename, page_num + 1))

            except Exception as e:
                print(f"An error occurred while processing {filename}: {e}")

    return results

def main():
    folder_path = input("Enter the path of the folder containing PDFs: ")
    word = input("Enter the word to search for: ")

    results = search_word_in_pdf(folder_path, word)

    if results:
        for filename, page_num in results:
            print(f"Found '{word}' in {filename} on page {page_num}")
    else:
        print(f"'{word}' was not found in any PDF in the specified folder.")

if __name__ == "__main__":
    main()
