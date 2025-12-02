from stats import get_num_words, get_num_char, sort_and_filter
import sys

if len(sys.argv) < 2:
  print('Usage: python3 main.py <path_to_book>')
  sys.exit(1)
def get_book_text(path_to_file):
  with open(path_to_file) as f:
    file_contents = f.read()
    return file_contents
  
def main():
  book_text = get_book_text(sys.argv[1])
  words_count = get_num_words(book_text)
  count_chars = get_num_char(book_text)
  sorted_dict = sort_and_filter(count_chars)

  print('============ BOOKBOT ============')
  print(f'Analyzing book found at {sys.argv[1]}...')
  print('----------- Word Count ----------')
  print(f'Found {words_count} total words')
  print('--------- Character Count -------')
  for item in sorted_dict:
    print(f'{item["char"]}: {item["num"]}')
  print('============= END ===============')

main()     