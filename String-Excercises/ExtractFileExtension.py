filename=input("Ente FileName with extension:")
print("File Name is ",filename)
extension = filename.partition(".")[2]
# print("Extension is ",extension)
match extension:
    case "":
        print("File extension is empty")
    case "pdf":
        print("File extension is pdf")
    case "png":
        print("File extension is png")
    case _:
        print("File extension is unknown")
