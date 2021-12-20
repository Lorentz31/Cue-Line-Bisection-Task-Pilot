'''
cd Desktop
python Cue_Line_Bisection_Task_Pilot.1.1.py
'''

# Importing many important modules
import os
from datetime import datetime
from psychopy import logging, visual, core, event, clock, gui
import numpy as np
from random import randint, sample, random
import pandas as pd

# Clear the command output / set the logging to critical
os.system('cls' if os.name == 'nt' else 'clear')
logging.console.setLevel(logging.CRITICAL)
print('************************************************')
print('"CUE" LINE BISECTION TASK: PILOT STUDY: version alpha')
print('************************************************')
print(datetime.now())
print('************************************************')

# Create lenght loop / no_trials
no_trials = 15 # This is the number of times that each length (5 lengths) is displayed three times for each cue position (5 x 3 = 15)
line_length_array = [] # Set of different line lengths. To append later
cue_pos_array = [] # Set of different cue position. To append later

for l in range(0, no_trials): # Previous explanation: 5 x 3 = 15
    for n in range(0, 3): # Number of cue position (= 3)
        if l < 3: # Create equally-spaced distribution for all lengths (= 3 each)
            line_length_array.append(642) # Measures are in pixels
        if l >= 3 and l < 6:
            line_length_array.append(128)
        if l >= 6 and l < 9:
            line_length_array.append(224)
        if l >= 9 and l < 12:
            line_length_array.append(322)
        if l >= 12 and l < 15:
            line_length_array.append(48)
        if n == 0:
            cue_pos_array.append(-1) # Measures are just indexes to use later on
        if n == 1:
            cue_pos_array.append(0)
        if n == 2:
            cue_pos_array.append(1)

condition = pd.DataFrame({'Length': line_length_array, 'Cue': cue_pos_array}) # Create a pandas dataframe
condition_random = condition.sample(frac=1) # Randomize trials (for each (5) length there are cue position (3), everything repeated two times (5 x 3 x 3 = 45))
condition_random = np.array(condition_random) # Re-convert in numpy array for further elaboration

# Define variables to declare
trial_no_array = [] # Number of total trials
sub_id_array = [] # To append later
date_value_array = [] # To append later
date_val = datetime.now().strftime('%d%m%Y')
time_value_array = [] # To append later
length_divided_for_pos_array = []
final_line_length_array = [] # The real sequence of lengths used by the loop. To append later
final_cue_pos_array = [] # The real sequence of cue position used by the loop. To append later
response_latency = [] # To append later

# Setup our experiment
myDlg = gui.Dlg(title = '"Cue Line Bisection Task: Pilot Study (version alpha)') # The dialog window poping when experiment opens
myDlg.addText('Subject Info')
myDlg.addField('Exp Date', date_val)
myDlg.addField('Number:')
myDlg.addField('Sex:', choices = ['Male', 'Female', 'Prefer not to say'])
myDlg.addField('Age:')
show_dlg = myDlg.show()

if myDlg.OK:
    print(show_dlg)
    save_file_name = show_dlg[0] + '_' + show_dlg[1] + '_cue_line_bisection_task.csv'
    print(save_file_name)

else:
    print('User cancelled')

# Create a save filepath (GUI)
save_path = gui.fileSaveDlg(initFileName = save_file_name, prompt = 'Select Save File')
print('Output form save dialog')
print(save_path)

if save_path == None:
    print('Experiment must be saved first')
    core.quit()

# Create window
win0 = visual.Window(size=(1920,1080),
                    color=(0,0,0),
                    fullscr=True,
                    monitor='testMonitor',
                    screen=1,
                    allowGUI=True,
                    pos=(0,0),
                    units='pix')

# Create fixation cross
def fixation_cross():
    fix_cross_horiz = visual.Rect(win0,
                                  width = 15,
                                  height = 1.5,
                                  units = 'pix',
                                  lineColor = [-1,-1,-1],
                                  fillColor = [-1,-1,-1],
                                  pos = (0,0))
    fix_cross_vert = visual.Rect(win0,
                                 width = 1.5,
                                 height = 15,
                                 units = 'pix',
                                 lineColor = [-1,-1,-1],
                                 fillColor = [-1,-1,-1],
                                 pos = (0,0))
    fix_cross_horiz.draw() #This will draw the line onto the window
    fix_cross_vert.draw() #This will draw the line onto the window

