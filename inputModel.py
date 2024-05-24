import json                                       #pythonic JS 

class inputA(object):
	def __init__(self, input):
		self.input = input
		
	def getMessage(self):
		return self.input['message'].get('message_id')

	def getText(self):
		text = self.input['message'].get('text')
		if text:
			text = text.encode('utf-8','strict') 
		return text
		
	def getLocation(self):
		return self.input['message'].get('location')
