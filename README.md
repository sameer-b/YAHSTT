# YAHSTT
Yet Another HTTP Stress Test Tool
 
 This is a simple HTTP server test tool. Unlike most HTTP stress tools this does not require high bandwidth. It doesn't realyl flood the server with requests. It uses exploit similar to Pyloris/Slowloris where you open connections to the server but don't send the data.  
 Usage -> yadt.py <hostname> <port_number>
