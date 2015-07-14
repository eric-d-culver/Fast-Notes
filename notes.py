from Tkinter import *

class Group:
	def __init__(self, master):
		self.outerFrame = Frame(master)
		self.outerFrame.pack(side = TOP)
		self.flows = [] # A list of all the flows
		self.numCards = 1
		self.userHeight = 10 # called userHeight to remind me to make it user configureable
		self.userWidth = 30 # called userWidth to remind me to make it user configureable
		flow = self.addFlow()
		return

	def addFlow(self):
		newFlow = {}
		newFlow['frame'] = Frame(self.outerFrame)
		newFlow['frame'].pack(side = LEFT)
		newFlow['title'] = Label(newFlow['frame'], text = "Flow")
		newFlow['title'].pack(side = TOP)
		newFlow['cards'] = [] # A list of all the cards in the flow
		while len(newFlow['cards']) < self.numCards:
			self.addCard(newFlow)
		newFlow['cards'][0].focus()
		self.flows.append(newFlow)
		return newFlow

	def addCard(self, flow):
		newCard = Text(
			flow['frame'], 
			height = self.userHeight, 
			width = self.userWidth
		)
		newCard.pack(side = TOP)
		newCard.bind('<Key>', self.update_card_size)
		newCard.bind('<Return>', lambda event, flow=flow: self.moveCard(flow, event))
		newCard.bind('<Up>', lambda event, flow=flow: self.moveCard(flow, event))
		newCard.bind('<Down>', lambda event, flow=flow: self.moveCard(flow, event))
		newCard.bind("<Right>", lambda event, flow=flow: self.moveFlow(flow, event))
		newCard.bind("<Left>", lambda event, flow=flow: self.moveFlow(flow, event))
		flow['cards'].append(newCard)
		if len(flow['cards']) > self.numCards: self.numCards = len(flow['cards'])
		return newCard

	def moveFlow(self, flow, event):
		move = 0
		if event.keysym == 'Right':
			move = 1
		elif event.keysym == 'Left':
			move = -1
		for index, f in enumerate(self.flows):
			if f == flow:
				if index+move in range(len(self.flows)):
					self.addCard(self.flows[index+move]).focus()
				else:
					self.addFlow()
		return "break"

	def moveCard(self, flow, event):
		move = 0
		if event.keysym == 'Up':
			move = -1
		elif event.keysym == 'Down' or event.keysym == 'Return':
			move = 1
		for index, card in enumerate(flow['cards']):
			if card == event.widget:
				if index+move in range(len(flow['cards'])):
					flow['cards'][index+move].focus()
				else:
					self.addCard(flow).focus()
		return "break"

	def update_card_size(self, event):
		curCard = event.widget
		#lines = int(float(curCard.index(END))) # Returns the number of actual lines, as in, you have to press Enter to change it.
		# Need a function that returns the number of displayed lines.
		text_height = 1 + len(curCard.get("1.0", END))/curCard.cget("width")
		if curCard.cget("height") < text_height:
			curCard.config(height = text_height)

root = Tk()
group = Group(root)
root.mainloop()
