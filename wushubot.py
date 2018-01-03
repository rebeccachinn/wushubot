from slackclient import SlackClient
import time

slack_client=SlackClient("xoxb-291128787859-ih4VB21M7uTyl4aOXvEJnJ07")


responses={"practice1":"Practice’s are held 3-5 on Saturdays, and 8-10 on Mondays and Thursdays. Check the #practicelocation channel for the location, usually announced ~15 minutes before practice. ",
			"practice2":"Practice location will be announced via our #practicelocation channel, about 15 minutes before practice!",
			"condition":"Great! Check out this link for conditioning sets. The  Strength Plan is intended for members with access to a gym, while the Calisthenics one can be done without! Good luck! https://drive.google.com/drive/folders/1I-hiJpFjTIjGwAoEUvN83tkMNiV2Clyj?usp=sharing",
			"warmup":"warmup and conditioning exercises to be added soon!",
			"contact":"Eboard can be reached at columbiawushu@gmail.com. You can also checkout out website, columbiawushu.com, or send a direct message to anyone of our eboard members, Rebecca, Haejin, Katherine, Jeffrey, Jessica, or Anisa",
			"hi":"Hi friend!",
			"loctation":"Practice location will be announced via our #practicelocation channel, about 15 minutes before practice!",
			"greeting":"Life's good, thanks for asking! Ask me about practice, conditioning, warmups, or contacting eboard!",
			"bye":"Hope that helps. Bye friend!",
			"meaningoflife":"wushu is the meaning of life.",
			"intro":"I am wushubot, at your service!",
			"confused":"Hmm.. I don't quite understand. Ask me about practice, conditioning, warmups, or contacting eboard!"
			}
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
	message=message.lower()
	if ("practic" in message) and (("where" in message) or ("locat" in message)):
		t="practice2"
	elif ("practic" in message):
		t="practice1"
	elif ("condition" in message):
		t="condition"
	elif(("warm" in message) or ("stretch" in message)):
		t="warmup"
	elif(("contact" in message) or ("board" in message) or ("rebecca" in message)):
		t="contact"
	elif(("hey" in message) or ("hi"== message) or ("hi " in message) or ("hello" in message)):
		t="hi"
	elif(("sup" in message) or ("what's up" in message) or ("how are you" in message) or ("how's it going" in message)):
		t="greeting"
	elif(("thank" in message) or ("bye" in message) or ("ttyl" in message)):
		t="bye"
	elif ("meaning of life" in message):
		t="meaningoflife"
	elif(("who are you" in message) or ("your name" in message)):
		t="intro"
	else:
		t="confused"
	return t
def getResponse(t):
	r=responses[t]
	return r

def sendresponse(text,channel):
	slack_client.api_call("chat.postMessage",channel=channel, text=text, as_user=True)

def main():
	slackConnect()
	slackReadRTM()


if __name__ == '__main__':
	main()
