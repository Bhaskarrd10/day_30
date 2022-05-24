#try:
#    file = open("a_file.text")
#    a_dictionary = {"key": "value"}
#    print(a_dictionary["key"])
#except FileNotFoundError:
#    file = open("a_file", "w")
#    file.write("something")
#except KeyError as error_message:
#    print(f"The key{error_message} does not exist")
#else:
#    content = file.read()
#    print(content)
#finally:
#    file.close()
#    print("file was closed")


height = float(input("Height: "))
weight = int(input("weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 metere")

bmi = weight/ height ** 2
print(bmi)
