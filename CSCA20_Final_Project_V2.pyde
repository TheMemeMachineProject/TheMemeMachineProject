#-----------------------------------------------------------------------
#---------------START---------------------------------------------------
def setup():
    global CurrentImage, img1, img2, img3, Dogetracker, Cattracker, Poohtracker, Ironictracker, Pikachutracker, Bobtracker, MemeFont, MemeListDoge, MemeListCat, MemeListPooh, MemeListIronicDoge, MemeListPikachu, MemeListBob, tracker, DogeTemplate, BadLuckBrianTemplate, PoohTemplate, SpongeTemplate, SuccessKidTemplate, answer, answer2, random #We want to make these accessible throughout the entire code
    size(1920, 1080) #Sets the window size
    import random #Allows us to use the random generator
    img1 = loadImage("Homescreen.jpg") 
    img2 = loadImage("ShrekBackground.png")
    img3 = loadImage("NyanBackground.png")
    CurrentImage = img1 #This will serve as the variable that will load the current meme image
    Dogetracker = -1 #We start at -1 instead of 0 because as soon as the key is pressed the tracker gets a number added. We want to count from 0, so we made it -1.
    Cattracker = -1 #Doing it this way allows for randomization when the tracker reaches the maximimum limit
    Poohtracker = -1
    Ironictracker = -1
    Pikachutracker = -1
    Bobtracker = -1
    fontList = PFont.list() #This is a list of fonts. Type (print(fontList)) if you wish to see all the available fonts.
    ComicSans = createFont("Comic Sans MS Bold", 100) #Setup to create the Comic Sans font
    MemeFont = createFont("Impact", 40) #This will be our variable for the font used in memes
    image(CurrentImage, 0, 0, 1920, 1080)
    textFont(ComicSans)
    textSize(100)
    text("Welcome to the meme machine", 200, 200)
    textSize(30)
    text("Left click somewhere to see/use the meme generator instructions", 800, 500)
    Doge1 = loadImage("Doge1.jpg") #These random files are the memes we will pull and is added onto respective lists
    Doge2 = loadImage("Doge2.jpg")
    Doge3 = loadImage("Doge3.jpg")
    Doge4 = loadImage("Doge4.png")
    MemeListDoge = [Doge1, Doge2, Doge3, Doge4] #This will be our list of available doge memes to draw upon randomly
    Cat1 = loadImage("Cat1.jpg")
    Cat2 = loadImage("Cat2.jpg")
    Cat3 = loadImage("Cat3.jpg")
    MemeListCat = [Cat1, Cat2, Cat3] #This will be our list of available Chemistry Cat memes to draw upon randomly
    Pooh1 = loadImage("Pooh1.jpg")
    Pooh2 = loadImage("Pooh2.jpg")
    Pooh3 = loadImage("Pooh3.jpg")
    Pooh4 = loadImage("Pooh4.jpg")
    MemeListPooh = [Pooh1, Pooh2, Pooh3, Pooh4] #This will be our list of available Winnie the Pooh memes to draw upon randomly
    IronicDoge1 = loadImage("IronicDoge1.png")
    IronicDoge2 = loadImage("IronicDoge2.png")
    IronicDoge3 = loadImage("IronicDoge3.jpg")
    IronicDoge4 = loadImage("IronicDoge4.jpg")
    IronicDoge5 = loadImage("IronicDoge5.jpg")
    IronicDoge6 = loadImage("IronicDoge6.jpg")
    IronicDoge7 = loadImage("IronicDoge7.jpg")
    IronicDoge8 = loadImage("IronicDoge8.png")
    IronicDoge9 = loadImage("IronicDoge9.jpg")
    IronicDoge10 = loadImage("IronicDoge10.png")
    MemeListIronicDoge = [IronicDoge1, IronicDoge2, IronicDoge3, IronicDoge4, IronicDoge5, IronicDoge6, IronicDoge7, IronicDoge8, IronicDoge9, IronicDoge10] #This will be our list of available Ironic Doge memes to draw upon randomly
    Pikachu1 = loadImage("Pikachu1.png")
    Pikachu2 = loadImage("Pikachu2.jpg")
    Pikachu3 = loadImage("Pikachu3.png")
    Pikachu4 = loadImage("Pikachu4.jpg")
    MemeListPikachu = [Pikachu1, Pikachu2, Pikachu3, Pikachu4] #This will be our list of available Surprised Pikachu memes to draw upon randomly
    Bob1 = loadImage("Bob1.jpg")
    Bob2 = loadImage("Bob2.jpg")
    Bob3 = loadImage("Bob3.jpg")
    Bob4 = loadImage("Bob4.jpg")
    Bob5 = loadImage("Bob5.jpg")
    Bob6 = loadImage("Bob6.jpg")
    Bob7 = loadImage("Bob7.jpg")
    Bob8 = loadImage("Bob8.jpg")
    Bob9 = loadImage("Bob9.jpg")
    Bob10 = loadImage("Bob10.jpg")
    MemeListBob = [Bob1, Bob2, Bob3, Bob4, Bob5, Bob6, Bob7, Bob8, Bob9, Bob10] #This will be our list of available Spongebob memes to draw upon randomly
    DogeTemplate = loadImage("DogeTemplate.jpg") #This is our non-text template for user inputted doge memes
    SpongeTemplate = loadImage("MockSpongeTemplate.jpg")
    BadLuckBrianTemplate = loadImage("BadLuckBrianTemplate.jpg")
    PoohTemplate = loadImage("PoohTemplate.png")
    SuccessKidTemplate = loadImage("SuccessKidTemplate.jpg")
    

