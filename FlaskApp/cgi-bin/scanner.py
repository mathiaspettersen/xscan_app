import os


def scan():
	file = open("ip_user_input.txt", "r")
	ip_addr = file.read()
	print(ip_addr)

	os.system(f"nmap -T4 -p0-100 {ip_addr}")
	

scan()

