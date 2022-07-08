# -*- coding: utf-8 -*-
"""RL

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/14EperKOvRltJHHvdRGipzweEzzoTLe2l
"""

import random

#create Environment class
class MyEnvironment:

  def __init__(self):
    #maximum number of steps which the agent can take to gain rewards
    self.remaining_steps=20 #assume that the game must be completed within 20 steps

  def get_observation(self):
    #it can be any number of coordinates.Its considered as 3 here.
    #These values -0.0,0.0,0.0 represent some kind of logic that gives info about the environment.These values can be anything.
    return [1.0,2.0,1.0]  
  
  #when agent,performs an action,it should get a reward
  #i have set it as 1 for reward,-1 for punishment
  def get_actions(self):
    return [-1,1]

  #if steps are completed,return True because the agent should not move anymore
  def check_is_done(self)->bool:
    return self.remaining_steps==0

  def action(self,int):
    if self.check_is_done():
      raise Exception("Game over")      
    self.remaining_steps-=1  #if steps can still be taken-game not finished=>decrement the remaining number of steps
    return random.random()  #here-as this is a simple implementation-just returning a random number



#agent implements some policy

class myAgent:
  def __init__(self):
    self.total_rewards=0.0 #initially-agent-no rewards

  def step(self,ob:MyEnvironment):
    curr_obs=ob.get_observation()
    print(curr_obs)
    curr_action=ob.get_actions()
    print(curr_action)
    curr_reward=ob.action(random.choice(curr_action)) 
    #here,we are randomly picking -1 or 1
    #usually,when action() is invoked,implementation to check if the decision of the agent is crt-give positive reward else negative reward
    self.total_rewards+=curr_reward
    print("Total rewards so far= %.3f "%self.total_rewards)

if __name__=='__main__':
  obj=MyEnvironment()
  agent=myAgent()
  step_number=0

  while not obj.check_is_done():
    step_number+=1
    agent.step(obj)
    

  print("Total reward is %.3f "%agent.total_rewards)
  #different o/p everytime we run this code b'coz diff random numbers will be generated