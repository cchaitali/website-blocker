import time
import os
from datetime import datetime as dt

hosts_path = r"C:\Windows\System32\drivers\etc\hosts"

localhost_IP = "127.0.0.1"

path_to_blocking_list_file = "<set_path_here>"
with open(os.path.join(path_to_blocking_list_file, "blocking_list.txt"), "r") as input_file:
	websites_to_block = input_file.readlines()

start_hour = 9
end_hour = 17

while True:
	start_time = dt(dt.now().year, dt.now().month, dt.now().day, start_hour)
	end_time = dt(dt.now().year, dt.now().month, dt.now().day, end_hour)
	if start_time < dt.now() < end_time:
		with open(hosts_path, "r+") as hosts_file:
			hosts_contents = hosts_file.read()
			for website in websites_to_block:
				if not website in hosts_contents:
					hosts_file.write(localhost_IP + " " + website)
	else:
		with open(hosts_path, "r+") as hosts_file:
			hosts_contents = hosts_file.readlines()
			hosts_file.seek(0)
			for line in hosts_contents:
				if not any(website in line for website in websites_to_block):
					hosts_file.write(line)
			hosts_file.truncate()
	time.sleep(5)
