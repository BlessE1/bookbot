import sys

from stats import count_book_words
from stats import count_book_characters
from stats import sort_dictionary_by_counts

def get_book_text(filepath):
	with open(filepath) as f:
		file_contents = f.read()

	return file_contents

def main():
	if len(sys.argv) < 2:
		print("Usage: python3 main.py <path_to_book>")
		sys.exit(1)

	book_filepath = sys.argv[1]
	book_text = get_book_text(book_filepath)
	num_book_words = count_book_words(book_text)
	book_characters_dict = count_book_characters(book_text)
	sorted_characters_list = sort_dictionary_by_counts(book_characters_dict)

	print("============ BOOKBOT ============")
	print(f"Analyzing book found at {book_filepath} ...")
	print("----------- Word Count ----------")
	print(num_book_words)
	print("--------- Character Count -------")

	for item in sorted_characters_list:
		if item["char"].isalpha():
			print(f"{item['char']}: {item['count']}")

	print("============= END ===============")

main()