# Create the line stimulus
def line(line_length): # Define the horizontal line where its lenght will change alongside the loop iteration number
    hor_line = visual.Rect(win0,
                       width = line_length,
                       height = 1,
                       units = 'pix',
                       lineColor = [-1,-1,-1],
                       fillColor = [-1,-1,-1],
                       pos = (0,0))
    hor_line.draw()

# Create the cue
def cue(cue_pos):
    cue_dash = visual.Rect(win0,
                         width = 1,
                         height = 4,
                         units = 'pix',
                         lineColor = [1,1,1],
                         fillColor = [1,1,1],
                         pos = (cue_pos,3))
    cue_dash.draw()

# Create the slider
def slider(newpos):
    dash = visual.Rect(win0,
                     width = 1,
                     height = 7,
                     units = 'pix',
                     lineWidth = 0.5,
                     lineColor = [-1,-1,-1],
                     fillColor = [-1,-1,-1],
                     pos = newpos)

    dash.draw()

mymouse = event.Mouse(visible = False, win = win0) # Don't need mouse during this experiment

# Wait for subjects to press enter (when they're ready)
text_info = visual.TextStim(win0,
                         text = 'PRESS ENTER TO START',
                         pos = (0,0),
                         color = (-1,-1,-1),
                         units = 'pix',
                         height = 32)
text_info.draw()
win0.flip()
key = event.waitKeys(maxWait = 9999, keyList = ('return', 'q'), clearEvents = True)

if 'return' in key:
    win0.flip()
    core.wait(1)
    pass # Go on in the code

if 'q' in key: # Exit whenever you want
    win0.close()
    core.quit()
    print('OK, program and window closed.')

# Update the subject on what task to do (training)
text_info_block = visual.TextStim(win0,
                               text = 'This is the Training Block',
                               pos = (0, 100),
                               color = (-1,-1,-1),
                               units = 'pix',
                               height = 32)
text_info = visual.TextStim(win0,
                         text = 'Press Space Key in Correspondence of the White Cue',
                         pos = (0,0),
                         color = (-1,-1,-1),
                         units = 'pix',
                         height = 32)
text_info_start = visual.TextStim(win0,
                               text = 'Press Enter to Start',
                               pos = (0,-100),
                               color = (-1,-1,-1),
                               units = 'pix',
                               height = 32)
text_info_block.draw()
text_info.draw()
text_info_start.draw()
win0.flip()

keys = event.waitKeys(maxWait = 9999, keyList = ['return','q'], clearEvents = True)

if 'return' in key:
    win0.flip()
    core.wait(1)
    pass # Go on in the code

if 'q' in keys:
    win0.close()
    core.quit()

# Training loop
for i in range(0, 5):

    line_length_array_tra = [128,642,224,322,48] # Just example
    cue_pos_array_tra = [-1,0,-1,1,1] # Just example

    if cue_pos_array_tra[i] == -1: # It indicates a left cue located approximately at 2/3 of total length
        cue_pos = ((-(line_length_array_tra[i])/2)*0.66)
    if cue_pos_array_tra[i] == 0: # It indicates a cue located at the midpoint
        cue_pos = (0)
    if cue_pos_array_tra[i] == 1: # It indicates a right cue located approximately at 2/3 of total length
        cue_pos = (((line_length_array_tra[i])/2)*0.66)

    fixation_cross()
    win0.flip()
    core.wait(0.8)

    length_divided = (line_length_array_tra[i])/2 # Define the two halves
    length_divided_for_pos = length_divided # DO NOT MODIFY: NECESSARY FOR LOOPING WELL

    while True: # DO NOT MODIFY: NECESSARY FOR LOOPING WELL

        event.clearEvents()

        line(line_length_array_tra[i])
        line.autoDraw = True

        cue(cue_pos)
        cue.autoDraw = True

        start_pos = (-length_divided_for_pos, 0) # Slider starts from the left end
        slider(start_pos)
        slider.autoDraw = True
        win0.flip()

        core.wait(0.005)
        if (line_length_array_tra[i]) == 322 or (line_length_array_tra[i]) == 642: # For these long length, the increment is set at 3 pixels, otherwise it is 1
            length_divided_for_pos = length_divided_for_pos - 3
        else:
            length_divided_for_pos = length_divided_for_pos - 1

        if start_pos[0] >= length_divided: # When the slider reaches the right end, it "refresh" and starts again and over again if 'space' is not pressed
            length_divided_for_pos = (line_length_array_tra[i])/2 # DO NOT MODIFY: NECESSARY FOR LOOPING WELL

        keys = event.getKeys(keyList = ['space','q'])

        if 'q' in keys:
            win0.close()
            core.quit()

        if 'space' in keys:
            break_flag = 1
            break

