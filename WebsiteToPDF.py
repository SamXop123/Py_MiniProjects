import pdfkit

url = "https://www.wikipedia.org/"
pdfkit.from_url(url, "output.pdf")  
