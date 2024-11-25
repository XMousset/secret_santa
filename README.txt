This code provide 
CSV file containing these columns : "Name", "Email", "Exclusions", "Gifts ideas"
Be sure to change the values in 'christmas_friends.py' and 'test.py' if your csv is different.



'yourpassword' is unique and given by your gmail account specifically for this usage.
Protocol for getting your password :
1. have 2-step Verification on (by adding a phone number for example)
2. go to app passwords (this link should work: 'myaccount.google.com/apppasswords')
3. set a name for the password (you can call it 'Python yagmail' for example)
4. copy the password (be careful, it cannot be seen again afterward, but can be deleted of course)
(There are many tutorials for this on the web, as example 'Google Gmail Remove Allow Less Secure Apps Option Alternative Solution' by 
Geeky Shows is a good one)

When you have your password, follow these steps ONE TIME in order to be able to send email :
1. install yagmail and keyring
2. register you email address and password using 'yagmail.register("youremail@gmail.com", "yourpassword")'

The 2nd step allows you to use yagmail without explicitely write your password in your code.
You can test if it works by sending an email to yourself using 'test_email.py'.

To delete a password, use 'keyring.delete_password("yagmail", "youremail@gmail.com")'.