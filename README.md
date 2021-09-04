# CA_MIDI 
[English](https://github.com/FuryL/CA_MIDI/blob/main/README_ENG.md)
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
