import pyshorteners
user_input=input("Enter URL to shorten: ")
typeurl=pyshorteners.Shortener()
shorntner=typeurl.tinyurl.short(user_input)
print("Your shortened URL is:  " + shorntner) 