def draw():
    global CurrentImage, img1, img2, tracker, Toptext, answer
    if mousePressed and (mouseButton == LEFT):
        CurrentImage = img2
        image(CurrentImage, 0, 0, 1920, 1080)
        fill(21, 82, 17)
        textSize(40)
        text("List of Commands", 300, 200)
        text("Input to generate a meme", 1300, 200)
        fill(245, 197, 66)
        text("Random Meme Generator", 800, 100) 
        textSize(30)
        fill(245, 66, 66)
        text("Doge", 300, 300) 
        text("Chemistry cat", 300, 400)
        text("Winnie the Pooh", 300, 500)
        text("Ironic Doge", 300, 600)
        text("Surprised Pikachu", 300, 700)
        text("Spongebob", 300, 800)
        text("Press 'D'", 1500, 300) #Instructs user that pressing a 'D' will pull a random doge meme
        text("Press 'C'", 1500, 400) #Instruction text for same thing, but for chemistry cat memes...
        text("Press 'P'", 1500, 500)
        text("Press 'I'", 1500, 600)
        text("Press 'S'", 1500, 700)
        text("Press 'B'", 1500, 800)
        fill(117, 66, 245)
        text("Meme Creator", 300, 900)
        text("Press right arrow key", 1500, 900)
         
