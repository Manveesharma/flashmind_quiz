import requests,random,time,json,os,urllib.parse,pyttsx3

F="flashmind_mem.json"
def speak(t):
    if V:S.say(t);S.runAndWait()
def fetch(d="medium",c=9):
    u=f"https://opentdb.com/api.php?amount=8&category={c}&difficulty={d}&type=multiple&encode=url3986"
    r=requests.get(u).json()["results"];q=[]
    for i in r:
        Q=urllib.parse.unquote(i["question"]);A=urllib.parse.unquote(i["correct_answer"])
        O=[urllib.parse.unquote(x) for x in i["incorrect_answers"]]+[A];random.shuffle(O)
        q.append((Q,A,O))
    return q
def play(qs,d):
    s=0;w=[];st=0;t=[]
    for Q,A,O in qs:
        print(f"\n🔍{Q}");[print(f" {i+1}. {x}")for i,x in enumerate(O)]
        t0=time.time()
        while 1:
            u=input("🎯(num/text or 'exit'):").strip().lower()
            if u in["exit","quit"]:return s,"end"
            if not u:continue
            p=O[int(u)-1]if u.isdigit()and 1<=int(u)<=len(O)else u
            tt=time.time()-t0;t.append(tt)
            if p.lower()==A.lower():
                st+=1;b=max(0,int(6-tt));s+=1+b
                if tt<2:s+=2;print("⚡Speed Bonus!")
                if st>=5:s+=5;print("🔥Combo Bonus +5!");speak("Amazing combo!")
                m=random.choice(["🔥Excellent!","💪Smart!","🌟Brilliant!"])
                if st>=3:m+=f"🔥x{st}"
                print(f"✅+{1+b}pts({tt:.1f}s){m}");speak(random.choice(["Great!","Well done!"]));break
            else:w.append(Q);st=0;print(f"❌{A}.Keep going!");speak("Don't worry, you're improving!");break
    D["best"]=max(D.get("best",0),s);json.dump({"wrong":w,"best":D["best"]},open(F,"w"))
    print(f"🏅Best so far:{D['best']}")
    sk=s/(sum(t)/len(t)+1);nd="easy"if sk<1.5 else"medium"if sk<3 else"hard"
    print(f"🤖Adjusting difficulty→{nd}");return s,nd
if __name__=="__main__":
    print("🌟FlashMind AI v3 — Smart Quiz!\n")
    V=input("Enable voice?(y/n):").lower().startswith("y")
    S=pyttsx3.init()if V else None
    d=input("Start difficulty(easy/medium/hard):").lower().strip()or"medium"
    D=json.load(open(F))if os.path.exists(F)else{}
    if D.get("wrong"):print("📘Reviewing past weak topics!");speak("Welcome back! Let's review missed ones.")
    q=fetch(d);random.shuffle(q)
    s,d2=play(q,d)
    if d2!="end":
        fb="Great accuracy!"if s>8 else"Keep practicing!"if s>4 else"Try slower, think clearly!"
        print(f"\n🎉Final Score:{s}{'🏆'if s>8 else'✨'if s>5 else'💪'}-{fb}");speak(fb)
