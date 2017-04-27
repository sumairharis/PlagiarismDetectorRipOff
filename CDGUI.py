from Tkinter import *
from nltk import word_tokenize
from nltk import pos_tag
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize

        
def coloromatext1(Strings,plagiarized,color):
        start=0
        end=0
        text1.delete(1.0,END)
        for i in range(len(Strings)):
           text1.insert("1."+str(start), Strings[i])
           end=end+len(Strings[i])
           text1.tag_add(str(i),"1."+str(start) , "1."+str(end))
         
           print "start","1."+str(start),"end",end,"for ",Strings[i]
           start=start+len(Strings[i])
           #add plagiarism insteada this dummy
           if(plagiarized[i]==True):
                   text1.tag_config(str(i), background=color, foreground="white")
           else:
                   text1.tag_config(str(i), background="white", foreground="black")
        text1.pack()
def coloromatext2(Strings,plagiarized,color):
        start=0
        end=0
        text2.delete(1.0,END)
        for i in range(len(Strings)):
           text2.insert("1."+str(start), Strings[i])
           end=end+len(Strings[i])
           text2.tag_add(str(i),"1."+str(start) , "1."+str(end))
         
           print "start","1."+str(start),"end",end,"for ",Strings[i]
           start=start+len(Strings[i])
           #add plagiarism insteada this dummy
           print(plagiarized)
           if(plagiarized[i]==True):
                   text2.tag_config(str(i), background=color, foreground="white")
           else:
                   text2.tag_config(str(i), background="white", foreground="black")
        text2.pack()

def test(threshold,ArrayWordlist1,SentencesAll1,CleanSentencesAll1,ArrayWordlist2,SentencesAll2,CleanSentencesAll2):
        plagiarized=[]
        plagiarizedfrom=[]
        plagiarizedfromtrueorfalse=[]
        netplagiarized=0
        for i in range(len(ArrayWordlist1)):
                        flag=0
                        copiedfromj=[]
                        for j in range(len(ArrayWordlist2)):
                                if  len(set(ArrayWordlist1[i]).intersection(set(ArrayWordlist2[j])))*100.0/(len(set(ArrayWordlist1[i]))) <=threshold:
                                        continue;
                                elif len(set(ArrayWordlist1[i]).intersection(set(ArrayWordlist2[j])))*100.0/(len(set(ArrayWordlist1[i]))) >threshold:
                                        flag=1
                                        netplagiarized+=1
                                        copiedfromj.append(j)
                        if flag==1:
                                copied=[]
                                for k in copiedfromj:
                                        copied.append(CleanSentencesAll2[k])
                                        plagiarizedfrom.append(k)   #storing indeces.
                                print CleanSentencesAll1[i],copied,"plagiarized"
                                plagiarized.append(True)
                        else:
                                print CleanSentencesAll1[i]," notplagiarized"
                                plagiarized.append(False)
        setofplagiarizedfrom=set(plagiarized)
        for p in range(len(CleanSentencesAll2)):
                if p in plagiarizedfrom:
                        plagiarizedfromtrueorfalse.append(True)
                else:
                        plagiarizedfromtrueorfalse.append(False)
                
                
        coloromatext1(SentencesAll1,plagiarized,"red")
        coloromatext2(SentencesAll2,plagiarizedfromtrueorfalse,"blue")
        return netplagiarized
			

def clean(a,Stop):
	Allsentences=[]
	for i in range(len(a)):
		newsentence=""
		words=word_tokenize(a[i])
		for each in words:
			if each in Stop:
				continue;
			else:
				newsentence+=each+" "
		Allsentences.append(newsentence)
		
	return Allsentences

def checkPlagiarism():
    Stop=stopwords.words('english')
    String1=text1.get(1.0,END)
    String2=text2.get(1.0,END)
    threshold=float(E1.get())

    
    SentencesAll1=sent_tokenize(String1)
    SentencesAll2=sent_tokenize(String2)

    CleanSentencesAll1=clean(SentencesAll1,Stop)
    CleanSentencesAll2=clean(SentencesAll2,Stop)

    WordsListArray1=[]
    for i in CleanSentencesAll1:
       WordsListArray1.append(word_tokenize(i))
    WordsListArray2=[]
    for i in CleanSentencesAll2:
       WordsListArray2.append(word_tokenize(i))
    result=test(threshold,WordsListArray1,SentencesAll1,CleanSentencesAll1, WordsListArray2,SentencesAll2,CleanSentencesAll2);

    result=result*100.0/len(SentencesAll1);
    E2.insert(0,str(result))


    
global E1,E2

root = Tk()
label1 = Label( root, text="Threshold")
E1 = Entry(root, bd =5)

label2 = Label( root, text="Net Similarity")
E2 = Entry(root, bd =5)

   


submit = Button(root, text ="Submit", command = checkPlagiarism)
global text1
global text2

text1= Text(root)
text1.pack(side=LEFT)

text2=Text(root)
text2.pack(side=RIGHT)

label1.pack()
E1.pack()

label2.pack()
E2.pack()



submit.pack(side =BOTTOM) 
root.mainloop()
