SPAM_WORDS = [
        "free", "winner", "won", "prize", "lottery",
        "urgent", "click", "claim", "cash", "verify",
        "congratulations", "offer", "limited", "now", "account"
]
def checkk_spam(message):
    words = message.lower().split()
    count = 0
    for i in words:
        i = i.strip(".,!?:;\"'()")
        if i in SPAM_WORDS:
            count +=1
    if count>=2:
        return"SPAM"
    else:
        return"SAFE"
# Test messages
messages = [
    "Congratulations! You won a free prize",
    "Urgent! Verify your account",
    "Hey, how are you?",
    "plz give api adress "
    "Your free coding class starts today"
]
for i in messages:
    print(i,"->",checkk_spam(i))
while True:
    messages = input ("\n Enter a message  (OR TYPE quit):")
    if messages.lower()== quit :
        break
    print("result:",checkk_spam(messages))