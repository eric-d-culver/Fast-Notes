from Tkinter import *

class App:
	def __init__(self, master):
		self.outerFrame = Frame(master)
		self.outerFrame.pack(side = TOP)
		self.flows = [] # A list of all the flows
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
		self.addCard(newFlow).focus()
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
		newCard.bind("<Right>", lambda event, flow=flow: self.moveFlow(flow, event))
		flow['cards'].append(newCard)
		return newCard

	def moveFlow(self, flow, event): # only moves right for now, add left
		for index, f in enumerate(self.flows):
			if f == flow:
				if index+1 < len(self.flows):
					self.addCard(self.flows[index+1]).focus()
				else:
					self.addFlow()
		return "break"

	def moveCard(self, flow, event): # only moves down when Enter (Return) is pressed, perhaps add Up and Down arrows to move?
		for index, card in enumerate(flow['cards']):
			if card == event.widget:
				if index+1 < len(flow['cards']):
					flow['cards'][index+1].focus()
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
app = App(root)
root.mainloop()
