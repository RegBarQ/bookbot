from stats import get_num_words
from stats import get_ordered_dict
import sys

def main():
  ##file_contents = get_book_text("books/frankenstein.txt")
  ##file_word_list = count_book_words()
  ##print(file_word_list.count(",")}]

  if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)



  file_path = sys.argv[1]#"
  ##file_path = "books/frankenstein.txt"

  num_words = get_num_words(file_path)
  #print(f"Found {num_words} total words")

  ordered_dict = get_ordered_dict(file_path)
  print("============ BOOKBOT ============\n")
  print(f"Analyzing book found at {file_path}...\n")
  print("----------- Word Count ----------\n")
  print(f"Found {num_words} total words\n")
  print("--------- Character Count -------\n")
  for i in ordered_dict:
    #for key, value in i.items():
    #  print(f"{key}: {value}\n")
    print(f"{i["char"]}: {i["num"]}\n")

  #print(ordered_dict)

  

  ##print(file_word_list)

main()