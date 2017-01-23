from nltk.stem import SnowballStemmer
from nltk.stem.api import StemmerI
import nltk
import json

class ParticleStemmer(SnowballStemmer):

	def __init__(self, language="english", ignore_stopwords=False, suffix_rule_list={}):
		super().__init__(language=language, ignore_stopwords=ignore_stopwords)
		if language == "english":
			self.stemmer._EnglishStemmer__special_words.update({
				"experiment":"experiment", 
				"experimented":"experiment", 
				"experimenting":"experiment", 
				"experiments":"experiment",
				'organization': 'organiz',
				"organization's": 'organiz',
				'organizational': 'organiz',
				'organizationally': 'organiz',
				'organizations': 'organiz',
				'organize': 'organiz',
				'organized': 'organiz',
				'organizer': 'organiz',
				'organizers': 'organiz',
				'organizes': 'organiz',
				'organizing': 'organiz',
				'science': 'scient',
				'sciences': 'scient',
				'scientific': 'scient',
				'scientifically': 'scient',
				'scientist': 'scient',
				'scientistic': 'scient',
				'scientists': 'scient',
				'animal': 'animal',
				'animalism': 'animal',
				'animalistic': 'animal',
				'animalities': 'animal',
				'animality': 'animal',
				'animals': 'animal',
				})
			
			from partstem.word_list import word_list
			self.word_list = word_list
			self.word_list += nltk.corpus.words.words()
			
			self.stem = self.__stem
			self.suffix_rule_list = {
				'ant': {"with": ['ation'], "exception": []},
				'eti': {"with": ['ant', ''], "exception": []},
				'or': {"with": ['ion'], "exception": []},
				'um': {"with": ['a'], "exception": ["medium"]},
				'a': {"with": ['um'], "exception": ["media"]},
				'ri': {"with": [' -ried'], "exception": []},
				'er': {"with": ['y'], "exception": []},
				'al': {"with": ['us'], "exception": ["animal"]},
				'us': {"with": ['al'], "exception": []},
				'ifi': {"with": ['e'], "exception": []},
				'e': {"with": ['ification'], "exception": []},
				'ion': {"with": ['e'], "exception": []},
				'i': {"with": ['e', 'us'], "exception": []},
				'si': {"with": ['sis'], "exception": []},
				's': {"with": ['sis'], "exception": []},
				't': {"with": ['sis'], "exception": []},
				'z': {"with": ['sis'], "exception": []},
				"ier": {"with": ["ying", ""], "exception": []},
				"abl": {"with": ["es", ""], "exception": ["stabl", "capabl"]},
				"th": {"with": [""], "exception": []},
				"atori": {"with": ["ation"], "exception": []},
				"ori": {"with": ["ion"], "exception": []},
				"ous": {"with": ["y", "", "e", "on", "ity"], "exception": []},
				"ic": {"with": ["", "e"], "exception": ["sonic"]},
				"iti": {"with": ["est+ification"], "exception": []},
				"iz": {"with": ["ize", "izate"], "exception": []},
				"at": {"with": ["atic"], "exception": []},
				'if': {"with": ["ity+est", "e"], "exception": []}
			}
			self.suffix_rule_list.update(suffix_rule_list)
			self.suffix_list = sorted(list(self.suffix_rule_list.keys()), key=lambda x: -len(x))

	def __stem(self, word, return_snowball=False):
		if not word.startswith("improv"):
			remove_suffix = {"isate":"izate", "isated":"izated", "isating":"izating", "isates":"izates"}
			for key in remove_suffix.keys():
				if word.endswith(remove_suffix[key]):
					word = word[:-len(key)] + remove_suffix[key]
					break

			remove_suffix = {"ise":"ize", "ised":"ized", "ising":"izing", "ises":"izes"}
			for key in remove_suffix.keys():
				if word.endswith(remove_suffix[key]):
					new_word = word[:-len(key)] + remove_suffix[key]
					if new_word in self.word_list:
						word = new_word
						break

		
		word = self.stemmer.stem(word)
		stem_word = word
		num = 0
		if word not in list(self.stemmer._EnglishStemmer__special_words.keys()) + list(self.stemmer._EnglishStemmer__special_words.values()):
			while num < len(self.suffix_list):
				if stem_word.endswith(self.suffix_list[num]) and stem_word not in self.suffix_rule_list[self.suffix_list[num]]["exception"]:
					without_suffix = stem_word[:-len(self.suffix_list[num])]
					if len(without_suffix) == 0:
						num += 1
						continue
					for el in self.suffix_rule_list[self.suffix_list[num]]["with"]:

						el = el.replace("+", " ")
						el = el.replace("-", " -") if "-" in el and " -" not in el else el
						el = el.split(" ")
						key = True
						for el1 in el:
							if not ((without_suffix + el1 in self.word_list and not el1.startswith("-")) or (without_suffix + el1.replace("-", "") not in self.word_list and el1.startswith("-"))):
								key = False
								break
						if key:
							stem_word = without_suffix
							break
					break
				num += 1

		return (stem_word, word) if return_snowball else stem_word
			