#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

def get_first_part_of_name(name):
	i = 0
	for j in name:
		if j == '-':
			break
		i+=1
	bon = name[0:i]
	bon = bon.lower()
	return bon.capitalize()
def get_random_sentence(animals, adjectives, fruits):
	def aa():
		return random.randrange(0, 3)
	return f"Aujourd’hui, j’ai vu un {animals[aa()]} s’emparer d’un panier `{adjectives[aa()]}` plein de {fruits[aa()]}."

def encrypt(text, shift):
	text = text.upper()
	new = ""
	for i in text:
		if (ord(i) <= 90) and (ord(i) >= 90-26):
			if ord(i) > 90-shift:
				i = chr(ord(i)-26)
			new += chr(ord(i)+shift)
		else:
			new += i
	return new

def decrypt(encrypted_text, shift):
	text = encrypted_text.upper()
	new = ""
	for i in text:
		if (ord(i) >= 90-26) and (ord(i) <= 90):
			if ord(i) <= 90 - 26 + shift:
				i = chr(ord(i) + 26)
			new += chr(ord(i) - shift)
		else:
			new += i
	return new


if __name__ == "__main__":
	parrot = "jEaN-MARC"
	print(f"Pour {parrot}, on a '{get_first_part_of_name(parrot)}'.")

	animals = ("chevreuil", "chien", "pigeon")
	adjectives = ("rouge", "officiel", "lourd")
	fruits = ("pommes", "kiwis", "mangue")
	print(get_random_sentence(animals, adjectives, fruits))
	
	print(encrypt("ABC", 1))
	print(encrypt("abc 123 XYZ", 3))
	print(decrypt("DEF 123 ABC", 3))
