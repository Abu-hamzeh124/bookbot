import sys
from stats import word_count
from stats import chars_dict_to_sorted_list
from stats import get_chars_dict
from stats import sort_on
def main():
     
    if len(sys.argv) == 2: 
       book_path = sys.argv[1]
       text = get_book_text(book_path)
       counts = get_chars_dict(text)
       sorted_letters = chars_dict_to_sorted_list(counts)
       for  item in sorted_letters: print(f"{item['char']}: {item['num']}")
       print(f"Found {counts} total words")
       
       
    else:
        print(f"Usage: python3 main.py <path_to_book>")
        sys.exit(1)   
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_cotents = f.read()
    return file_cotents    
main()  

    
