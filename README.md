## Carlton v0.01

This is a simple bot to vote for Carlton's favorite song in an online radio contest.

#### Features

* Proxy via openvpn
* Generate a complete persona including:
  - Random plausible name
  - 06 phone number
  - actual address (Street, postal code, city)
  - Temporary email address
  - Maybe a custom message
* Use openCV to decode a number captcha


### Questions

- Use real addresses or fake ones?
- Maybe don't even bother with tempmail, and just make fake emails using the names we generate, since it doesn't seem as if they verify them anyway
- Do we want to add a little note in the 'toelichting' to make it seem more legit?
- Do we stop voting at night? (who the fuck is voting in a radio contest at 4.30am)
- I can also add random timing to keystrokes to make it seem more legit, but I think this is overkill.



#### Todo
|What|Who|How|Done?|Notes|
|-|-|-|-|-|
|Proxy script|Glenn|Bash script via python?|In Progress||
|Name generator|Glenn|Python Script from csv source|In Progress||
|Phone generator|Bart|Python|Done||
|Adress Generator|Bart|Pyhon Script|Planning|Not sure if we do real addresses or not|
|Captcha solver 1: Plan Model|Bart|OpenCV python, image recognition||
|Captcha solver 2: Train number recogniser|Bart & Glenn|Tensorflow, need beefy GPU|Planning||
|Captcha solver 3: Test number recogniser|Bart & Glenn|Tensorflow, need beefy GPU|Planning||
|Captcha solver 4: Implement|Bart|Python|||
|Web Driver|Bart|Python with Selenium|Working Prototype||
