from typing import List, Dict, Union, Optional
import csv

def load_data(
	filepath: str,
	delimiter: str = ',',
	headers: bool = True,
	encoding: str = 'utf-8'
) -> Union[List[Dict[str, str]], List[List[str]]]:
	"""Load a CSV file.

	Args:
		filepath: Path to the CSV file.
		delimiter: Field delimiter (default: ',').
		headers: If True, return a list of dicts using the first row as keys.
				 If False, return a list of rows (each a list of strings).
		encoding: File encoding (default: 'utf-8').

	Returns:
		List of dicts (if headers=True) or list of rows (if headers=False).

	Raises:
		FileNotFoundError: If the file does not exist.
		UnicodeDecodeError: If the file cannot be decoded with the given encoding.
		csv.Error: If there is a CSV parsing error.
	"""
	with open(filepath, newline='', encoding=encoding) as f:
		reader = csv.reader(f, delimiter=delimiter)
		try:
			if headers:
				rows = list(reader)
				if not rows:
					return []
				header = rows[0]
				return [dict(zip(header, row)) for row in rows[1:]]
			else:
				return [row for row in reader]
		except csv.Error:
			# re-raise to let caller handle
			raise
