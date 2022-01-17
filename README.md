# Assignment2# Assignment2
Created an instance in AWS EC2 ( Amazon Linux (Inferred))
Moved the instance to the previously created Service group

In the user tags gave the following text 
#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
EC2ID='{"coord":{"lon":-123.262,"lat":44.5646},"weather":[{"id":701,"main":"Mist","description":"mist","icon":"50n"}],"base":"stations","main":{"temp":41,"feels_like":41,"temp_min":37.15,"temp_max":47.28,"pressure":1024,"humidity":79},"visibility":8047,"wind":{"speed":1.01,"deg":90,"gust":1.01},"clouds":{"all":100},"dt":1642295831,"sys":{"type":2,"id":2040223,"country":"US","sunrise":1642261568,"sunset":1642294710},"timezone":-28800,"id":5720727,"name":"Corvallis","cod":200}'


echo '<center><h5>EC2ID</h5></center>' > /var/www/html/index.txt
sed "s/EC2ID/$EC2ID/" /var/www/html/index.txt > /var/www/html/index.html

If we restart the aws server the content will be displayed on the Public Ipv4. Have attached the screenshot in the assignment when the instance was working.
Currently running on http://34.224.173.103/
