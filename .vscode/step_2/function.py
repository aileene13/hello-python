def read_input():
    return "some input"


def do_calculation(data):
    return data + " " + data


def send_email(body, to):
    return True


def main():
    inputValue = read_input()
    result = do_calculation(inputValue)
    sendEmailResult = send_email(result, "aileene.lomeda13@gmail.com")
