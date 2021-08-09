import sys
from Cache import *
import os

L2_cache=Cache(19,6,8)
L3_cache=Cache(21,6,16)

def invalidate_inclusive(L2_cache, tag , set_no):
	tag=format(tag,'047b')
	set_no=format(set_no,'011b')
	temp_add=tag+set_no
	L2_tag=temp_add[:48]
	L2_tag=int(L2_tag,2)
	L2_set=temp_add[48:58]
	L2_set=int(L2_set,2)

	if L2_set in L2_cache.cache_structure :
		if L2_tag in L2_cache.cache_structure[L2_set]:
			L2_cache.cache_structure[L2_set][L2_tag]=0


def Nine_policy(L2_cache, L3_cache, address):
	flag2=L2_cache.isMissorHit(address)
	if flag2==0:
		L2_cache.miss+=1
		flag3=L3_cache.isMissorHit(address)
		if flag3==1:
			L3_cache.hits+=1
			set_no,replaced=L2_cache.LRU(address)
		else:
			L3_cache.miss+=1
			set_no, replaced=L3_cache.LRU(address)
			L2_cache.LRU(address)
	else:
		L2_cache.hits+=1


def inclusive_policy(L2_cache, L3_cache, address):
	flag2=L2_cache.isMissorHit(address)
	if flag2==0:
		L2_cache.miss+=1
		flag3=L3_cache.isMissorHit(address)
		if flag3==1:
			L3_cache.hits+=1
			set_no,replaced=L2_cache.LRU(address)
		else:
			L3_cache.miss+=1
			set_no, replaced=L3_cache.LRU(address)
			if replaced!=None:
				invalidate_inclusive(L2_cache,replaced[0],set_no)
			L2_cache.LRU(address)
	else:
		L2_cache.hits+=1

def invalidate_exclusive(L3_cache, address):
	address=format(address,'064b')
	tag=address[:47]
	set_number=address[47:58]
	tag=int(tag,2)
	set_number=int(set_number,2)

	L3_cache.cache_structure[set_number][tag]=0


def exclusive_policy(L2_cache, L3_cache, address):
	flag2=L2_cache.isMissorHit(address)
	if flag2==0:
		L2_cache.miss+=1
		flag3=L3_cache.isMissorHit(address)
		if flag3==1:
			L3_cache.hits+=1
			set_no, replaced = L2_cache.LRU(address)
			invalidate_exclusive(L3_cache,address)
		else:
			L3_cache.miss+=1
			L3_cache.LRU(address) 
			set_no, replaced = L2_cache.LRU(address)
			invalidate_exclusive(L3_cache, address)
		if replaced!=None:
				replaced=format(replaced[0],'048b')
				set_no=format(set_no,'010b')
				dummy_bits='0'*6
				temp_add=replaced+set_no+dummy_bits
				temp_add=int(temp_add,2)
				L3_cache.LRU(temp_add)
	else:
		L2_cache.hits+=1

policy_dict={1:"Inclusive Policy", 2:"Nine Policy", 3:"Exclusive Policy"}
application_name=sys.argv[1]
policy=int(sys.argv[2])

input_file_name=application_name + ".txt"	

direct=os.getcwd()
os.chdir("..")
os.chdir("traces")

fp=open(input_file_name,"r")
f1=fp.readlines()

print("Processed file : " + str(input_file_name))
print("Policy Used : " + policy_dict[policy])
count=0
for line in f1:
	address=line
	address=int(address)
	if policy==1:
		inclusive_policy(L2_cache, L3_cache, address)
	if policy==2:
		Nine_policy(L2_cache,L3_cache, address)
	if policy==3:
		exclusive_policy(L2_cache, L3_cache, address)


print("For L2 Cache : ")
print("Hits: "+ str(L2_cache.hits))
print("Miss: "+ str(L2_cache.miss))

print("For L3 Cache : ")
print("Hits: "+ str(L3_cache.hits))
print("Miss: "+ str(L3_cache.miss))

fp.close()