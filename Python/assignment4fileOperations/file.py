# File Read and Write
with open("input_file.py ", "w") as f:
  f.write("Hello this is the input file created for you as a test, It will be modified and give the output file")
# This works if you have a ffile name created already and you are to input the name of the file required 
def file_read_write(input_file,output_file):
  try:
    # Read from input file
    with open(input_file, "r") as file:
      content = file.read()

    modified_content = content.upper()

    with open(output_file, "w") as file:
      file.write(modified_content)

    print(f"Modified content has been written to {output_file}")

  except FileNotFoundError:
    print(f"Error: The file '{input_file}' does not exist. ")
  except Exception as e:
    print(f"An unexpected error occurred:", e)


filename = input("Enter the name of the file to read: ")

output_filename = "output.txt"

file_read_write(filename, output_filename)


# file = open("newfile.pdf","w")
# content = "Hello World, This is amazin\n"

# file.write(content.upper())

# try:
#     file =  open('newFile', 'r')
#     content = file.read()
#     print(content)
# except FileNotFoundError:
#     print("File not found")
# finally:
#     print("File operation completed")
#     file.close()