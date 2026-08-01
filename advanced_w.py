import math, time

def checkForLetters(x):
	for char in x:
		if char.lower() in "abcdefghijklmnopqrstuvwxyz'\"\\":
			return True

	return False

def advancedW(base, x): # yes the inverse of xk^x is W(x ln k)/ln k i know.
	if x < 0:
		raise ValueError("Failed to calculate for negative numbers")

	if x == 0:
		return 0

	if base == 1:
		return base

	if base == x:
		return 1

	k = math.log(x)/math.log(base) if x > 1 else x/base

	start = time.time()
	while abs(k*base**k - x) > 1e-15*x:
		numerator = k*base**k - x
		denominator = (base ** k) * (k*math.log(base) + 1)

		k = k - (numerator/denominator)

		if time.time() - start >= 2:
			break
		

	return k

if __name__ == "__main__":
	import tkinter
	window = tkinter.Tk()
	window.geometry("800x600")
	window.title("Advanced Extension for W Lambert Function")

	title = tkinter.Label(window, text="Advanced Extension of W Lambert Function*", font=("Arial", 16, "bold"))
	note = tkinter.Label(window, text="*Yes, I know you don't need to use a seperate function to calculate the inverse of xk^x where k is a constant.", font=("Arial", 8))


	class Labels:
		def __init__(self):
			self.base = tkinter.Label(window, text="Enter Base:")
			self.val = tkinter.Label(window, text="Enter Value:")
			self.result = tkinter.Label(window, text="Result:")

	class Entries:
		def __init__(self):
			self.base = tkinter.Entry(window, width="10", state="normal")
			self.val = tkinter.Entry(window, width="10", state="normal")
			self.result = tkinter.Entry(window, width="10", state="readonly")


	labels = Labels()
	entries = Entries()

	def calculate():
		base = entries.base.get().replace("e", f"{math.e}").replace("pi", f"{math.pi}").replace("^", "**")
		value = entries.val.get().replace("e", f"{math.e}").replace("pi", f"{math.pi}").replace("^", "**")

		if checkForLetters(base) or checkForLetters(value):
			entries.result.config(state="normal")
			entries.result.delete(0, tkinter.END)
			entries.result.insert(0, "I do not recognize this expression.")
			entries.result.config(state="readonly")

			return

		base = eval(base)
		value = eval(value)

		try:
			result = advancedW(base, value)
			result = int(result) if result == int(result) else result

			entries.result.config(state="normal")
			entries.result.delete(0, tkinter.END)
			entries.result.insert(0, str(result))
			entries.result.config(state="readonly")

		except ValueError:
			entries.result.config(state="normal")
			entries.result.delete(0, tkinter.END)
			entries.result.insert(0, "Cannot calculate for negative values.")
			entries.result.config(state="readonly")

	calculate_button = tkinter.Button(window, text="Calculate", command=calculate)

	title.place(x=170, y=20)

	labels.base.place(x=145, y=115)
	entries.base.place(x=145, y=135)

	labels.val.place(x=575, y=115)
	entries.val.place(x=575, y=135)

	labels.result.place(x=370, y=195)
	entries.result.place(x=357, y=215)

	calculate_button.place(x=358, y=240)

	note.place(x=125, y=575)

	window.mainloop()