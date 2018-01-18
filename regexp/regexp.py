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


def cake_info(document):
    info = re.findall(r"[ア-ン]+\s\d+円", document)
    return info


def shop_info(document):
    info = re.finditer(r"\S+:\S+", document)
    list = [match.group() for match in info if match.group().find("http") < 0]
    return list


def url(document):
    info = re.search(r"https://tabelog.com/[a-zA-Z0-9/]+", document).group()
    return info


def del_url_document(document):
    text = re.sub(r"(https?|ftp)(:\/\/[-_\.!~*\'()a-zA-Z0-9;\/?:\@&=\+\$,%#]+)", "", document)
    return text


def main():
    document = get_document()
    print(shop_name(document))
    print(cake_info(document))
    print(shop_info(document))
    print(url(document))
    print(del_url_document(document))


if __name__ == "__main__":
    main()
