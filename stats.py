def get_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
  return file_contents


def get_num_words(file_path):
  file_contents = get_text(file_path)
  ##file_word_list = file_contents.split()
  count_words = len(file_contents.split())
  return count_words

def get_letter_count(file_path):
  c = 0
  pos = 0
  letter_count = {}
  lowercase_file_contents = get_text(file_path).lower()
  unique_chars = dict.fromkeys(lowercase_file_contents)

  for c in unique_chars:
    char_count = 0
    for character in lowercase_file_contents:
      if character == c:
        char_count += 1
    unique_chars[c] = char_count
  return unique_chars 



def get_ordered_dict(file_path):
  unique_chars = get_letter_count(file_path)
  list_of_dicts = []

  for key, value in unique_chars.items():
    if key.isalpha():
      list_of_dicts.append({"char": key, "num": value})
  
  def sort_on(list_of_dicts):
    return list_of_dicts["num"]

  list_of_dicts.sort(reverse=True,key=sort_on)
  


  return list_of_dicts

