# CA_MIDI
[中文](https://github.com/FuryL/CA_MIDI/blob/main/README.md)      
        
Use the cellular automata of **Game of Life** to generate MIDI music files         
                
The .EXE file is in the dist folder     
    
Mainly implemented using Pygame and Mido
                
The window consists of 64*64 small grids, white is "dead" and black is "live"
    
This code only did the judge sentences of the acoustic grand piano which instrument number is 0 in MIDI
  
## operate
Left-click on a white grid to turn it to black, it means "live"; hold down the left button and drag it to make an area black; right-click on the black grid to turn it into white
        
After defining the initial pattern, click the space to start evolution, and click again to pause
    
Q key displays the row and col number
    
M key outputs the current pattern as a MIDI file
    



## MIDI file generation rules
This code part adopts Mido default settings: GPM defaults to 120; instrument defaults to 0, which means acoustic grand piano. If you need to change, please refer to the Mido document
  
Because MIDI has a pitch of 128, the screen is divided into upper and lower parts to generate MIDI
  
**the upper half**  
  
The upper 32 rows represent the time when the note appears, the 0th row is 0-480ms, and the 1st row is 480ms-960ms
    
The upper 64 columns represent the note, the 0th column is the 0 note of the MIDI file, and the 63rd column is the 63 note
    
**the lower half**  
  
The lower 32 rows represent the time when the notes appear, which is consistent with the upper 32 rows. The 32nd row is 0-480ms, and the 33rd row is 480ms-960ms.
    
The lower 64 column represents the note, the 64th column is the 64 note of the MIDI file, and the 127th column is the 127 note
    
    
#### Because I have never studied music, this project is just my idea of random (but not completely random) generating music, for reference only