# Update the subject on what task to do (test)
text_info_block = visual.TextStim(win0,
                               text = 'This is the Test Block',
                               pos = (0, 100),
                               color = (-1,-1,-1),
                               units = 'pix',
                               height = 32)
text_info = visual.TextStim(win0,
                         text = 'Press Space Key in Correspondence of the White Cue',
                         pos = (0,0),
                         color = (-1,-1,-1),
                         units = 'pix',
                         height = 32)
text_info_start = visual.TextStim(win0,
                               text = 'Press Enter to Start',
                               pos = (0,-100),
                               color = (-1,-1,-1),
                               units = 'pix',
                               height = 32)
text_info_block.draw()
text_info.draw()
text_info_start.draw()
win0.flip()

keys = event.waitKeys(maxWait = 9999, keyList = ['return','q'], clearEvents = True)

if 'return' in key:
    win0.flip()
    core.wait(1)
    pass # Go on in the code

if 'q' in keys:
    win0.close()
    core.quit()

# Main loop
for i in range(0, len(line_length_array)):

    if condition_random[i][1] == -1:
        cue_pos = ((-(condition_random[i][0])/2)*0.66)
    if condition_random[i][1] == 0:
        cue_pos = (0)
    if condition_random[i][1] == 1:
        cue_pos = (((condition_random[i][0])/2)*0.66)

    trial_no_array.append(i)
    sub_id_array.append(show_dlg[1])
    date_value_array.append(date_val)
    time_value_array.append(datetime.now().strftime('%H%M%S'))
    final_line_length_array.append(condition_random[i][0])
    final_cue_pos_array.append(condition_random[i][1])

    fixation_cross()
    win0.flip()
    core.wait(1)

    length_divided = (condition_random[i][0])/2 # Define the two halves
    length_divided_for_pos = length_divided # DO NOT MODIFY: NECESSARY FOR LOOPING WELL

    while True: # DO NOT MODIFY: NECESSARY FOR LOOPING WELL

        event.clearEvents()

        line(condition_random[i][0])
        line.autoDraw = True

        cue(cue_pos)
        cue.autoDraw = True

        start_pos = (-length_divided_for_pos, 0)
        slider(start_pos)
        slider.autoDraw = True
        win0.flip()
        start_time = clock.getTime() # Starting our timer

        core.wait(0.005)

        if (condition_random[i][0]) == 322 or (condition_random[i][0]) == 642:
            length_divided_for_pos = length_divided_for_pos - 3
        else:
            length_divided_for_pos = length_divided_for_pos - 1

        if start_pos[0] >= length_divided:
            length_divided_for_pos = (condition_random[i][0])/2 # DO NOT MODIFY: NECESSARY FOR LOOPING WELL

        keys = event.getKeys(keyList = ['space','q'])

        if 'q' in keys:
            win0.close()
            core.quit()

        if 'space' in keys:
            length_divided_for_pos_array.append(-length_divided_for_pos) # Coordinates at which subjects respond
            stop_timer = clock.getTime()
            break_flag = 1
            delta_time = ('%.4f' %((stop_timer - start_time)*1000)) # Rounded to four digits. Converted in milliseconds
            response_latency.append(delta_time)
            break

# Create our output table in pandas
output_file = pd.DataFrame({'Trial_No':trial_no_array,
                            'SubID':sub_id_array,
                            'Date':date_value_array,
                            'Time':time_value_array,
                            'Line_Length':final_line_length_array,
                            'Sub_response':length_divided_for_pos_array,
                            'Cue_Position': final_cue_pos_array,
                            'Latency_ms':response_latency})

output_file.to_csv(save_file_name, sep = ',', index = False)

win0.close()
print('OK, program and window closed.')
