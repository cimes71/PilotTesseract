Evaluating PyTesseract
This code currently is reading a multi-page PDF and converting it to images to be parsed into text/data with tesseract.

Current code exports to TSV - 

Method filtered output which just contains the text and page number (starting with 0) so I can see the page breaks.  Also only contains text in which tesseract has > 30% confidence.
<img width="308" alt="Screenshot 2024-09-17 at 8 50 25 AM" src="https://github.com/user-attachments/assets/64e8a4b5-1859-4322-955a-f9f9658361ba">  <img width="302" alt="Screenshot 2024-09-17 at 8 52 56 AM" src="https://github.com/user-attachments/assets/38e77328-8c3a-460b-b8c7-c68db95ddedc">



Method for unfiltered ouput which gives all the output and position of the text and the levels.


<img width="1318" alt="Screenshot 2024-09-17 at 8 48 02 AM" src="https://github.com/user-attachments/assets/b8655e51-7abd-42d6-84c1-c52f62b23b8a">



Looking at annontation tools and Spacy for NLP for potential Chatbot Analysis.
