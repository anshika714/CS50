def main():
    time=input("What time is it ").strip()
    ntime=convert(time)
    if 7.0<=ntime<=8.0:
        print("Breakfast time")
    elif 12.0<=ntime<=13.0:
        print("Lunch time")
    elif 18.0<=ntime<=19.0:
        print("Dinner time")
def convert(t):
    t=t.strip().lower()
    if "a.m." in t or "p.m." in t:
        nt=t.replace("a.m."," ").replace("p.m."," ").strip()
    hours,min=nt.split(":")
    hours=int(hours)
    min=int(min)
    if "a.m." in t and hours==12:
        hours=0
    elif "p.m." in t and hours!=12:
        hours+=12
    return hours+min/60
if __name__=="__main__":
    main()
