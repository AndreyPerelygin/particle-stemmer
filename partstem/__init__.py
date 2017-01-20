from nltk.stem import SnowballStemmer
from nltk.stem.api import StemmerI
import nltk
import json

class ParticleStemmer(SnowballStemmer):

	def __init__(self, language="english", ignore_stopwords=False, suffix_rule_list={}):
		super().__init__(language=language, ignore_stopwords=ignore_stopwords)
		if language == "english":
			self.stemmer._EnglishStemmer__special_words.update({
				"":"",
				})
			
			self.word_list = json.loads(open("word_list.json", "rb").read())
			self.word_list += nltk.corpus.words.words()
			
			self.stem = self.__stem
			self.suffix_rule_list = {
				'ant': {"with": ['ation'], "exception": []},
				'eti': {"with": ['ant', ''], "exception": []},
				'or': {"with": ['ion'], "exception": []},
				'um': {"with": ['a'], "exception": ["medium"]},
				'a': {"with": ['um'], "exception": ["media"]},
				'ri': {"with": [''], "exception": []},
				'er': {"with": ['y'], "exception": []},
				'al': {"with": ['us'], "exception": []},
				'us': {"with": ['al'], "exception": []},
				'ifi': {"with": ['e'], "exception": []},
				'e': {"with": ['ification'], "exception": []},
				'if': {"with": ['e'], "exception": []},
				'ion': {"with": ['e'], "exception": []},
				'i': {"with": ['e'], "exception": []},
				'si': {"with": ['sis'], "exception": []},
				's': {"with": ['sis'], "exception": []},
				't': {"with": ['sis'], "exception": []},
				'z': {"with": ['sis'], "exception": []},
				'ic': {"with": ['e'], "exception": []},
			}
			self.suffix_rule_list.update(suffix_rule_list)
			self.suffix_list = sorted(list(self.suffix_rule_list.keys()), key=lambda x: -len(x))

	def __stem(self, word, return_snowball=False):
		word = self.stemmer.stem(word)
		stem_word = word
		num = 0
		while num < len(self.suffix_list):
			if stem_word.endswith(self.suffix_list[num]) and stem_word not in self.suffix_rule_list[self.suffix_list[num]]["exception"]:
				without_suffix = stem_word[:-len(self.suffix_list[num])]
				for el in self.suffix_rule_list[self.suffix_list[num]]["with"]:
					if without_suffix + el in self.word_list:
						stem_word = without_suffix
						break
				break
			num += 1

		return (stem_word, word) if return_snowball else stem_word
		