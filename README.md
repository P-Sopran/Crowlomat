# Crowlomat

this piece of software controls two stepper motors connected to a raspberry pie via a UI built with PySimpleGUI. The pie is then placed on a high shelf and two cups (one green, one white) are attached to the motors. These cups are filled with dry cat food. When the motor makes a 360 degree turn, the cat food falls out and my cat is very happy. 

The UI is in Swiss-German, as its users are based in Switzerland. It offers three possible ways to control to stepper:
1) turn both cups every 24 hours
2) set a date and time for each cup individually to turn
3) turn each cup when a button is pushed. 

The motor class handles how the motor turns and the layout file contains the UI as well as the logic
