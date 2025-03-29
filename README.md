# pdf2txt-multipage-extractor

**pdf2txt-multipage-extractor** is a Python tool designed to extract text from PDF files, processing entire directories efficiently. Optimized with multiprocessing, it can handle thousands of PDFs, making it suitable for large-scale document conversion tasks.

---

## Features

- **Batch Processing**: Converts all PDFs in a specified folder to text files.
- **Multiprocessing**: Utilizes multiple CPU cores for faster processing.
- **Encoding Handling**: Manages various text encodings to ensure accurate text representation.
- **Indentation Preservation**: Retains the original indentation and structure from PDFs.

---

## Repository Structure

- `Pdf_test/`: Directory containing sample PDFs for testing purposes.
- `Python2/`: Contains the Python 2 version of the extraction script.
- `Python3/`: Contains the Python 3 version of the extraction script.
- `README.md`: This file, providing an overview of the project.

---

## Getting Started

### Prerequisites

- **Python 3.x** (recommended)
- **pdfminer.six**: A PDF parsing library for text extraction.

### Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/LorysHamadache/pdf2txt-multipage-extractor.git
   cd pdf2txt-multipage-extractor/Python3
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. **Prepare Your Directories**:
   - Place all target PDF files into a source directory (e.g., `input_pdfs/`).
   - Ensure an output directory exists for the text files (e.g., `output_txts/`).

2. **Run the Extraction Script**:

   ```bash
   python pdf_to_txt.py input_pdfs/ output_txts/
   ```

   Replace `pdf_to_txt.py` with the actual script name if different.

3. **Review Output**:
   - Each PDF in `input_pdfs/` will have a corresponding `.txt` file in `output_txts/` containing the extracted text.

---

## Implementation Details

1. **Library Selection**:
   - **pdfminer.six** was chosen for its reliability in text extraction across diverse PDF formats.

2. **Extraction Process**:
   - **Single PDF Handling**: Developed a function to extract text, ensuring proper encoding and indentation.
   - **Batch Processing**: Implemented a loop to process all PDFs in the source directory.
   - **Multiprocessing**: Utilized Python's `multiprocessing` module to enhance processing speed by leveraging multiple CPU cores.

3. **Performance**:
   - **Tested** on 10,031 PDFs, completing extraction in approximately 12 minutes under typical system load.
   - **Optimization Attempts**: Explored multithreading; however, observed no significant performance gains due to the Global Interpreter Lock (GIL) in Python.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your enhancements.

---

## Contact

For questions or suggestions, please open an issue in the repository.

---

*Note: This project is provided "as-is" without warranty of any kind. Use at your own discretion.*
