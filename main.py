from encode import encode_image
from compare import compare_image

print('''
  ___ __  __   _   ___ ___                                     
 |_ _|  \/  | /_\ / __| __|                                    
  | || |\/| |/ _ \ (_ | _|                                     
 |___|_| _|_/_/_\_\___|___|__  __   _   ___ _  _____ _  _  ___ 
 \ \    / /_\_   _| __| _ \  \/  | /_\ | _ \ |/ /_ _| \| |/ __|
  \ \/\/ / _ \| | | _||   / |\/| |/ _ \|   / ' < | || .` | (_ |
   \_/\_/_/ \_\_| |___|_|_\_|  |_/_/ \_\_|_\_|\_\___|_|\_|\___|
      ''')
print("===============================================================\n")
print("Welcome to the Image Watermarking program!")
print("made by Aulia Nadhirah Yasmin B (18221066)\n")
print("First, prepare the image that will be used for watermarking")
print("Put the input image in the input folder")
originalImage = input('''Enter the file name of the original image 
(add .jpg or.png in the end) : ''')
intensity = int(input("Enter the noise intensity : "))
seed = int(input("Enter the seed used : "))
resultFile = input("Enter the name of the result file : ")
print("")
encode_image(resultFile, "input\\" + originalImage, intensity, seed)
print("\n===============================================================\n")
answer = input("Would you like to check if the image has been watermarked? (Y/N) : ")
while answer != "Y" and answer != "N":
  print("Input invalid!") 
  answer = input("Would you like to check if the image has been watermarked? (Y/N) : ")
if answer == "Y" :
  compare = compare_image("input\\" + originalImage, resultFile + ".png")
  print("RESULT : " + compare)
print("\n -+-+-+-+- THAT'S ALL! Thank you for using my program! -+-+-+-+-\n")
