# ------------------------------------------ # Exercise for translattion

from translate import Translator

# translator = Translator(to_lang="ja")
# try:
#   with open("Udemy/files/text-file.text", mode="r") as myFile:
#     text = myFile.read()
#     translation = translator.translate(text)
#     print(translation)
# except FileNotFoundError as e:
#   print("Check your file path!")

translator = Translator(to_lang="hi")
try:
  with open("Udemy/files/text-file.text", mode="r") as myFile:
    text = myFile.read()
    translation = translator.translate(text)
    print(translation)
    with open("Udemy/files/text-file-hi-tran.text", mode="w") as hindiFile:# Write in new file
      hindiFile.write(translation)
except FileNotFoundError as e:
  print("Check your file path!")