# PDF-to-Markdown Conversion App

This application provides a streamlined method for converting PDF documents into Markdown format. Utilizing `pdf2image` for image conversion and OpenAI's language models for text extraction and transformation, it automatically processes PDFs and outputs their contents in Markdown, adhering to specified formatting rules.

## Features

- **Automated Conversion:** Processes all PDF files placed in a designated folder, converting them into a series of images, and then extracting the textual content.
- **Markdown Formatting:** Converts the textual content extracted from the PDF pages into Markdown, following specified formatting rules.
- **Table-to-JSON Conversion:** Any tables found within the PDF are automatically converted into JSON representations.
- **Header/Footer Ignoring:** The system attempts to ignore headers and footers in the PDF, focusing on the main content.

## How It Works

1. **PDF to Image Conversion:**  
   Each PDF page is converted into an image using `pdf2image`. This ensures that even documents with complex formatting can be reliably processed.

2. **Text Extraction via LLM:**  
   The images are then sent to an OpenAI-powered Large Language Model (LLM). The LLM:  
   - Extracts the textual content from the image.  
   - Converts the extracted text into Markdown while adhering to the given rules:
     - **Ignore Headers and Footers:** No extraneous header/footer details will be included.
     - **Convert Tables to JSON:** Any tabular content is rendered as JSON objects rather than Markdown tables.

3. **Output Generation:**  
   The resulting Markdown content (including embedded JSON for tables) is appended to a `.txt` file with a name corresponding to the original PDF (but without its extension).

## Requirements

- **Python 3.8+** recommended.
- **Dependencies:**
  - [pdf2image](https://pypi.org/project/pdf2image/)
  - [base64](https://docs.python.org/3/library/base64.html) (Standard library)
  - [os](https://docs.python.org/3/library/os.html) (Standard library)
  - [langchain-core](https://pypi.org/project/langchain-core/) and [langchain-openai](https://pypi.org/project/langchain-openai/) for LLM integration.
  - An active OpenAI API key with appropriate permissions.  
    *Note:* The code references an API key of the form `sk-****************************`; make sure you replace this with your own API key.

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/kkaarrss/pdf-to-markdown.git
   cd pdf-to-markdown
   ```

2. **Create and Activate a Virtual Environment (optional but recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

   Ensure that `pdf2image`, `langchain-core`, and `langchain-openai` are listed in `requirements.txt`, along with `pillow` (for `pdf2image`), and other required packages.

4. **Set up Poppler (if using pdf2image):**
   - **Linux:** Install `poppler-utils` via your package manager (e.g., `sudo apt-get install poppler-utils`).
   - **macOS:** Use `brew install poppler`.
   - **Windows:** Download the latest [Poppler binaries](http://blog.alivate.com.au/poppler-windows/) and add the `bin` directory to your `PATH`.

5. **Configure Your OpenAI API Key:**
   Replace the placeholder `sk-****************************` in the code with your actual OpenAI API key. Alternatively, you can set it as an environment variable or integrate it using a configuration file.

## Usage

1. **Place your PDFs:**
   Place all the PDF files you want to convert into the `pdf/` directory.

2. **Run the Script:**
   ```bash
   python3 convert.py
   ```
   *Assuming `convert.py` is the name of the script provided.*

3. **Output:**
   For each PDF, the script will generate a `.txt` file with a name matching the original PDF. This `.txt` file will contain the Markdown-formatted output.

   - **Headers and footers** are omitted.
   - **Tables** in the original PDF are represented as JSON objects in the Markdown output.

## Example

If you have a file named `document.pdf` in the `pdf/` folder, after running the script, you might see:

- `document.txt` containing the extracted markdown:
  ```markdown
  # Introduction

  This is the introduction text from the PDF.

  **JSON Table Representation:**
  ```json
  [
    {"Column1": "Value1", "Column2": "Value2"},
    {"Column1": "Value3", "Column2": "Value4"}
  ]
  ```
  ```

## Troubleshooting

- **No Output File Created:**  
  Ensure that the PDF is accessible and that `pdf2image` can read and convert it. Check if `poppler` is correctly installed.
  
- **Incomplete or Incorrect Output:**  
  The quality of the OCR and text extraction depends on the clarity of the PDF. Scanned PDFs with poor image quality may yield suboptimal results.

- **API Rate Limits or Errors:**  
  If you encounter API errors, you may be hitting rate limits or have an invalid API key. Check your OpenAI account and ensure your key is correct.

## Contributing

Contributions, bug reports, and feature requests are welcome! Please open an issue or submit a pull request on GitHub.

## License

This project is licensed under the [Apache License 2.0](https://www.apache.org/licenses/LICENSE-2.0).

