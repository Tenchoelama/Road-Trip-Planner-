
import requests 


#url
url = "https://maps.googleapis.com/maps/api/distancematrix/json?"

#starting point
home = input("Enter City, From: ")

#destination
work = input('Enter City, To:  ')

#get response 
url2 = url+'origins='+home+'&destinations='+work+'&key=AIzaSyABTBiqUDJPPK0mQzboqBh5Gm2-V_NPXwE'
response = requests.get(url+'origins='+home+'&destinations='+work+'&key=AIzaSyABTBiqUDJPPK0mQzboqBh5Gm2-V_NPXwE')
print(url2)
print(response.text)


