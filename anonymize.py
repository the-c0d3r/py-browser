import urllib2
import random

class theanonymizer(urllib2.build_opener):
	""" Anonymizer Class which contain the functions
		of Changing The Browser's Proxy and The User-Agent.
		"""
	def __init__(self, proxies = [], user_agents = []):
		urllib2.build_opener.__init__(self)
		# btw, we can add more proxies and user_agents
		self.proxies = proxies + ['201.101.131.227:8080', '110.4.12.178:80',\
			'111.13.136.57:80', '107.150.97.140:80']
		self.user_agents = user_agents + ['Cyberdog/2.0', 'Mozilla/5.0 ',\
			'FireFox/6.01','IBM WebExplorer /v0.94', 'Opera/9.80'] 
		self.anonymize()
		
	def change_proxy(self): # Function which will change Browser Proxy.
		if self.proxies:
			index = random.randrange(0, len(self.proxies))
			self.ProxyHandler({'http': self.proxies[index]})
			
	def change_user_agent(self): # Function which will change the User-Agent.
		index = random.randrange(0, len(self.user_agents))
		self.addheaders = [('User-agent', (self.user_agents[index]))]
		
	def anonymize(self):
		self.change_proxy()
		self.change_user_agent()
