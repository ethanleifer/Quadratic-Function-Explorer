'''
File: QuadraticEquation.py
Description: Coding Assignment (Quadratic Function Explorer) 
Requirements: 
	In this assignment, which is intended to serve as a warmup in terms of putting together a complex, working project, you will set up a user-friendly interface so that a typical user can input values for A,  B, and C and interact with your program effectively. Your program should be able to let the user:
	i. modify/input the parameters A, B, and C
	ii. graph the corresponding function
	iii. clear the graph
	iv. show any real roots of the equation, graphically and/or otherwise
	v. display of the current equation with the input parameters shown to at least 2 decimal places of precision (you might want this to happen automatically)
	vi. zoom in or out of the graph as desired
	
READ.ME
	My 'Unique' feature is letting the user graph multiple functions. This makes keeping track of the different coeffs. and other variables extremely tricky without a class system where its easy to add functionality. My plan wasn't to do that at the begining. Because I pivoted it made my code extremely complicated. I ended up using two dimensial lists to keep track of coefficents plus Text (for the Roots and EQ) and Circle (for the roots on the graph) objects. It is 6 items long: 
			1. Coefficent a
			2. Coefficent b
			3. Coefficent c
			4. The first root as a Circle object
			5. The second root as a Circle object
			6. The Text object that includes the two roots and Quadratic Equation
	Instructions: 
		MAKE SURE YOU ARE READING THE QUESTIONS IN THE COMMAND LINE
		After running the code it will ask you to enter your first 3 coefficents to be able to graph your first function. Please enter your desired coefficents. Then it will plot the graph and the two roots as Circle objects. 
		If you type 'q' it will quit the program and close the graph window. 
		If you type 's' if you only have one equation (look below). If you have more then one Equation it will ask you if you want to show all of the coords or just a specific graph. For each graph that you choose (LOOK BELOW). 
			it will show the equation and the two roots and let you either the plot the Text Object on the graph yourself or let the computer place them right above or below the vertex (based on the graph). 
		If you type 'c' it will clear the graph win. Keeps root objects and text objects.  
		If you type 'g' it will let you graph a new function and plots the roots as Circle objects.
		If you type 'z' it will either zoom either in or out (You can only zoom out after you have zoomed in. The farthest you can zoom out is the orginal coordinantes) 
		If you type 'r' it will remove all of the text objects
			
	Notes:
		Because of the weird cases of the Quadratic Function (some have 1 root, some have two roots, some have no roots), Some already have had the text displayed, some don't, you can display the text more then once for each function. All of this is hard to keep track of. I would say the code works 95% of the time. The other 5% is when one of these irregular cases happened. 
Date Created: October 10, 2019
Date Last Modifed: October 16, 2019
'''

#Imports:
from DEgraphics import *
from math import *


def getCoefficents():
	"""Creates and returns a list of user specificed coefficents."""
	
	coefficents = []
	
	print("Please enter your desireed Coefficents: \n")
	
	#take user input for Coefficents
	
	a = input("Input the value you want for the A coefficent (A value cannot be equal to 0): ")
	coefficents.append(float(a))
	
	b = input("Input the value you want for B coefficent: ")
	coefficents.append(float(b))
	
	c= input("Input the value you want for C coefficent: ")
	coefficents.append(float(c))
		
	return coefficents
		
def computeDiscriminant(coefficents):
	"""Returns the Discriminat from a list of coefficents."""
	return coefficents[1]**2 - 4*coefficents[0]*coefficents[2];

def hasRoots(coefficents):
	"""returns True if the coefficents is greater then 0, False otherwise."""
	return computeDiscriminant(coefficents)>=0

	
def getRoots(coefficents):
	"""Compute the Roots of Quadratic Function using coefficents.
	
	Precondition: Discrinant =>0"""
	
	#computes discriminant
	d = computeDiscriminant(coefficents)
	
	a = coefficents[0]
	b = coefficents[1]
	c = coefficents[2]
	
	r1 = 0.0
	r2 = 0.0
	
	#calculates two roots
	r1=(-b+sqrt(d))/(2*a)
	r2=(-b-sqrt(d))/(2*a)

	roots = [r1,r2]
	return roots
	
