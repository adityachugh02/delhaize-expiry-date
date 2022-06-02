# Expiry date reader

## Description
Building an expiry date reader with computer vision in Python

## Usage
Process:
- Employee receives list of articles he/she needs to check for expiry date
- Checks article expiry dates on shelf
- Removes expired products
- Takes a picture with the PDA of the closest expiry date from the products remaining on shelf

Expected benefits compared to manual encoding of expiry dates:
- Less mistakes
- Faster process

## API
API link: https://delhaize-expiry-date.herokuapp.com/  
POST: {"image": <image.JPG>}  
Response: {"prediction": prediction}  
GUI can be accessed through the browser at https://delhaize-expiry-date.herokuapp.com/

## Prerequisites
Python version: 3.10  
Main librairies: EasyOcr, Flask

## Contributors
Tony Anciaux  
Aditya Chugh  
Nadia Rosyidah  
Saina Nuersulitan  
Vincent Palau  
Anjali Tiwari  

## Timeline
#### Monday 2022-05-16
- First meeting
- Start project
#### Friday 2022-05-20
- First Q&A
#### Monday 2022-05-30
- Second Q&A
#### Wednesday 2022-06-01
- Finishing first version
#### Thursday 2022-06-02
- Deployment
#### Friday 2022-06-03
- Delivery

## Further improvements
- Ability to read a broader variety of formats 
- Ability to deal with dates on tricky packaging
- Higher accuracy
- More speed
- A mobile application on the PDA
