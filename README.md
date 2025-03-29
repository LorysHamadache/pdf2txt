# pdf2txt — Batch PDF First-Page Text Extractor

**pdf2txt** is a Python script that extracts the **first page** of text from every PDF in a folder and saves each as a `.txt` file with the same name.  
It is optimized using **Python multiprocessing** and was successfully tested on **10,031 PDFs**, reducing total processing time from **44 minutes to 12 minutes**.

---

## 📌 Features

- Extracts **only the first page** for speed and relevance
- Preserves **indentation** and **text encoding**
- Batch processes entire folders
- Outputs `.txt` files with matching names
- Fast, minimal, no unnecessary dependencies

---

## 🚀 Usage

### Requirements

- Python 3.x
- [`pdfminer.six`](https://github.com/pdfminer/pdfminer.six)

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run the script

```bash
python pdf_to_txt.py <input_folder> <output_folder>
```

Example:

```bash
python pdf_to_txt.py ./pdfs ./txts
```

> Each PDF in `./pdfs` will be processed, and the output text will be written to `./txts/filename.txt`.

---

## 🧠 Implementation Notes

- Uses `pdfminer.six` for PDF parsing and text extraction
- Focused on **first-page only** to speed up processing and reduce noise
- Ensures:
  - Proper UTF-8 encoding
  - Correct word spacing
  - Structural indentation preserved

---

## ⏱️ Performance

- Test Set: **10,031 PDFs**
- **Single-threaded**: ~44 min  
- **Multi-threaded**: ~21.2 sec for 101 files (but unstable)  
- **Multiprocessing**: ~5.4 sec for 101 files → **Full run in ~12 min**

---

## 📜 Development History

1. **Library Research**:
   - `PyPDF` worked on user PDFs but failed on test files.
   - Custom parser failed due to encoding issues.
   - Settled on `pdfminer` (`pdfminer3k` for Python 3) for proper text handling.

2. **Single PDF Extraction Tool**:
   - Tuned parameters for:
     - Proper UTF-8 encoding
     - Correct word spacing
     - Indentation preservation

3. **Created test folders** for structured evaluation.

4. **Batch Processing Script**:
   - Built program to extract from all PDFs in a given folder.

5. **Initial Benchmark**:
   - Processed 10,031 PDFs in **44 minutes** on a lightly used PC.

6. **Multithreading Attempt**:
   - `Linear`: 22.8 sec for 101 files  
   - `Multithread`: 21.24 sec for 101 files  
   - Result: **High volatility**, sometimes slower than linear.
   - Cause: Python’s **Global Interpreter Lock (GIL)** prevents true parallelism in threads.  
     Ref: [StackOverflow](https://stackoverflow.com/questions/36955638/how-should-i-reduce-the-execution-time-using-threading-in-python)

7. **Switched to Multiprocessing**:
   - `Multiprocessing`: 5.4 sec for 101 files
   - Brought total processing time down to **~12 minutes**

8. **Final Version**:
   - Python script using `multiprocessing`
   - Minimal, no class boilerplate
   - Simple CLI with two arguments: `input_path`, `output_path`

---

## 📁 Project Structure

- `pdf_to_txt.py` – Main script
- `requirements.txt` – Dependencies
- `README.md` – This file

---

## 📄 License

MIT License — see [LICENSE](./LICENSE)

---

## 🔗 Related Links

- [pdfminer.six Docs](https://pdfminersix.readthedocs.io/)
- [Python Multiprocessing Docs](https://docs.python.org/3/library/multiprocessing.html)
- [StackOverflow Thread on GIL](https://stackoverflow.com/questions/36955638/how-should-i-reduce-the-execution-time-using-threading-in-python)
