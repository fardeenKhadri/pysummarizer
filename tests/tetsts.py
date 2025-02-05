import pysummarizer as pyss

pdf_path = "F:/pysummarizer/tests/Unit - 4.pdf"  
output_file = "F:/pysummarizer/tests/summary.txt"

# Summarize the PDF and save it
# pyss.summarize_pdf(pdf_path, output_file, method="textrank", summary_type="extractive")
pyss.summarize_pdf(pdf_path, output_file, max_length=10000) 


print(f"Summary saved to {output_file}")
