exten = input("File name: ").lower().strip()

if exten.endswith(".gif"):
    print("image/gif")
elif exten.endswith(".jpg"):
    print("image/jpeg")
elif exten.endswith(".jpeg"):
    print("image/jpeg")
elif exten.endswith(".png"):
    print("image/png")
elif exten.endswith(".pdf"):
    print("application/pdf")
elif exten.endswith(".txt"):
    print("text/plain")
elif exten.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
