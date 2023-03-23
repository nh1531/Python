file = open("example2.txt", "w")

# 파일에 문자열을 씁니다.
file.write("Hello, world!\n")
file.write("This is an example file.\n")

# 파일에 문자열의 리스트를 씁니다.
lines = ["We will use it to demonstrate file writing in Python.\n",
         "We can write multiple lines at once.\n"]
file.writelines(lines)

file.close()  # 파일을 닫습니다.
