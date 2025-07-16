def main():
    name=input("file name: ").strip().lower()
    extension=name.rsplit('.', 1)[-1] if '.' in name else ''

    if extension in ["gif"]:
        print("image/gif")
    elif extension in ["jpg", "jpeg"]:
        print("image/jpeg")
    elif extension in ["png"]:
        print("image/png")
    elif extension in ["pdf"]:
        print("application/pdf")
    elif extension in ["txt"]:
        print("text/plain")
    elif extension in ["zip"]:
        print("application/zip")
    else:
        print("application/octet-stream")

if __name__ == "__main__":
    main()
