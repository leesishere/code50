extension = {
    "gif":"image/gif",
    "jpg":"image/jpeg",
    "jpeg":"image/jpeg",
    "png":"image/png",
    "pdf":"application/pdf",
    "txt":"text/plain",
    "zip":"application/zip"
}

file, ext = input("File name: ").split(".")

try:
    print(extension[ext])
except:
    print()
