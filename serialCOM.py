#!/usr/bin/env python2
import time
import serial
import array
import serial.tools.list_ports
import socket
import sys



#DEFINE SCRIPT ID STRINGS

#
# def flagpasser():
# 	def __init__():
# 		Fvalue = 'Pass'



# configure the serial connections (the parameters differs on the device you are connecting to)
def ScriptStart():
	#passnopass flag for script
	#global ssflag
	#ssflag = 0
	try:

		# print('Listing ports in use...')
		# ports = list(serial.tools.list_ports.comports())
		# for p in ports:
		# 	if (ports.startswith('USB Serial') | p.startswith('Serial')):
		# 		comvar = p
		# 		print(p)


		ser = serial.Serial("COM10",9600, timeout=0)
		# #print('debug')
		# 	if(ser):
		# 		pass
		# 	else:
		# 		print("Device not powered on")




		# print ('Enter your commands below.\r\nInsert "exit" to leave the application.')
		# print('Entering test script...\r\nType "exit"\r\nType "scriptstart" to begin script')
		#
		# while 1:
		# 	# get keyboard input
		# 	# input = raw_input(">> ")
		# 	# Python 3 users
		# 	Tinput = raw_input(">>")
		# 	if (Tinput == 'exit'):
		# 		print('test')
		# 		ser.close()
		# 		exit()
		# 	if (Tinput == 'scriptstart'):
		# send the character to the device
		# (note that I happend a \r\n carriage return and line feed to the characters - this is requested by my device)
		#after(2000)
		print('Serial test starting...')

		f = open('5440 Harris test.txt', "r")
		fo = open('Script results.txt', "w")
		numcounter = 0
		for line in f:
			time.sleep(0.5)
			print("Sending cmd: " + line)

			# line1 = line.rstrip('/n')
			# line2 = line1 + ('/r/n')
			# ser.write(line2)
			# ser.write("*idn?\r\n")

			ser.write(line.replace('\n', '\r\n'))
			TFLAG = 0
			time.sleep(1)
			print("Cmd Result: ")
			time.sleep(0.5)
			isResultValid = ser.readline()
			time.sleep(1)
			numcounter += 1
			if (isResultValid):
				print(isResultValid)
				# flagpasser.Fvalue = 'Pass'
				fo.write("Cmd: " + line + "     " + "Result: " + isResultValid)
			else:
				print("No Result\n")
				# flagpasser.Fvalue = 'Fail'
				fo.write("Cmd: " + line + "     " + "Result is not valid\r\n")


			# let's wait one second before reading output (let's give device time to answer)
		print("SerialCOM completed")

		if (ser.isOpen(self)):
			ser.close(self)
#############################

		f.close()
		# time.sleep(2)
		#
		# print("Ethernet test starting...")
		#
		# TCP_IP = '10.180.50.72'
		# TCP_PORT = 123
		# BUFF = 128
		#
		# # f = open('5440 Harris SCPI.txt', "r")
		# s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		# s.connect((TCP_IP, TCP_PORT))
		#
		# print("sending *idn cmd via eth")
		# s.send('*idn?')
		# data = s.recv(BUFF)
		#
		# s.close()
		# print ("received data: " + data)

		fo.close()
		print('Exiting script...')
		print('....')
		print('....')
		print('....')
		print('Press View Test Results')
		ssflag = 1
		print(ssflag)
		# if out != '':
		#	print (">>" + out)
		# else:
		# 	print('Invalid command')
		# 	exit
	except:
		print('\nERROR:\n')
		print('Serial not connected...')

	try:
		print("Starting Ethernet Scan")
		TCP_IP = '10.180.50.236'
		TCP_PORT = 10
		BUFFER_SIZE = 1024
		MESSAGE = "ROUTE:\sDELAY1\s200\n\r"
		#MESSAGE = "*IDN?\n\r"
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.connect((TCP_IP, TCP_PORT))
		s.send(MESSAGE)
		time.sleep(1)
		MESSAGE2 = "ROUTE:EXECUTEDELAY\n\r"
		s.send(MESSAGE2)
		time.sleep(1)
		print("Waiting for message...")
		#data = s.recv(BUFFER_SIZE)
		s.close()

		#print "received data:", data

	except:
		print('\nERROR:\n')
		print('Ethernet not connected...')
