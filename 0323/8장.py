import re

def extract_email(string):
    #\b\b 단어의 시작과 끝
    # . 자체를 찾고 싶을 땐 \. , 왜냐면 . 은 모든 문자를 찾아주는 메타문자이기 때문
    pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(pattern, string)
    return emails


string = "John's email is john.doe123@example.com. Jane can be reached at jane@example.co.uk."

emails = extract_email(string)
print(emails)  # ['john.doe123@example.com', 'jane@example.co.uk']
