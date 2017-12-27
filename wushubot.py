from slackclient import SlackClient
import time

slack_client=SlackClient(<<enter token>>)

def slackConnect():
	return slack_client.rtm_connect()

def slackReadRTM():
	while True:
		rec=slack_client.rtm_read()
		print(rec)
		if(len(rec)!=0):
			rec=rec[0]
			if rec['type']=='message' and rec['user']!="U8K3SP5R9":
				text=rec['text']
				t=getMsgType(text)
				r=getResponse(t)
				channel=rec['channel']
				sendresponse(r,channel)
		time.sleep(1)

def getMsgType(message):
	#1= practice
	#2=condition
	#3=warmup or stretch
	#4=contact
	#5=hi
	#6=practice location
	#7=sup
	#8=end
	#9=who
	#0=unknown
	message=message.lower()
	if ("practic" in message) and (("where" in message) or ("locat" in message)):
		t=6
	elif ("practic" in message):
		t=1
	elif ("condition" in message):
		t=2
	elif(("warm" in message) or ("stretch" in message)):
		t=3
	elif(("contact" in message) or ("board" in message) or ("rebecca" in message)):
		t=4
	elif(("hey" in message) or ("hi"== message) or ("hi " in message) or ("hello" in message)):
		t=5
	elif(("sup" in message) or ("what's up" in message) or ("how are you" in message) or ("how's it going" in message)):
		t=7
	elif(("thank" in message) or ("bye" in message) or ("ttyl" in message)):
		t=8
	elif ("meaning of life" in message):
		t=9
	elif(("who are you" in message) or ("your name" in message)):
		t=10
	else:
		t=0
	return t
def getResponse(t):
	if t==1:
		r="Practice’s are held 3-5 on Saturdays, and 8-10 on Mondays and Thursdays. Check the #practicelocation channel for the location, usually announced ~15 minutes before practice. "
	elif t==2:
		r="Great! Check out this link for conditioning sets. The  Strength Plan is intended for members with access to a gym, while the Calisthenics one can be done without! Good luck! https://drive.google.com/drive/folders/1I-hiJpFjTIjGwAoEUvN83tkMNiV2Clyj?usp=sharing"
	elif t==3:
		r="warmup and conditioning exercises to be added soon!"
	elif t==4:
		r="Eboard can be reached at columbiawushu@gmail.com. You can also checkout out website, columbiawushu.com, or send a direct message to anyone of our eboard members, Rebecca, Haejin, Katherine, Jeffrey, Jessica, or Anisa"
	elif t==5:
		r="Hi friend!"
	elif t==6:
		r="Practice location will be announced via our #practicelocation channel, about 15 minutes before practice!"
	elif t==7:
		r="Life's good, thanks for asking! Ask me about practice, conditioning, warmups, or contacting eboard!"
	elif t==8:
		r="Hope that helps. Bye friend!"
	elif t==9:
		r="wushu is the meaning of life."
	elif t==10:
		r="I am wushubot, at your service!"
	else:
		r="Hmm.. I don't quite understand. Ask me about practice, conditioning, warmups, or contacting eboard!"
	return r

def sendresponse(text,channel):
	slack_client.api_call("chat.postMessage",channel=channel, text=text, as_user=True)

def main():
	slackConnect()
	slackReadRTM()


if __name__ == '__main__':
	main()
