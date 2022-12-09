from translate import Translator  # google translate
from reverso_context_api import Client  # reverso translate

# this module was written by Anthony Aboussafy
# It utiltizes APIs from Reverso and Google Translate. It is a very simple project
# the reverso API currently has issues


# translate {text} using reverso module//ISSUES WITH MODULE...
#                                   ONLY RETURNS TRANSLATION FOR SMALL STRINGS
def reverso_translate(text, from_lang='en', to_lang='fr'):
    client = Client(from_lang, to_lang)
    reverso_translation = list(client.get_translations(text, from_lang, to_lang))
    try:
        return reverso_translation[0]
    except:
        print("reverso translation did not work")
        return None


# translate {text} using google translate module
def google_translate(text, from_lang='en', to_lang='fr'):
    translator = Translator(to_lang=to_lang)
    google_translation = translator.translate(text)
    # print(google_translation)
    return google_translation


# Helper function translate_loop. Prints outputs for both Reverso and Google Translate
def translate(to_input=True):
    if to_input:
        text = input("Enter some text to translate to french:\t\t")
    else:
        text = "hello there good friend"
    print("text to translate: ", text)

    print("\nREVERSO TRANSLATION:")
    print(reverso_translate(text))

    print("\nGOOGLE TRANSLATION:")
    print(google_translate(text))


# Test function, loops interations number of times. To test output quality of both modules
def translate_loop(iterations=100):
    for i in range(1, iterations + 1):
        print(f"-----\tTest # {i}\t-----")
        translate()
        print("------------------------------\n")
    print("\n-----\tTests complete\t-----")


# function that translates a file of pathname = {filname}
def translate_txt(filename):
    file_read = open(filename, "r")
    text = file_read.read()
    file_read.close()
    return google_translate(text)


# writes a string {text} to pathname =  {filename}
def write_translation_to_file(text, filename):
    file_write = open(filename, "w")
    file_write.write(text)
    file_write.close()


# function that takes a filepath = {filename}, translates it and saves it as {filename}fr.
def translate_read_write(filename, output_filename=False):
    text = translate_txt(filename)

    if not output_filename:
        output_filename = filename.split(".")
        output_filename = output_filename[0] + "fr." + output_filename[1]
    write_translation_to_file(text, output_filename)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(google_translate("Hello my friend"))
    print(google_translate("Hello my friend","en","es"))
    # translate_test_loop(2)
    # print(translate_txt("test_text.txt"))
    translate_read_write("test_text.txt")
    translate_read_write("test_text.txt", "test_output_filename.txt")
