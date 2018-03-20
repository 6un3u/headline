<table border = "1">
%for row in rows:
	<tr>
		<td>{{row[0]}}</td>
		<td>{{row[1]}}</td>
		<td><a href="{{row[3]}}">{{row[2]}}</a></td>
	</tr>
%end
</table>