def keyPressed(): #Allows us to set a new image whenever the specific key is pressed
    global CurrentImage, img1, img2, img3, Dogetracker, Cattracker, Poohtracker, Ironictracker, Pikachutracker, Bobtracker, MemeFont, MemeListDoge, MemeListCat, MemeListPooh, MemeListIronicDoge, MemeListPikachu, MemeListBob, DogeTemplate, Toptext, answer, answer2, BadLuckBrianTemplate, PoohTemplate, SpongeTemplate, SuccessKidTemplate
    if key == CODED:
        if keyCode == RIGHT:
            CurrentImage = img3 #The background for the user inputted memes
            image(CurrentImage, 0, 0, 1920, 1080)
            fill(48, 3, 252)
            textSize(40)
            text("List of Commands", 300, 200)
            text("Input to generate a meme", 1300, 200) 
            fill(255, 135, 197)
            text("Meme Creator", 850, 100)
            fill(198, 252, 3)
            textSize(30)
            text("Bad Luck Brian Template", 300, 300)
            text("Doge Template", 300, 400)
            text("Pooh Template", 300, 500)
            text("Mock Sponge Template", 300, 600)
            text("Success Kid Template", 300, 700)
            text("Press '1'", 1500, 300) #Instructs user that pressing 1 will allow user input for bad luck brian memes
            text("Press '2'", 1500, 400) #Same thing, but for doge memes now...
            text("Press '3'", 1500, 500)
            text("Press '4'", 1500, 600)
            text("Press '5'", 1500, 700)
    if key == '1':
        answer = input('What will be your toptext?')
        if len(answer) >= 24: #We want to set a character limit at 24 to avoid user input spam and bypassing meme borders, so we generate a new input dialogue box!
            answer = input('Top text too long: must be less than 24 characters')
        answer2 = input('What will be your bottomtext?')
        if len(answer2) >= 24: #Same for the bottom text
            answer2 = input('Bot text too long: must be less than 24 characters')
        image(BadLuckBrianTemplate, 750, 300, 500, 500) #This will serve as the image where the text will overlay onto
        fill(255, 255, 255)
        textFont(MemeFont)
        if len(answer) >= 14:
            text(answer.upper(), 760, 350) #If the meme is greater than 14 characters, place the text on the left to maximize space. We also make it all caps to homogenize discrepancies in text (and because this is typical meme format).
        else:
            text(answer.upper(), 910, 350) #Otherwise, we can afford to center the text
        if len(answer2) >= 14: 
            text(answer2.upper(), 760, 780) #Same thing done here for bottom text now
        else:
            text(answer2.upper(), 910, 780)
    if key == '2':
        answer = input('What will be your toptext?')
        if len(answer) >= 24:
            answer = input('Top text too long: must be less than 24 characters')
        answer2 = input('What will be your bottomtext?')
        if len(answer2) >= 24:
            answer2 = input('Bot text too long: must be less than 24 characters')
        image(DogeTemplate, 750, 300, 500, 500)  
        fill(255, 255, 255)
        textFont(MemeFont)
        if len(answer) >= 12:
            text(answer.upper(), 760, 350)
        else:
            text(answer.upper(), 910, 350)
        if len(answer2) >= 12:
            text(answer2.upper(), 760, 780)
        else:
            text(answer2.upper(), 910, 780)
    if key == '3':
        answer = input('What will be your toptext?')
        if len(answer) >= 24:
            answer = input('Top text too long: must be less than 24 characters')
        answer2 = input('What will be your bottomtext?')
        if len(answer2) >= 24:
            answer2 = input('Bot text too long: must be less than 24 characters')
        image(PoohTemplate, 750, 300, 500, 500) 
        fill(0, 0, 0)
        textFont(MemeFont)
        if len(answer) >= 14:
            text(answer[0:13].upper() + "-", 970, 350) #The pooh meme is different due to the white box borders, so if the text is greater than 14 characters, we wrap the text instead and add hyphenation!
            text(answer[13:].upper(), 970, 400) #The second half of the text is now placed lower than the first half!
        else:
            text(answer.upper(), 970, 350) #Otherwise, it is short enough to fill in the entire white box!
        if len(answer2) >= 14: #Now for bottom text...
            text(answer2[0:13].upper() + "-", 970, 600)
            text(answer2[13:].upper(), 970, 650)
        else:
            text(answer2.upper(), 970, 600)
    if key == '4':
        answer = input('What will be your toptext?')
        if len(answer) >= 24:
            answer = input('Top text too long: must be less than 24 characters')
        answer2 = input('What will be your bottomtext?')
        if len(answer2) >= 24:
            answer2 = input('Bot text too long: must be less than 24 characters')
        image(SpongeTemplate, 750, 300, 500, 500) 
        fill(255, 255, 255)
        textFont(MemeFont)
        if len(answer) >= 12:
            text(answer.upper(), 760, 350)
        else:
            text(answer.upper(), 910, 350)
        if len(answer2) >= 12:
            text(answer2.upper(), 760, 780)
        else:
            text(answer2.upper(), 910, 780)
    if key == '5':
        answer = input('What will be your toptext?')
        if len(answer) >= 24:
            answer = input('Top text too long: must be less than 24 characters')
        answer2 = input('What will be your bottomtext?')
        if len(answer2) >= 24:
            answer2 = input('Bot text too long: must be less than 24 characters')
        image(SuccessKidTemplate, 750, 300, 500, 500)
        fill(255, 255, 255)
        textFont(MemeFont)
        if len(answer) >= 12:
            text(answer.upper(), 760, 350)
        else:
            text(answer.upper(), 910, 350)
        if len(answer2) >= 12:
            text(answer2.upper(), 760, 780)
        else:
            text(answer2.upper(), 910, 780)
    if key == 'd':
        if Dogetracker >= 3:
            Dogetracker = -1 #We set it to -1 because right after we add by 1. We want to start counting from zero!
            random.shuffle(MemeListDoge) #We want to shuffle the meme list every time we empty it (static order != fun)
        Dogetracker = Dogetracker + 1 #We want a separate tracker for each meme otherwise swapping between memes completely ruins the meme ordering
        CurrentImage = MemeListDoge[Dogetracker] #Randomly generates the doge meme from the list of doge memes
        image(CurrentImage, 750, 300, 500, 500) #Positions the window for the meme
    if key == 'c':
        if Cattracker >= 2:
            Cattracker = -1
            random.shuffle(MemeListCat)
        Cattracker = Cattracker + 1
        CurrentImage = MemeListCat[Cattracker]
        image(CurrentImage, 750, 300, 500, 500)
    if key == 'p':
        if Poohtracker >= 3: #Once it reaches the last meme, it will reset the list and randomize it again
            Poohtracker = -1
            random.shuffle(MemeListPooh)
        Poohtracker = Poohtracker + 1
        CurrentImage = MemeListPooh[Poohtracker]
        image(CurrentImage, 750, 300, 500, 500)
    if key == 'i':
        if Ironictracker >= 9:
            Ironictracker = -1
            random.shuffle(MemeListIronicDoge)
        Ironictracker = Ironictracker + 1
        CurrentImage = MemeListIronicDoge[Ironictracker]
        image(CurrentImage, 750, 300, 500, 500)
    if key == 's':
        if Pikachutracker >= 3:
            Pikachutracker = -1
            random.shuffle(MemeListPikachu)
        Pikachutracker = Pikachutracker + 1
        CurrentImage = MemeListPikachu[Pikachutracker]
        image(CurrentImage, 750, 300, 500, 500)
    if key == 'b':
        if Bobtracker >= 9: #Once it reaches the last meme, it will reset the list and randomize it again
            Bobtracker = -1
            random.shuffle(MemeListBob)
        Bobtracker = Bobtracker + 1
        CurrentImage = MemeListBob[Bobtracker]
        image(CurrentImage, 750, 300, 500, 500)
    if key == 't':
        image(DogeTemplate, 750, 300, 500, 500)
        #if len(answer) > 10:
        fill(255, 255, 255)
        textFont(MemeFont)
        text(answer.upper(), 770, 350)
        text(answer2.upper(), 770, 780)

def input(message=''): #THIS IS THE FUNCTION TO CREATE THE DIALOGUE BOX FOR THE TOP TEXT. CHECK REFERENCES. villares. (2018, March). Processing 2.x and 3.x Forum. Retrieved December 1, 2019, from https://forum.processing.org/two/discussion/23646/how-to-use-input-with-python-processing-running-on-a-mac (lines 5-7).
    from javax.swing import JOptionPane #CHECK REFERENCES: villares. (2018, March). Processing 2.x and 3.x Forum. Retrieved December 1, 2019, from https://forum.processing.org/two/discussion/23646/how-to-use-input-with-python-processing-running-on-a-mac (lines 5-7).
    return JOptionPane.showInputDialog(frame, message) #CHECK REFERENCES: villares. (2018, March). Processing 2.x and 3.x Forum. Retrieved December 1, 2019, from https://forum.processing.org/two/discussion/23646/how-to-use-input-with-python-processing-running-on-a-mac (lines 5-7).
