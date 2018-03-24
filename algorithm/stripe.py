import re
def next_server_number(server_list):
	if server_list is None:
		raise Exception("Invalid server_list")

	server_list.sort()

	index = 0
	while index < len(server_list):
		if index + 1 != server_list[index]:
			return index + 1
		index += 1
	return index + 1

class Tracker(object):
	def __init__(self):
		self.mapping = dict()

	def allocate(self, host_type):
		if host_type not in self.mapping:
			self.mapping[host_type] = []
		host_list = self.mapping[host_type]
		host_number = next_server_number(host_list)
		host_list.append(host_number)
		host_name = '%s%s' % (host_type, host_number)
		return host_name


	def deallocate(self, host_name):
		regext_obj = re.search("(\D+)(\d+)", host_name)
		host_type = regext_obj.group(1)
		host_number = int(regext_obj.group(2))
		if host_type in self.mapping:
			host_list = self.mapping[host_type]
			host_list.remove(host_number)



# []
# return next available one

# []

# {"host_type": []}

# allocate:{}
# deallocate:[]


if __name__ == "__main__":
# >> tracker = Tracker.new()
# >> tracker.allocate("apibox")
# "apibox1"
# >> tracker.allocate("apibox")
# "apibox2"
# >> tracker.deallocate("apibox1")
# nil
# >> tracker.allocate("apibox")
# "apibox1"
# >> tracker.allocate("sitebox")
# "sitebox1"
	tracker = Tracker()
	print tracker.allocate("apibox")
	print tracker.allocate("apibox")
	print tracker.allocate("apibox")
	tracker.deallocate("apibox1")
	print tracker.allocate("apibox")
	print tracker.allocate("apibox")
	print tracker.allocate("apibox")
	print tracker.allocate("apibox")
	print tracker.allocate("apibox")
	tracker.deallocate("apibox2")
	print tracker.allocate("apibox")
	print tracker.allocate("apibox")
	print tracker.allocate("apibox")
	print tracker.allocate("apibox")
	print tracker.allocate("sitebox")

	server_list = [5, 3, 1]
	result = next_server_number(server_list)
  	assert result == 2, result

  	server_list = [5, 4, 1, 2]
	result = next_server_number(server_list)
  	assert result == 3, result

  	server_list = [3, 2, 1]
	result = next_server_number(server_list)
  	assert result == 4, result

  	server_list = [2, 3]
	result = next_server_number(server_list)
  	assert result == 1, result

  	server_list = []
	result = next_server_number(server_list)
  	assert result == 1, result

	# server_list = None
	server_list = [1,2,3,8,10,14]
	server_list = [1,1,2,3]