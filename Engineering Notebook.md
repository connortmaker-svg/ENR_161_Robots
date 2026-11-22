# Engineering Notebook for ENR 161

This is the engineering notebook that will house all the ideas, thoughts, and planning for the ENR 161 Robotics Competition. 

**ENR 161 Team:**

| Name | Email |
| --- | --- |
| Connor Klute | cklute@student.monroecc.edu |
| Jalaluddin | Jmohammadi1@student.monroecc.edu | 

# Table of Contents

| Section | Topic |
| --- | --- |
| 1.0 | Week 1 |
| 2.0 | Week 2 |
| 3.0 | Week 3 |
| 4.0 | Week 4 |
| 5.0 | Competition |

# 1.0 | Initial Prompt

`To design and build an autonomous robot that can successfully make hockey goals with five pucks
(painted wooden dowels) laid down on a track while a goalie (3D printed panel operated by a motor)
intermittently blocks the goal. The pucks must be delivered to the appropriate opposing team goal. The
robots will have a maximum time of 150 seconds in each of the two allotted trials. The robot must begin
completely within the center circle but may expand to any size during the trial.`

| Restrictions |
| --- | 
| You must use the mBot2 |
| You must use Python as the programming language. |
| The goalies will expose the goal for ~3 seconds and obstruct the goal for ~2seconds in an endless loop |
| You are allowed to request additional Lego components on request |
| You can add your own non-Lego components as long as they total less than $15 |
| 3D printing is allowed. If you don’t have your own 3D printer, some student clubs allow some amount of free printing (e.g., Engineering Leadership Council in 03-132). |
| Scoring is defined as the appropriate color passing completely through the goal or preventing the goalie door from closing |

<!-- -This is the photo of the course taken from the Competition Rule Book- -->
![Figure 1](<Photos for Notebook/Figure 1.png>)


# 1.1 | Inital Plans (Week 1)

The intial plan that was drawn up that our team wanted to accomplish the full spectrum of the game. 

- Scoring all 5 pucks in there designated holes

- Fully utilize a PID algorithm with all three variables, as the provided code only utilized the P term

- Hoping to Complete the entire game within a 30 to 45 second time frame. 

# 1.1 | Code

The current codebase is setup as a github repository that this Markdown file exsists in. The folders show as follows:

| Folder | Item | 
| --- | --- |
| Assignments | This is where all of the different assignments and reports that go over specific items for the Robot are located |
| Competition Code | The final resting spot for all the different code that will be used in the competition |
| Test Files | This is the main working folder as I test out different ideas and execute them, the most changes in code will be here |
| Main Folder | The Engineering Notebook and Final Report will be housed | 

# 1.2 | Reflection Questions

1: How many points are you planning on scoring? What is the plan for how to robot will navigate the board and score points? What are the subtaks (smaller actionable tasks) that need to be accomplished?

Answer(s): 
- Currnently I am planning on maximum points; which breaks down to 4 points for the black puck, 12 points for the red and blue pucks, and potentionally a few addtional points.

- Currently my plan for having the robot navigate is to utilize my line following function within the repository for maximum speed between the two goals.

- The current subtasks are; line following, puck manipulation, scoring, and pathing. 

2: What subtake have you benn working on this week and how is that going?

Answer(s):
- I have been working on the line following subtask and planning the pathing. The line following has been nearly fully tuned, there is a bit of wobble in the corners, but it is still driving around the corners in the line. 

3: What are some norms that your team has agreed on (e.g., when will you meet outside of class? How will you make sure one person is not doing all the work?)

Answer(s):
- Currently We have seperated the tasks; I am focusing on the Line following and the main pathing algorithim for the robot. And my parnter is working on the puck manipulation and potential scoring.

- We are working on the two main aspects in paraell and hopefully once we come back after break we work through combining the two processes together. 

4: What are the goals for the upcoming week and what needs to be done to meet those goals?

Answer(s):
- Over the Thanksgiving break I plan to fully flush out the pathing algorithm and plan for how the game will be played. Which will just require time to be put into the project. 

# 1.3 | Personal Time Spent on Project for Week 1 

This is all the time spent on the project by myself (Connor). Inside this github repository will be everything recorded that is created for the ENR 161 Robotic section. 

| Date | Hours Spent | What was done | 
| --- | --- | --- |
| 10/28 | 2 to 3 | Created the main Line following program that will be utilized in the Competition |
| 10/29 | ~20 minutes | Edited the dt function in the line following to attempt to fix the wobble in the movement |
| 11/17 | 3 total | Attempted to create differential turning with the line following for more optimized line following, currently unsuccesful. |
| 11/17 | ~1 | Spent time tuning the PID values within the line following code to get a much smoother line out of the robot, currently semi-successful; Also created a quick inital test on throwing the black puck into the goal through brute force, that was massivly unsuccesful. |
| 11/18 | ~1 | Created the intial document of the Engineering Notebook to fully fill out later. | 
| 11/19 | ~2 | Fully flushed out the Engineering Notebook for Week 1 | 
