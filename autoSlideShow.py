import time, pyautogui

pauseTime = 15 #Set this to the amount of time that you want to wait on each slide

numberOfSlides = 22 #Set this to the number of slides in the presentation. If you don't know an exact number, guess high, it will just pause for the extra slides at the end.

loopForever = True #Set this to False if you want it to look a finite number of times

numberOfLoops = 1 #If you want the slide show to run a finite number of times, set this to the number of times you want it to run.

loopsDone = 0

#Actual Script
time.sleep(10) #This is just a delay to allow you to open the aplication you want to scroll through.
while True:
	i=0
	t=0
	while i < numberOfSlides:
		pyautogui.press('right') #This creates a keypress that will advance the slide to the right.
		time.sleep(pauseTime)
		i+=1
	while t < numberOfSlides:
		pyautogui.press('left') #This creates a keypress that will advance the slide to the left.
		time.sleep(.1)
		t+=1
	if not loopForever:
		if loopsDone < numberOfLoops:
			loopsDone += 1
		else:
			break
