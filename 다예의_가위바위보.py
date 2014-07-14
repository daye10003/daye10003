#-*- coding:utf-8 -*-
import random
for i in range(3):
	i=random.randint(i)
array={"0":"가위", "1":"바위", "2":"보"}
computer=array[i]
player= raw_input("가위 바위 보!:")
if player not in "가위바위보":
	print "가위, 바위, 보 중 하나를 입력하세요."
else:
	if player==computer:
		print "비겼습니다."
		again = raw_input("다시 하시겠습니까?[예/아니오]")
		if again=="아니오":
		 	break
		elif again!="아니오" and again!="예":
			print "예/아니오 중 하나를 입력하세요."
	elif player=="가위":
		if computer=="보":
			print "cpu: 보"
			print "이겼습니다!"
			again = raw_input("다시 하시겠습니까?[예/아니오]")
			if again=="아니오":
		 		break
		 	elif again!="아니오" and again!="예":
				print "예/아니오 중 하나를 입력하세요."
		elif computer=="바위":
			print "cpu: 바위"
			print "졌습니다."
			again = raw_input("다시 하시겠습니까?[예/아니오]")
			if again=="아니오":
		 		break
		 	elif again!="아니오" and again!="예":
				print "예/아니오 중 하나를 입력하세요."
	elif player=="바위":
		if computer=="보":
			print "cpu: 보"
			print "졌습니다."
			again = raw_input("다시 하시겠습니까?[예/아니오]")
			if again=="아니오":
		 		break
		 	elif again!="아니오" and again!="예":
				print "예/아니오 중 하나를 입력하세요."
		elif computer=="가위":
			print "cpu: 가위"
			print "이겼습니다!"
			again = raw_input("다시 하시겠습니까?[예/아니오]")
			if again=="아니오":
		 		break
		 	elif again!="아니오" and again!="예":
				print "예/아니오 중 하나를 입력하세요."
	elif player=="보":
		if computer=="바위":
			print "cpu: 바위"
			print "이겼습니다!"
			again = raw_input("다시 하시겠습니까?[예/아니오]")
			if again=="아니오":
		 		break
		 	elif again!="아니오" and again!="예":
				print "예/아니오 중 하나를 입력하세요."
		elif computer=="가위":
			print "cpu: 가위"
			print "졌습니다."
			again = raw_input("다시 하시겠습니까?[예/아니오]")
			if again=="아니오":
		 		break
		 	elif again!="아니오" and again!="예":
				print "예/아니오 중 하나를 입력하세요."