# import the necessary libraries
import sys
from PIL import Image, ImageEnhance
import requests
import re
from time import sleep

from mrbeast import MRBEAST

from ansiconverter.converter import RGBtoANSI

ANSI_RESET = "\033[0m"
ANSI_REG = r"\[^\[]+\[[^]+m"

print(MRBEAST.replace("\\033[0m", "").replace("\\033", ""))

title = '|                                                           |\n' + '|   iASCII - General Meme-ing tool for making copypastas.   |\n' + '|___________________________________________________________|\n'
print(title)
while True:
  # define the ascii characters
  # soon to be an array
  ascii_characters = '@#%*+=-:. '

  # https://i.ytimg.com/vi/1RJqPFJxkYI/hqdefault.jpg
  URL = "https://art.pixilart.com/81b2a49b47ddb18.png\n"
  print("Example : " + URL)
  URL = input("Enter your URL: ")

  r = requests.get(URL, stream=True)
  image = Image.open(r.raw)

  if len(URL) < 1:
    print("Got less than:", str(len(URL)), "\n - This program will error.")
  else:
    print("Got :", URL, "\n-=*=-\n\n")
    print("Width X Height :", str(image.width), "X", str(image.height),
          "\n-=*=-\n\n")

  print("Example : 30 (Great for small images), 100 \n")
  width = int(input("Enter your Width: "))

  if len(URL) < 1:
    print("Got less than:", str(len(width)), "\n - This program will error.")
  else:
    print("Got :", str(width), "\n-=*=-\n\n")

  print("Example : 30 (Great for small images), 100 \n")
  height = int(input("Enter your Height: "))
  if len(URL) < 1:
    print("Got less than:", str(len(height)), "\n - This program will error.")
  else:
    print("Got :", str(height), "\n-=*=-\n\n")

  print("Ⓟ ick an option:\n")
  print("1: @#%*+=-:. \n")
  print("2: .:-=+*#%@\n")
  print("3: @$#086543271=+-:,. \n")
  print("4:  .,:-+=172345680#$@\n")
  print(
    "5: $@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. \n"
  )
  print(
    "6:  .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$\n"
  )
  print(
    "7: ÆÑÊŒØMÉËÈÃÂWQBÅæ#NÁþEÄÀHKRŽœXgÐêqÛŠÕÔA€ßpmãâG¶øðé8ÚÜ$ëdÙýèÓÞÖåÿÒb¥FDñáZPäšÇàhû§ÝkŸ®S9žUTe6µOyxÎ¾f4õ5ôú&aü™2ùçw©Y£0VÍL±3ÏÌóC@nöòs¢u‰½¼‡zJƒ%¤Itocîrjv1lí=ïì<>i7†[¿?×}*{+()\/»«•¬|!¡÷¦¯—^ª„”“~³º²–°¹‹›;:’‘‚’˜ˆ¸…·¨´`\n"
  )
  print(
    "8: `´¨·…¸ˆ˜’‚‘’:;›‹¹°–²º³~“”„ª^—¯¦÷¡!|¬•«»/\)(+{*}×?¿[†7i><ìï=íl1vjrîcotI¤%ƒJz‡¼½‰u¢sòön@CóÌÏ3±LÍV0£Y©wçù2™üa&úô5õ4f¾ÎxyOµ6eTUž9S®ŸkÝ§ûhàÇšäPZáñDF¥bÒÿåÖÞÓèýÙdë$ÜÚ8éðø¶Gâãmpß€AÔÕŠÛqêÐgXœŽRKHÀÄEþÁN#æÅBQWÂÃÈËÉMØŒÊÑÆ\n"
  )
  print("9: Custom characterset\n")

  ascii_choice = int(input("Enter style (1, 2, 3, 4, 5, 6, 7, 8, 9): "))
  if len(URL) < 1:
    print("Got less than 1:", str(len(ascii_choice)),
          "\n - This program will error.")
  else:
    print("Got :", str(ascii_choice), "\n-=*=-\n\n")

  if ascii_choice == 2:
    ascii_characters = " .:-=+*#%@"
    print("Got :", str(ascii_characters), "\n-=*=-\n\n")
  if ascii_choice == 3:
    ascii_characters = "@$#086543271=+-:,. "
    print("Got :", str(ascii_characters), "\n-=*=-\n\n")
  if ascii_choice == 4:
    ascii_characters = " .,:-+=172345680#$@"
    print("Got :", str(ascii_characters), "\n-=*=-\n\n")
  if ascii_choice == 5:
    ascii_characters = "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. "
    print("Got :", str(ascii_characters), "\n-=*=-\n\n")
  if ascii_choice == 6:
    ascii_characters = " .'`^\",:;Il!i><~+_-?][}{1)(|\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"
    print("Got :", str(ascii_characters), "\n-=*=-\n\n")
  if ascii_choice == 7:
    ascii_characters = "ÆÑÊŒØMÉËÈÃÂWQBÅæ#NÁþEÄÀHKRŽœXgÐêqÛŠÕÔA€ßpmãâG¶øðé8ÚÜ$ëdÙýèÓÞÖåÿÒb¥FDñáZPäšÇàhû§ÝkŸ®S9žUTe6µOyxÎ¾f4õ5ôú&aü™2ùçw©Y£0VÍL±3ÏÌóC@nöòs¢u‰½¼‡zJƒ%¤Itocîrjv1lí=ïì<>i7†[¿?×}*{+()\/»«•¬|!¡÷¦¯—^ª„”“~³º²–°¹‹›;:’‘‚’˜ˆ¸…·¨´`"
    print("Got :", str(ascii_characters), "\n-=*=-\n\n")
  if ascii_choice == 8:
    ascii_characters = "`´¨·…¸ˆ˜’‚‘’:;›‹¹°–²º³~“”„ª^—¯¦÷¡!|¬•«»/\)(+{*}×?¿[†7i><ìï=íl1vjrîcotI¤%ƒJz‡¼½‰u¢sòön@CóÌÏ3±LÍV0£Y©wçù2™üa&úô5õ4f¾ÎxyOµ6eTUž9S®ŸkÝ§ûhàÇšäPZáñDF¥bÒÿåÖÞÓèýÙdë$ÜÚ8éðø¶Gâãmpß€AÔÕŠÛqêÐgXœŽRKHÀÄEþÁN#æÅBQWÂÃÈËÉMØŒÊÑÆ"
    print("Got :", str(ascii_characters), "\n-=*=-\n\n")

  if ascii_choice == 9:
    print("Got :", str(ascii_choice),
          "Select a charset of at least 11 letters, \n-=*=-\n\n")
    ascii_characters = input("Set range from 0 (White) to any (Black): ")
    print("Got :", str(ascii_characters), "\n-=*=-\n\n")

  #open the image
  # image = Image.open('image.png')

  #resize the image
  image = image.resize(((width * 2), height))

  #convert the image to RGBA then grayscale
  image = image.convert("RGB")
  # Prompt the user for color option
  use_color = input("Do you want to use color? (y/n): ").lower().strip()
  if use_color == "n":
    image = image.convert('L')
  else:
    brightness = float(input("Brightness? (float) : ").strip() or 1)
    image = ImageEnhance.Brightness(image).enhance(brightness)

  # Convert the image to ASCII text
  ascii_text = ""
  for y in range(image.height):
    for x in range(image.width):
      pixel = image.getpixel((x, y))
      if image.mode == "RGB" and use_color == "y":
        r, g, b = pixel[:3]

        
        # Convert to grayscale
        op = image.convert('L')
        greypixel = op.getpixel((x, y))

        index = int(greypixel / 256 * len(ascii_characters))

        # RGBtoANSI(text='Green text on a white background',foregound=[0, 255, 0], background=[255, 255, 255]))
        ascii_text += RGBtoANSI(text=f"{ascii_characters[index]}", foregound=[r, g, b])
      else:
        gray_value = pixel
        index = int(gray_value / 256 * len(ascii_characters))
        ascii_text += ascii_characters[index]

    # Add ANSI escape code to reset color at the end of each line if using color
    if image.mode == "RGB" and use_color == "y":
      ascii_text += ANSI_RESET

    ascii_text += '\n'

  # Print the colored or grayscale ASCII text
  print(ascii_text)

  # The text contains ANSI escape codes, but we want to retain them without escaping them
  print("Raw ASCII art:\n")

  lcase = ascii_text.replace("\033", "\\033").replace("\\033[0m", "")+ANSI_RESET

  print(lcase)

  # open the file
  f = open("out.txt", "a")

  
  # write the string to the file
  f.write("\n" + f"""
-=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=-
{ascii_text}
-=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=- -=*=-
""")

  # open the file
  f = open("links.txt", "a")

  # write the string to the file
  f.write(f"{ URL } -> w: {width}, h: {height}, '{ascii_characters}'\n")

  # close the file
  f.close()
  sleep(2.00)
