from Tkinter import *
from tabs import *

class Group:
	def __init__(self, master, caller = None):
		self.master = master
		self.caller = caller
		self.flows = [] # A list of all the flows
		self.numCards = 1
		self.userHeight = 10 # called userHeight to remind me to make it user configureable
		self.userWidth = 30 # called userWidth to remind me to make it user configureable
		self.currentFlow = None
		self.currentCard = None
		flow = self.addFlow()
		return

	def addFlow(self):
		newFlow = {}
		newFlow['frame'] = Frame(self.master)
		newFlow['frame'].pack(side = LEFT)
		newFlow['title'] = Label(newFlow['frame'], text = "Flow")
		newFlow['title'].pack(side = TOP)
		newFlow['cards'] = [] # A list of all the cards in the flow
		while len(newFlow['cards']) < self.numCards:
			self.addCard(newFlow)
		newFlow['cards'][self.currentCard].focus()
		self.currentFlow = len(self.flows)
		self.flows.append(newFlow)
		return newFlow

	def addCard(self, flow):
		newCard = Text(
			flow['frame'], 
			height = self.userHeight, 
			width = self.userWidth,
			borderwidth = 1,
			relief = RAISED
		)
		newCard.pack(side = TOP)
		newCard.bind('<Key>', self.update_card_size)
		newCard.bind('<Return>', lambda event, flow=flow: self.moveCard(flow, event))
		newCard.bind('<Up>', lambda event, flow=flow: self.moveCard(flow, event))
		newCard.bind('<Down>', lambda event, flow=flow: self.moveCard(flow, event))
		newCard.bind("<Right>", lambda event, flow=flow: self.moveFlow(flow, event))
		newCard.bind("<Left>", lambda event, flow=flow: self.moveFlow(flow, event))
		newCard.bind("[", lambda event: self.caller.moveTab(event))
		newCard.bind("]", lambda event: self.caller.moveTab(event))
		self.currentCard = len(flow['cards'])
		flow['cards'].append(newCard)
		if len(flow['cards']) > self.numCards: 
			self.numCards = len(flow['cards'])
		for flow in self.flows:
			while len(flow['cards']) < self.numCards:
				self.addCard(flow)
		return newCard

	def moveFlow(self, flow, event):
		move = 0
		if event.keysym == 'Right':
			move = 1
		elif event.keysym == 'Left':
			move = -1
		index = self.currentFlow
		if index+move in range(len(self.flows)):
			self.flows[index+move]['cards'][self.currentCard].focus()
		else:
			self.addFlow()
		return "break"

	def moveCard(self, flow, event):
		move = 0
		if event.keysym == 'Up':
			move = -1
		elif event.keysym == 'Down' or event.keysym == 'Return':
			move = 1
		index = self.currentCard
		if index+move in range(len(flow['cards'])):
			flow['cards'][index+move].focus()
			self.currentCard = index+move
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

class App:
	def __init__(self, master):
		self.master = master
		# self.options = loadConfigFile("config.txt")
		self.tabBar = TabBar(master)
		self.tabs = []
		self.addTab("Tab")
		self.tabBar.show()

	def addTab(self, name):
		newTab = Tab(self.master, name)
		newTabStuff = {}
		newTabStuff['tab'] = newTab
		newTabStuff['name'] = name
		newTabStuff['group'] = Group(newTab, caller = self)
		self.tabBar.add(newTab)
		self.tabs.append(newTabStuff)
		return newTabStuff

	def moveTab(self, event):
		move = 0
		if event.char == '[':
			move = -1
		elif event.char == ']':
			move = 1
		index = self.tabBar.currentTab()
		if index+move in range(len(self.tabs)):
			self.tabBar.switch_tab(index+move)
		else:
			self.addTab("Tab")
			self.tabBar.switch_tab(-1)
		return "break"

root = Tk()
app = App(root)
root.mainloop()
