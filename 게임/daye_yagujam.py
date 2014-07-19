#-*- coding:utf-8 -*-

import random
attempt=0
print "숫자 야구를 시작합니다!"
playing= True
again=True
onegame=True
save=""
while playing:
	computer=random.sample(range(0,10),4)
	computer = ''.join(str(i) for i in computer)
	attempt = 0
	print computer
	B=0
	S=0
	attempt+=1
	player= raw_input("서로 다른 숫자로 이루어진 네자리 숫자를 입력하세요: ")
	while not player.isdigit() or len(player) != 4 or len(player) !=len(set(player)):
		print "잘못 입력하셨습니다. 서로 다른 숫자로 이루어진 네자리 숫자를 입력하세요."
		player= raw_input("서로 다른 숫자로 이루어진 네자리 숫자를 입력하세요: ")
	for i in range(0,4):
		if player == computer:
			print "%s번째 시도에서 홈런!"%(attempt)
			while again == True:
				Qagain = raw_input("다시 하시겠습니까? 예/아니오: ")
				if Qagain != "예" and Qagain != "아니오":
					print "잘못 입력하셨습니다. 예 또는 아니오를 입력하세요."
				elif Qagain == "예 ":
					break
		elif player[i] in computer:
			if player[i]==computer[i]:
				S+=1
			else:
				B+=1
				if player != computer:
					print "%s번째 시도의 %sB, %sS 입니다." %(attempt, B, S)
	save= raw_input("저장하시겠습니까? 예/아니오: ")
	if save != "예" and save!="아니오":
		print "잘못 입력하셨습니다. 예 또는 아니오를 입력하세요."
	elif save == "예":
		print "서비스 준비중입니다."

