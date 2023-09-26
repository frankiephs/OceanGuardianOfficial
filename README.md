# OceanGuardian Game
## About

Ocean Guardian is a game where you invented a robot fish to prevent/reduce ocean pollution. This game aims to give awareness about the effects of ocean pollution in an interactive and enjoying way.

### Objectives:
The Objectives is to collect a specific number of rubbish *(Displayed in game)* in a specific time limit *(Displayed in game.)*

### Controls:
Use the **W A S D** Controls.
## Screenshots

## Installation

**step 1:** Clone this repository

**Step 2:** Locate your directory using **cmd** or **powershell** or *any Python IDE*

**Step 3:** Install the requirements.

**Step 4:** Run the python file using **cmd** or **powershell** or any *Python IDE*

## Tips:
Collect the rubbish as soon as it respawns because the rubbish respawns as soon as the previous rubbish disappears. 


## Frequently Asked Questions
### "Why is it not an exe file?"

> *.exe* files or *executables* are compiled files, Any changes will need to be compiled again to make it up to date. In this process, This reduces flexibility for the developers and for the users. 
>
### **"why not just create a configuration file?"**
> Configuration files are limited to variables and cannot change things such as functions, etc.
>
### **"Why not just use a portable python distribution and still be able to configure the files afterwards since it have its own directory for modules?"**
> A portable python distribution is still a large size approximately 700 MB (Depending on the version) This will not be very flexible for low end devices and 700 MB is too big for just a simple game.

### "Why not just publish it in gaming marketplaces?"
> We can publish it to gaming marketplaces like itch.io, etc. However, Just like the exe file, It is compiled, reduces flexibility and gaming marketplaces are not available in the school network. This requires an additional library called pygbag including asyncio. Pygbag games tend to be in low performance based on my experience.

### "Why not just embed it in web hosting platforms?"
> Web hosting platforms costs money, and again, flexibility.

### "Why not just self host it with your own server"
> Servers online costs money, flexibility, maintenance and additional hardwares.

### "Why is it 'not responding' in some areas even it is actually responding?"
> In the code, We use the "time.sleep(n)" method from the time library. This delays a particular code. When the software is pausing, Your PC thinks your PC is not responding so when you try to click the screen during those delays. The 'not responding' dialogue will pop up.

### "Why can't I press the 'x' or exit button?"
>In pygame, to exit the game, You will need to call the *'pygame.quit' and 'sys.exit'*, When in a delay method (refering to the previous question), the software stops or the file stops therefore it cannot call the quit method. "Then why on other areas are working?" Other areas use the tick difference to make a timer, this is quite complex and requires a longer code.  We are planning to remove the delay by proceeding with the "click to continue" system but that will consume another time.



## Credits:
- **Programmers and Debuggers**
	- Manling He
	- Frankie Bula
	- Chien Nguyen
- **Artworks Credits** 
	- Main Game background - designed by Manling He
	- Rubbish Sprites - designed by Manling He
	- Robot Fish Sprites - designed by Manling He
- **Sound Credits**
	- OceanGuardian "Game On" - Composed by Frankie Bula
	- Old Guy Naration - Developed in Eleven Labs


## Found a bug?
Please create an issue.