def solveQuadraticFormula(x,coefficents):
	"""Solves the Quadratic Formula at x value with Coefficents supplied."""
	a = coefficents[0]
	b = coefficents[1]
	c = coefficents[2]
	
	return x**2*a+b*x+c

def graphQuadFunction(win, coefficents = [1,0,0]):
	"""Graphs a Quadratic Function on win and returns coefficents of that Graph."""
	
	
	if hasRoots(coefficents) !=  True:
		x=-10
		while(x<10):
			win.plot(x,solveQuadraticFormula(x, coefficents),"red")
			x+=.001
		return coefficents
		
	roots = getRoots(coefficents)
	
	#Plots the roots as circles
	c1 = Circle(Point(roots[0],0),.1)
	c2 = Circle(Point(roots[1],0),.1)
	c1.draw(win)
	c2.draw(win)
	
	#Plots the graph
	x=-10
	while(x<10):
		win.plot(x,solveQuadraticFormula(x, coefficents),"red")
		x+=.001
	
	coefficents.append(c1)
	coefficents.append(c2)
	return coefficents

def showRealRoots(coefficents):
	"""Returns string roots as (x1,y1), (x2,y2)"""
	if hasRoots(coefficents) !=  True:
		return "No Roots"
	
	roots = getRoots(coefficents)
	
	#When th the roots are equal
	if roots[0] == roots[1]:
		return "(" + str(roots[0]) + ",0)"
	return "(" + str(round(roots[0],2)) + ",0), (" + str(round(roots[1],2)) + ",0)"

	'''
	Graphing the roots on win
	roots = getRoots(coefficents)
	printroots = "r1 = (" + str(roots[0]) + ",0)\n r2 = (" + str(roots[1]) + ",0)"
	t =  Text(Point(-7,-7), printroots)
	t.draw(win)
	return t
	'''
	
def createQuadraticFormula(coefficents):
	"""Returns Quadratic Formula with correct + - signs as a string in the form ax^2 + bx + c and removes non existent terms."""
	
	# number version for ifs
	a = round(coefficents[0],2)
	b = round(coefficents[1],2)
	c = round(coefficents[2],2)

	# str version to add to equation
	A = str(round(coefficents[0],2))
	B = str(round(coefficents[1],2))
	C = str(round(coefficents[2],2))
	
	
	QuadEq = ""
	
	#A term:
	#Case: ax^2 (a n!= 1 or -1)
	if (a != 1.0 and a != -1.0):
		QuadEq += A + "x^2"
	#Case: ax^2 (a = -1)
	elif (a == -1.0):
		QuadEq += "-x^2"
	#Case: ax^2 (a = 1)
	elif (a == 1.0):
		QuadEq += "x^2"
	#Case: "" (a = 0)
	else: 
		QuadEq += ""
		
	#B Term:
	#Case: + bx (b > 0)
	if (b > 0.0):
		QuadEq += " + " + B + "x"
	#Case: + x (b = 1)
	elif (b == 1.0):
		QuadEq += " + x"
	#Case: "" (b = 0)
	elif (b == 0.0):
		QuadEq += ""
	#Case: - x (b = -1)
	elif (b == -1.0):
		QuadEq += " - x"
	#Case: - abs(b)x (b < 0)
	else: 
		QuadEq += " - " + str(abs(b)) + "x"
		
	#C Term:
	#Case: + C (c > 0)
	if (c > 0): 
		QuadEq += " + " + C
	#Case: "" (c = 0)
	elif (c == 0):
		QuadEq += ""
	#Case: - abs(c) (c < 0)	
	else:
		QuadEq += " - " + str(abs(c))
	
	return QuadEq

