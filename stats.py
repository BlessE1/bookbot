def count_book_words(book_text):
	num_of_words = len(book_text.split())

	return f"Found {num_of_words} total words"

def count_book_characters(book_text):
	character_dict = {}
	characters = list(book_text.lower())

	for character in characters:
		character_dict[character] = character_dict.get(character, 0) + 1

	return character_dict

def sort_dictionary_by_counts(dict):
	list_of_dicts = []

	for char, count in dict.items():
		list_of_dicts.append({"char": char, "count": count})

	list_of_dicts.sort(reverse=True, key=lambda item: item["count"])

	return list_of_dicts
