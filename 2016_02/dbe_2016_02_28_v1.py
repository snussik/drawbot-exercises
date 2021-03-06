#  Eli Heuer's daily DrawBot exercise!
#  eliheuer@gmail.com
#  02/29/16 -- version 1
#  Made with DrawBot:
#  http://www.drawbot.com/ 

# pep-8 maximum-line-length #/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#/#

# setting up the main variables
canvas      = 512  # size of the gif in pixels
margin      = 128  # grids distance from edge of canvas 
increment   =  16  # grid increment
num_frames  =  17  # number of frames in the animation
step        =  -1   # steps in looping animation
circle_size =  14  # self explanatory

# grid increments (16px X 16pc)
gridarray_reg = range(margin, (canvas - margin) + increment, increment) 
gridarray_rev = gridarray_reg[::-1]
print gridarray_reg
print gridarray_rev


# draw the canvas
for frame in range(num_frames):
  newPage(canvas, canvas)
  step = step + 1
  frameDuration(1/20)
  fill(0.8)
  rect(0, 0, canvas, canvas)
  
  # draw the grid
  fill(None)
  stroke(0.5)
  strokeWidth(1)
  lineCap("round")
  lineJoin("round")
  
  # grid X-axis
  stepx  = -16  # step in sequence on x axis             
  for x in range(17):
    save()
    stepx = stepx + increment
    polygon((margin + stepx, margin), (margin+stepx, canvas-margin))
    restore()
    
  # grid Y-axis
  stepy  = -16  # step in sequence on y axis 
  for y in range(17):
    save()
    stepy = stepy + increment
    polygon((margin, margin + stepy), (canvas-margin, margin+stepy))
    restore()
    
  # guides
  stroke(0.4)  
  strokeWidth(0.5)
  polygon((0, 128), (512, 128))
  polygon((0, 128+256), (512, 128+256))
  polygon((128, 0), (128, 512))
  polygon((128+256, 0), (128+256, 512))
  polygon((256, 0), (256, 512))
  polygon((0, 256), (512, 256))

  # animation loop
  for frame in range(num_frames):
    print frame
    save()
    fill(1)
    strokeWidth(1.5)
    stroke(0.4)
    
    # moving circles
    w
    
    
    
    restore()
    
    
    
    
    
    
    
    
    #oval = 
    #position = starting positon
    #while position <= 18
    #for oval in ovals:
        #position = position =+1
    #else reverse
    oval((gridarray_reg[step])-(circle_size/2), (gridarray_reg[0])-(circle_size/2), 
    circle_size, circle_size)
    
    oval((gridarray_reg[step])-(circle_size/2), (gridarray_reg[2])-(circle_size/2), 
    circle_size, circle_size)
    
    oval((gridarray_reg[step])-(circle_size/2), (gridarray_reg[4])-(circle_size/2), 
    circle_size, circle_size)
    
    oval((gridarray_reg[step])-(circle_size/2), (gridarray_reg[6])-(circle_size/2), 
    circle_size, circle_size)
    
    oval((gridarray_reg[step])-(circle_size/2), (gridarray_reg[8])-(circle_size/2), 
    circle_size, circle_size)
    
    oval((gridarray_reg[step])-(circle_size/2), (gridarray_reg[10])-(circle_size/2), 
    circle_size, circle_size)
    
    oval((gridarray_reg[step])-(circle_size/2), (gridarray_reg[12])-(circle_size/2), 
    circle_size, circle_size)
    
    oval((gridarray_reg[step])-(circle_size/2), (gridarray_reg[14])-(circle_size/2), 
    circle_size, circle_size)
    
    oval((gridarray_rev[step])-(circle_size/2), (gridarray_reg[16])-(circle_size/2), 
    circle_size, circle_size)
    
    restore()
      
saveImage("dbe_2016_02_29_v1.gif")