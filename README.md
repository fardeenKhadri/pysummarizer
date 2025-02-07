# **PySummarizer**

PySummarizer is a **flexible and efficient** text summarization library that supports both **extractive** and **abstractive** summarization. It allows summarizing text from PDFs and generates bullet-point summaries dynamically.

---

## **✨ Features**
- 📌 **Supports Extractive & Abstractive Summarization**
- 📄 **Extracts text from PDFs & summarizes automatically**
- 🔍 **Uses TextRank, LSA, and LexRank for extractive summarization**
- 🔢 **Adjusts bullet points based on text length**
- ⚙️ **Allows user-defined summary length**
- 🖥 **Simple CLI support for terminal-based summarization**
- 🔗 **Easy integration into Python projects**

---

## **🛠 Installation**
To install PySummarizer, run:
bash
```pip install pysummarizer```


🚀 How to Use PySummarizer

1️⃣ Import the Library
```import pysummarizer as pyss```

2️⃣ Set PDF File Paths
pdf_path = "sample.pdf"      # Input PDF file
output_file = "summary.txt"  # Output summary file

3️⃣ Generate Summary (Extractive or Abstractive)
pyss.summarize_pdf(
    pdf_path,
    output_file,
    method="textrank",            # Options: "textrank", "lsa", "lexrank"
    summary_type="extractive",     # Options: "extractive" or "abstractive"
)


4️⃣ Run the Code & Check Output
```python script.py```


