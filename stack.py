def match_params(expression):
	stack = []
	for char in expression:
		if char == '(':
			stack.append(char)
		elif char == ')':
			if len(stack) < 1:
				return False
			stack.pop()
	if len(stack) == 0:
		return True
	return False

if __name__ == "__main__":
	result = match_params("(adil)")
	if result:
		print("params matched")
	else:
		print("not matched")
