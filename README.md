# OceanGuardian Game
## About

Ocean Guardian is a game where you invented a robot fish to prevent/reduce ocean pollution. This game aims to give awareness about the effects of ocean pollution in an interactive and enjoying way.

### Objectives:
The Objectives is to collect a specific number of rubbish *(Displayed in game)* in a specific time limit *(Displayed in game.)*

### Controls:
Use the **W A S D** Controls.
## Screenshots

## Requirements:
> **Python 3.2 or above**

>  **Required Libraries list:** 
>  *(Check out how to install the libraries in "Installation in windows step 2".)*
>  - pygame
>  - random
>  - sys
>  - Time

## Installation in windows


### Step 1: Clone this repository
Method 1: Using the git clone in the *cmd* or *powershell*
Method 2: Using the github Desktop
Method 3: Downloading the zip file

### Step 2:** Install the required libraries
Method 1: Manual download
Method 2: Using *cmd* or *powershell*

### Step 3: Run the file
Method 1: Using *cmd** or **powershell*
Method 2: Manually executing it in your IDE

## Installation in replit

## Game Tips:
Collect the rubbish as soon as it respawns because the rubbish respawns as soon as the previous rubbish disappears. 


## Frequently Asked Questions

### "Why can't I install requirements.txt or libraries using pip in cmd? Any solutions?"
> If using a school device, Installation or configuration of the device or hardware are prohibited. Use **Windows powershell** instead or use your **own personal computer**.
> Still cannot run? Use **replit** as an alternative.

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

### "It says pygame.mixer.init() error?"
> regarding to the `pygame.mixer.init()` error, This is because replit is a browser based IDE and the `pygame.mixer.init()` finds an audio device which is typically refering to the hardware. To solve this issue, you will need to use the "pygame" language instead of the "python" language. In this case, it now supports sounds from pygame.
> 
### "Why is the performance slower in replit?"
> Replit have its own GPU, RAM and storage because it is virtual environment that uses docker containers. These GPU, RAM, etc. have its own limitations and might require to upgrade your own account if you want a faster one. Pygame also runs fast frames therefore it requires a hardware that is fast too.

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
