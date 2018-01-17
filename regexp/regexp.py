import re


def get_document():
    with open("a.txt", "r") as f:
        document = (f.read()).split("\n")
    while document.count("") > 0:
        document.remove("")
    return "\n".join(document)


def shop_name(document):
    name = re.search(r"「\S+」", document).group()
    return re.sub(r"[「」]", "", name)


def main():
    document = get_document()
    print(shop_name(document))


if __name__ == "__main__":
    main()
