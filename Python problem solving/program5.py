
def find(s1, s2):
	

	len__ = len(s1)
	len_1 = len(s2)

	
	if (len__ != len_1):
		return False

	
	d = [0 for i in range(len__)]


	d[0] = ord(s2[0]) - ord(s1[0])


	for i in range(1, len__, 1):
		
	
		if (s1[i] > s2[i]):
			return False

		else:
			
	
			d[i] = ord(s2[i]) - ord(s1[i])
	
	
	for i in range(len__ - 1):
		
	
		if (d[i] < d[i + 1]):
			return False

	
	return True


if __name__ == '__main__':

	s1 = "abcd"
	s2 = "bcdd"

	
	
	if (find(s1, s2)):
		print("Equal difference")
	else:
		print("UN equal difference")


