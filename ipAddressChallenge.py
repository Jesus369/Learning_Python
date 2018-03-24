# Print the amount of character within each segment
# Of a provided IP Address
print("Please enter an IP Address")
ipAddress = raw_input("")
if ipAddress[-1]:
    ipAddress += "."
segment = 1
seg_length = 0

for character in ipAddress:
    if character == ".":
        print("segment {} containers {} characters".format(segment, seg_length))
        segment += 1
        seg_length = 0
    else:
        seg_length += 1

# if character != ".":
#     print("segment {} containers {} characters".format(segment, seg_length))
#     segment += 1
#     seg_length = 0
