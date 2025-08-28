def get_number_words(text):
  num_words = 0
  for words in text.split():
    num_words += 1
  return f"Found {num_words} total words"

def count_chars(text):
  count_dict = {}
  for char in text.lower():
    if char not in count_dict:
      count_dict[char] = 1
    else:
      count_dict[char] += 1
  return count_dict

def sorted_dict(count_dict):
  char_list = []
  for key, value in count_dict.items():
    char_list.append({'char':key, 'num':value})
  char_list.sort(key=lambda x: x['num'], reverse=True)
  return char_list
  #filtered_dict = [item for item in char_list if item['char'].isalpha()]
