import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))



from pysummarizer.extractive import ExtractiveSummarizer

text = """Python is a widely used high-level programming language for general-purpose programming. 
It was created by Guido van Rossum and first released in 1991. 
An interpreted language, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. 
It provides constructs that enable clear programming on both small and large scales."""

# Create an ExtractiveSummarizer instance
summarizer = ExtractiveSummarizer(method="textrank")

# Summarize the text
summary = summarizer.summarize(text, sentences_count=2)

print("Extractive Summary:")
print(summary)
 
