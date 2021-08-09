from math import *
from collections import OrderedDict

word_size=8 #assume everything in bytes

class Cache:
	def __init__(self,cache_size, block_size, associativity):
		self.cache_size=int(pow(2,cache_size))
		self.block_size=int(pow(2,block_size))
		self.associativity=associativity
		self.words_in_block=block_size//word_size
		self.num_of_sets=(self.cache_size//self.block_size)//self.associativity
		self.cache_structure={}
		self.hits=0
		self.miss=0

	def isMissorHit(self, address):   # Miss- 0 Hit-1
		address=format(address,'064b')
		tag_bits=int(64-(log2(self.num_of_sets))-(log2(self.block_size)))
		tag=address[:tag_bits]
		tag=int(tag,2)
		set_number=address[tag_bits:int(tag_bits+(log2(self.num_of_sets)))]
		set_number=int(set_number,2)
		if set_number in self.cache_structure:
			if tag in self.cache_structure[set_number]:
				if self.cache_structure[set_number][tag]==1:
					self.cache_structure[set_number].move_to_end(tag);
					return 1
				else:
					return 0
			else:
				return 0
		else:
			return 0

	def LRU(self,address):	
		address=format(address,'064b')
		tag_bits=int(64-(log2(self.num_of_sets))-(log2(self.block_size)))
		tag=address[:tag_bits]
		tag=int(tag,2)
		set_number=address[tag_bits:int(tag_bits+(log2(self.num_of_sets)))]
		set_number=int(set_number,2)
		if set_number not in self.cache_structure:
			self.cache_structure.update({set_number: OrderedDict() })
			self.cache_structure[set_number].update({tag : 1})
			return None,None
		else:
			if tag in self.cache_structure[set_number]:
				if self.cache_structure[set_number][tag]==0:
					self.cache_structure[set_number][tag]=1
					self.cache_structure[set_number].move_to_end(tag);
					return None, None
			else:
				if len(self.cache_structure[set_number])<self.associativity:
					self.cache_structure[set_number].update({tag:1})
					return None, None
				else:
					key_to_del=-1
					for key in self.cache_structure[set_number].keys():
						if self.cache_structure[set_number][key]==0:
							key_to_del=key
							break
					if key_to_del!=-1:
						deleted_tag=self.cache_structure[set_number][key_to_del]
						self.cache_structure[set_number].pop(key_to_del)
					
					else:
						deleted_tag=self.cache_structure[set_number].popitem(last=False)
					
					self.cache_structure[set_number].update({tag:1})
					return set_number, deleted_tag