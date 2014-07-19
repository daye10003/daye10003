#-*- coding:utf-8 -*-

import random 
import os 
attempt=0
running = True
lst=[]
print "숫자 야구를 시작합니다!"
lst.append("숫자 야구를 시작합니다!")
while running:
	playing = True
	while playing:
		playing = True
		guessing = True
		computer=random.sample(range(0,10),4)
		computer = ''.join(str(i) for i in computer)
		print computer
		lst.append("computer: %s" %(computer))
		attempt = 0
		while guessing:
			player= raw_input("서로 다른 숫자로 이루어진 네자리 숫자를 입력하세요: ")
			B=0
			S=0
			while not player.isdigit() or len(player) != 4 or len(player) !=len(set(player)):
				print "잘못 입력하셨습니다."
				break
			else:
				lst.append("player: %s" %(player))
				while playing:
					attempt +=1
					for i in range(0,4):
						if player[i] in computer:
							if player[i]==computer[i]:
								S+=1
							else:
								B+=1
					if S!=4:
						lst.append("%sB %xS" %(B, S))
						print "%s번째 시도의 %sB, %sS 입니다." %(attempt, B, S)
						break
					elif S==4:
						print "%s번째 시도에서 홈런!"%(attempt)
						guessing= False
						break
		ask= True
		while ask:
			again = raw_input("다시 하시겠습니까? 예/아니오: ")
			if again != "예" and again != "아니오":
				print "잘못 입력하셨습니다. 예 또는 아니오를 입력하세요."
			else:
				if again=="예":
					ask= False
				else:
					ask=False
					playing= False
					break
	lst.append("숫자 야구를 마칩니다.")		 
	save = raw_input("저장하시겠습니까? 예/아니오: ")
	if save  !="예" and save !="아니오":
		print "잘못 입력하셨습니다. 예 또는 아니오를 입력하세요."
	elif save=="예":
		if not os.path.exists("gamefile"): os.mkdir("gamefile")
		save_path = 'C:\Users\\nt530\Desktop\Likelion\gamefile'
		name_of_file = raw_input("파일 이름을 입력하세요.: ")
		completeName = os.path.join(save_path, name_of_file)         
		file1 = open(completeName, "w")
		for i in lst:
			file1.write((str(i)+"\n"))
		file1.close()
		break
	else:
		break



