import socket
import os
import re
import requests
import platform
def netinfo(bot,chat_id,message):
	local_ip = ''
	mac_address = ''
	public_ip = ''

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
		s.connect(('8.8.8.8', 80))
		local_ip = s.getsockname()[0]
	except:
		local_ip = os.popen('ipconfig | findstr IPv4').read().split('\n')[0].split(': ')[-1]


	try:
		if platform.system() == 'Windows':
			mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
		elif platform.system() == 'Darwin':
			ifconfig_output = os.popen('ifconfig').read()
			mac_address_matches = re.findall(r'ether\s+([^\s]+)', ifconfig_output)
			if mac_address_matches:
				mac_address = mac_address_matches[0]
	except:
		mac_address = 'Не найден'

	try:
		public_ip = requests.get('https://api.ipify.org').text
	except:
		public_ip = 'Не найден'

	response = f'Local IP: {local_ip}\nPublic IP: {public_ip}\nMAC Address: {mac_address}'
	bot.send_message(chat_id=chat_id, text=response)