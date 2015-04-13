#!/usr/bin/python

import urllib2


homePage = '''


<!DOCTYPE html>
<html>
	<head>
	<link rel="stylesheet" type="text/css" href="/styles.css">
	<meta charset = "UTF-8">
	<title>BeerMe - Verify Age</title>
</head>
<body>
	<table align ="center" width="800" cellspacing="0" cellpadding ="0" style="background-color: rgb(230,168,0); border-spacing: 0px">
		<tr>
			<td height="200" align="center"><a href="index.py"><img src="../images/foam.jpg" alt="banner" width="800" height="200" border="0" /></td>
		</tr>
	</table>
	<table align ="center" border="0" width="800" cellspacing="0" cellpadding="0">
		<tr valign="center" style="border-spacing: 0px;">
			<td width="188" align="center"><div class ="nav" ><a href="index.py">Home</a></div></td>
			<td width="188" align="center"><div class ="nav" ><a href="login.py">Login</a></div></td>
			<td width="188" align="center"><div class ="nav" ><a href="beerinfo.py">Beer Info</a></div></td>
			<td width="188" align="center"><div class ="nav" ><a href="resources.py">Other Resources</a></div></td>
			<td width="188" align="center"><div class ="nav" ><a href="about.py">About Us</a></div></td>
		</tr>
	</table>
	
	<table align="center" border="0" width="800" cellpadding="5">
	<tr valign ="top">
	<td>
	<br>
	<h1>Welcome to <strong style="font-size: 30px; letter-spacing: -2px">BeerMe</strong></h1>
	<p align="center">
	<strong>Please verify your age</strong>
	</p>
	

	<p align = "center">
	<input type="RADIO" value="http://www.toysrus.com" onclick="window.open(this.value)" name="ageChoice" id="ageRadio01"> I am not yet 21<br>
	<input type="RADIO" value="index.py" onclick="window.open(this.value)" name="ageChoice" id="ageRadio02"> I am 21 or over<br>
	</p>
			

	
	</td>
	</tr>
	</table>
</body>
</html>

'''
print homePage
