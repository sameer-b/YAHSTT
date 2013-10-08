
# Copyright (C) 2013 Sameer Balasubrahmanyam

#This program is free software; you can redistribute it and/or
#modify it under the terms of the GNU General Public License
#as published by the Free Software Foundation; either version 2
#of the License, or (at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program; if not, write to the Free Software
#Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.


import socket
import sys

def yadt(host,port):
	try:
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		print s
	except socket.error, msg:
		print 'Couldn\'t create a socket' + str(msg[0]) + ' , error : ' + msg[1]
		print msg, socket.error
		sys.exit();
 
	print 'A new socket created'

	try:
		remote_ip = socket.gethostbyname( host )
	except socket.gaierror:
		print 'Couldn\'t get IP. Error'
		print socket.gaierror 
		sys.exit()
     
	print 'IP: ' + remote_ip + ' Host ' + host
 

	s.connect((remote_ip , port))
 
	print 'Firing -> ' + remote_ip + '/' + host


if len(sys.argv) == 0:
	print "Usage -> yadt.py <hostname> <port_number>"

if len(sys.argv) <3 and len(sys.argv) > 0:
	print "Error! Usage -> yadt.py <hostname> <port_number> "


try:
	while True:
		yadt(sys.argv[1],int(sys.argv[2]))
except KeyboardInterrupt:
	sys.exit(0)
