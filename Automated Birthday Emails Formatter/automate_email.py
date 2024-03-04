def extract_names(path: str, array: list):
    n = ''
    with open(path, "r") as file:
        data = file.read()

        for i in data:
            if i != "\n":
                n += i
            else:
                array.append(n)
                n = ''

def write_email(array:list):
    for name in array:
        with open(f"Output/ReadyToSend/{name}.txt", "w") as file:
            file.write(f'''Dear {name},

You are invited to my birthday this Saturday.

Hope you can make it!

Regards, Mr. V''')