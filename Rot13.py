def rot13(message):
    return "".join(
        [((chr(ord(x) + 13) if (ord(x.lower()) + 13) <= ord("z") else chr(ord(x) - 13)) if x.isalpha() else x) for x in
         message])


print(rot13("test"))
