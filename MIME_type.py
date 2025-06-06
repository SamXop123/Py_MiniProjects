"""
Web browsers, rely on MIME types (also known as media types), to determine how to display files that live on the web. 
When you download a file from a web server, that server sends an HTTP header, along with the file itself, indicating the file’s media type. 
For instance, the media type for a GIF is image/gif, and the media type for a JPEG is image/jpeg. 
To determine the media type for a file, a web server typically looks at the file’s extension, mapping one to the other.
"""

extension = input("File name: ").strip().lower()

if "." in extension:
    extList = list(extension.split("."))
    L = len(extList)

    if(extList[L-1] in ["png", "gif", "jpeg"]):
        print(f"image/{extList[L-1]}")
    elif(extList[L-1] == "jpg"):
        print("image/jpeg")
    elif(extList[L-1] == "pdf" or extList[L-1] == "zip"):
        print(f"application/{extList[L-1]}")
    elif(extList[L-1] == "txt"):
        print(f"text/plain")
    else:
        print("application/octet-stream")

elif "." not in extension:
    print("application/octet-stream")

# ---------------------------------------------------

# OTHER METHOD

mime_types = {
    "png": "image/png",
    "jpeg": "image/jpeg",
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "pdf": "application/pdf",
    "zip": "application/zip",
    "txt": "text/plain"
    #Add More....
}

file = input("File name: ").strip().lower()

if "." in file:
    file_parts = file.split(".")
    file_extension = file_parts[-1]  
    print(mime_types.get(file_extension, "application/octet-stream"))
else:
    print("application/octet-stream")

# ----------------------------------------------------------------------

# OTHER METHOD (easiest)
#(Considers all the extensions taht exist)

import mimetypes

file = input("File name: ").strip().lower()

result = mimetypes.guess_type(file) 
mime_type = result[0]

if mime_type:
    print(mime_type)
else:
    print("application/octet-stream")



