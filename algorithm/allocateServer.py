def allocateServer2(server_list):
	if server_list is None:
		return -1

	if len(server_list) == 0:
		return 1

	start = 0
	end = len(server_list) - 1

	# check boundaries
	if server_list[start] > 1:
		return 1
	if server_list[end] == len(server_list):
		return server_list[end] + 1

	while start + 1 < end:
		middle = start + (end - start) / 2
		if middle + 1 == server_list[middle]:
			start = middle
		elif middle + 1 < server_list[middle]:
			end = middle - 1
	
	return server_list[start] + 1

def allocateServer(server_list):
	if server_list is None or len(server_list) == 0:
		return -1

	index = 0

	while index < len(server_list):
		if server_list[index] != index + 1:
			return index + 1
		index += 1
	return index + 1

if __name__ == "__main__":
	server_list = []
	result = allocateServer(server_list)
	assert result == 1, result

	server_list = [1,2,3,5]
	result = allocateServer(server_list)
	assert result == 4, result

	server_list = [1,2,3,4,5,10,13,15,21]
	result = allocateServer(server_list)
	assert result == 6, result

	server_list = [2,3,4,5,10,13,15,21]
	result = allocateServer(server_list)
	assert result == 1, result

	server_list = [5,10,13,15,21]
	result = allocateServer(server_list)
	assert result == 1, result

	server_list = [1,2,3,4,5]
	result = allocateServer(server_list)
	assert result == 6, result

	server_list = [1,3,5,6,9]
	result = allocateServer(server_list)
	assert result == 2, result

	server_list = [1,2,4,5,6,7,8,10,11,12,15,18,20,23,27,29]
	result = allocateServer(server_list)
	assert result == 3, result
