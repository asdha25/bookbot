def get_num_words(text):
  words = text.split()
  return len(words)

def get_num_char(text):
  char_dict = {}
  for word in text.split():
    for char in word.lower():
      if char not in char_dict:
        char_dict[char] = 1
      else:
        char_dict[char] += 1
  
  return char_dict

def sort_and_filter(char_dict):
  char_list = []
  
  for key, value in char_dict.items():
    char_list.append({'char': key, 'num': value})
  
  char_list.sort(key=lambda x: x['num'],
                 reverse=True)

  filtered_dict = [item for item in char_list if item['char'].isalpha()]

  return filtered_dict