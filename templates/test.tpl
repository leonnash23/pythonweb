<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Love page</title>
    <link rel="stylesheet" type="text/css" href="/static/mysite.css">
</head>
<body>
<h3>
% if a<1:
%   a=1
%end
%for i in range(a):
    Я люблю Ксюшу! <img src="/static/img/Heart.png" width="20">
%end
</h3>
</body>
</html>