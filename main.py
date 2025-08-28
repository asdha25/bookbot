from stats import get_number_words, count_chars, sorted_dict
import sys

if len(sys.argv) != 2:
  print("Usage: python3 main.py <path_to_book>") 
  sys.exit(1)

def get_book_text(filepath):
  with open(filepath) as f:
    file_content = f.read()
    return file_content

def main():
  book_text = get_book_text(sys.argv[1])
  book_dict = count_chars(book_text)

  print("============ BOOKBOT ============")
  print(f"Analyzing book found at {sys.argv[1]}...")
  print("----------- Word Count ----------")
  print(get_number_words(book_text))
  print("--------- Character Count -------")

  for item in sorted_dict(book_dict):
    if item['char'].isalpha():
      print(f"{item['char']}: {item['num']}")


  print("============= END ===============")

main()
