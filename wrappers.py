# FICS requires all information be sent in this format:
# <12> rnbqkb-r pppppppp -----n-- -------- ----P--- -------- PPPPKPPP RNBQ-BNRB -1 0 0 1 1 0 7 Newton Einstein 1 2 12 39 39 119 122 2 K/e1-e2 (0:06) Ke2 0 

import os
import sys
import multiprocess
import time
import ctimer   # ctimer.C module



positions = [pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8]  # each position is a string of dashes and upper or lowercase characters

class constrng()  #i don't think  need to initialize all of these, but i forgot how to code
	def __init__(self, number, positions, color, push, ws, wl, bs, bl, drawnum, gamenum, wname, bname, relation, stime, ctime, wpt, bpt, srt, brt, move, coords, turn_time, notes, flip):
		
	def number:
		#increase turn number every two turns
		
		 
	def timer:
		#get timer functions from timer.c for most of the time fucntions (and there are a few)
		
	def positions:
		#read the last move and change array values accordingly ?
		# this is what they look like at the begining of turn 1
		pos1 = [R,K,B,K,Q,B,K,N]
		pos2 = [P,P,P,P,P,P,P,P]
		pos3 = [-,-,-,-,-,-,-,-]
		pos4 = [-,-,-,-,-,-,-,-]
		pos5 = [-,-,-,-,-,-,-,-]
		pos6 = [-,-,-,-,-,-,-,-]		
		pos7 = [p,p,p,p,p,p,p,p]
		pos8 = [r,k,b,q,k,b,k,r]