def showText(win,coefficents):
	"""Places the text on the graph win and returns Text object"""
	
	a = coefficents[0]
	b = coefficents[1]
	c = coefficents[2]
		
	
	#Check if the function has roots
	if hasRoots(coefficents) !=  True:
		roots = "No Roots"
	else:
		roots = getRoots(coefficents)
		
	#Ask if user wants to place equation or if it should be placed above or below vertex
	if input("Do you want to choose where the text is placed or have the text placed below the vertex (Please enter either: y or n): ") == "y":
		print("Click point on window where you want the information to be placed: ")
		point = win.getMouse()
		
	#Point is determinded by prgogram
	else: 
		#Should point be above or below vertex	
		if (a>0):
			extra = 2
		else:
			extra = -2
				
		#Calculates Vertex plus adds extra from above so text is not ontop of vertex
		point = Point(-b/(2*a),solveQuadraticFormula(-b/(2*a) + extra, coefficents))
	
	#create the quadratic equation
	quadEq = createQuadraticFormula(coefficents)
	
	#creates the text object with Roots and Quadratic Equation
	t= Text(point, "Roots: " + showRealRoots(coefficents) + "\n Equation: " + quadEq)
	
	#draws the text obj from above
	t.draw(win)
	
	#returns text obj
	return t

def removeText(win,coefficents):
	"""Removes the Text element for the coefficent from the graph"""
	
	t = coefficents.pop()
	t.undraw()
	return coefficents
	
	
def main():
	"""main function"""
	'''
	coefficents = getCoefficents()
	print(coefficents)
	print(createQuadraticFormula(coefficents))
	'''
	key = "g"
	
	
	win = DEGraphWin(width = 600, height = 600, title = "Quadratic Functions")
	win.toggleAxes()
	
	
	#keeps track of coefficents that are graphed
	coefficentList = []
	
	print("Quadractic Functions on a Graph:")

	while (key != "q"):
		
		#Clears the window
		if key == "c":
			win.clear()
			
		#Graph a new function
		if key == "g":

			coefficent = getCoefficents()
			coefficentList.append(graphQuadFunction(win,coefficent))
	
		#Show more information about function
		if key == "s":
			
		
			#check if there is only one item in coefficent list
			if len(coefficentList)==1:
				coefficentList[len(coefficentList)-1].append(showText(win, coefficentList[len(coefficentList)-1]))

			
			
			#ask user what equation they want to show the roots for (or all maybe)
			elif (input("Do you want to show more information for all of the graphs? (Please enter either: y or n): ") == "y"):
				i = 0
				newcoefficentList = []
				while (i<len(coefficentList)):
					print("For " + str(coefficentList[i][0:3]) + ":")
					newcoefficentList.append(coefficentList[i].append(showText(win, coefficentList[i])))
					i+=1
				coefficentList = newcoefficentList 
			else:
				print("Please type the number for which coeiffent you want to show more information for:")
				x=1
				i = 0
				#print the first 3 values of each coefficent
				while (i<len(coefficentList)):
					
					print("\t" + str(x) + ": " + str(coefficentList[i][0:3]))
					i+=1
					x+=1
				#
				userinput = int(input("Enter the number you want: "))-1
			
				coefficentList[userinput].append(showText(win, coefficentList[userinput]))
							
	
			
		#Removes all extra information from graph about specific functions
		if key == "r":
			
			
			i = 0
			newcoefficentList = []
			
			while (i<len(coefficentList)):
				coefficents = coefficentList[i]
				#Basic Text Obj to compare with type
				textobj = Text(Point(0,0), "TextObj")
				
				#check type of the last element to see if there is already a text object
				if type(coefficents[len(coefficents)-1])==(type(textobj)):
					print("Remove Text")
			
					newcoefficentList.append(removeText(win, coefficents))
				i+=1
			coefficentList = newcoefficentList
			
		#Zoom in or out depending on what you enter
		if key == "z":
			
			#Make sure you change plot function to x coords of the display
			if (input("Zoom in or out? (PLease enter either: in or out (To zoom out you already have to be zoomed in)): ")=="out"):
				win.zoom("out")					
			else:
				win.zoom("in")
				
			#Regraph all of the windows
			for coefficents in coefficentList:
				graphQuadFunction(win, coefficents)
		#asks user to input new command (for next run through code)
		key = input("\nEnter Next Command: 'q' to quit, 'c' to clears the graph, 'g' to graph new function, 's' to show more information about last function, 'r' to remove all text items, 'z' to zoom. More indepth instructions are at the top of Code: ")
	
	#closes the graph window
	win.close()

	
if __name__ == "__main__":
	main()