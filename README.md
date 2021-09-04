# CA_MIDI 
使用**生命游戏规则**的元胞自动机生成MIDI音乐文件  
打包后的EXE文件在dist文件夹中
    
主要使用Pygame与Mido实现 
界面由64*64个小格子组成，白色为“死”，黑色为“生”
    
本代码只做了0号乐器大钢琴的音高判定  
  
## 操作
鼠标左键单击一个白色格子使其变为黑色则定义其为“生”；按住左键不放拖拽可使一片区域变为黑色；右键点击黑色格子可将其变为白色，即为“死” 
        
定义初始图案后点击空格键开始演化，再次点击暂停  
    
Q键显示行列序号  
    
M键输出当前图案为MIDI文件     
    



## MIDI文件生成规则   
本代码部分采用Mido默认设置：GPM默认为120；乐器默认是0，即大钢琴。如有更改需求请查阅Mido文档   
  
因为MIDI有128音高，所以将画面分为上下两部分进行生成   
  
**上半部分**  
  
上方32行代表音符出现的时间，第0行为0-480ms,第1行即为480ms-960ms 
    
上方64列代表音符音高(note)，第0列为MIDI文件的0音高，第63列为63音高  
    
**下半部分**  
  
下方32行代表音符出现的时间，与上方32行一致，第32行为0-480ms,第33行即为480ms-960ms
    
下方64列代表音符音高(note)，第64列为MIDI文件的64音高，第127列为127音高  
      

#### 因本人未进行过音乐学习，此项目仅是我一个随机（但不完全随机）生成音乐的想法，仅供参考  





# CA_MIDI
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
