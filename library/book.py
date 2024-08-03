from dataclasses import dataclass


@dataclass
class Book:
	title: str = ''
	author: str = ''
	publication_year: str = ''
	available: bool = True
