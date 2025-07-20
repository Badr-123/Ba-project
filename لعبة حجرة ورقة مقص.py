import random
import time
import sys
print("""
                     //////////
                     Made with  
                        BR
                   //////////\n \n
""")
time.sleep(1)
print("""
 --------------------------    
| is loading....           |
 --------------------------
""")
time.sleep(2)
print("Welcome to our game:\n")
#us_ch
us_ch=input("Choose cut, paper, rock:\n").lower()
#co_chs
paper="""
_______
---    ____|____
           ______|
          _______|
         _______|
---.__________|"""
cut ="""
_______
---   ____|____
          ______|
       __________|
      |____|
---.__|___|"""
rock ="""
_______
---    ____|
      |_____|
      |_____|
      |____|
---._|___|"""
#cm_ch
cm_chs=["rock","cut","paper"]
cm_ch=random.choice(cm_chs)
#if user
if us_ch == "rock":
	print("You choosed Rock "+ rock)
elif us_ch == "cut":
	print("You choosed Cut " + cut)
elif us_ch == "paper":
	print("You choosed Paper " + paper)
else:
	print("Please try again")
	sys.exit()
#if co
if cm_ch == "rock":
	print ("\nComputer is thinking....\n")
	time.sleep(2)
	print(f"Computer choosed Rock {rock}")
elif cm_ch == "paper":
	print ("\nComputer is thinking....\n")
	time.sleep(2)	
	print(f"Computer choosed Paper {paper}")
else:
	print ("\nComputer is thinking....\n")
	time.sleep(2)	
	print(f"Computer choosed Cut {cut}")
#if win
if us_ch == "rock" and cm_ch == "cut":
	print("\nCongratulations! you won🎉🎊")
elif us_ch == "paper" and cm_ch == "rock":
	print("\nCongratulations! you won🎉🎊")
elif us_ch == "cut" and cm_ch == "paper":
	print("\nCongratulations! you won🎉🎊")
elif us_ch == cm_ch:
	print("\nOh! that's draw😄")
else:
	print("\nYou lost😞, Please try again")