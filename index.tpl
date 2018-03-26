<html>
<head>
	<title>Headline</title>
	<link rel="stylesheet" type="text/css" href="static/style.css"> 
</head>
<body>
	<div class="full_width" id="wrap">
	<table class="table">
	%for row in rows:
		<tr>
			<td class="date">{{row[0]}}</td>
			<td class="pub">{{row[1]}}</td>
			<td class="title"><a href="{{row[3]}}">{{row[2]}}</a></td>
		</tr>
	%end
	</table>
	</div>
</body>
</html>
