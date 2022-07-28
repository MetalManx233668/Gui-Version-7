from tkinter import * #for GUI
import random #randomises
from PIL import Image, ImageTk #for Images
import time 
from tkinter import messagebox  #error message box




class StartPage1:#the start up (intro page)

  
  def __init__(self, parent):
    background_color="lightblue"#background color

  
    self.alternative_generater=IntVar()

    self.user_name=Label(window, text="Please Enter your name Below: ", font=( "Times","18","bold"),bg=background_color)
    self.user_name.place(x=10, y=350)#username header (instructions for user)
    

    self.name_box=Entry(window)
    self.name_box.place(x=10, y=400)#username entry box (for users to follow out instructions)
    

    self.start_option = Button(window, text="Start quiz", font=( "Helvetica","13","bold"), bg="Light green",command=self.name_storing)
    self.start_option.place(x=10, y=440)#start option (progresses to quiz)

  def name_storing(self): #name storing
      name = self.name_box.get()
        # error managment
      if name == '':

        
            messagebox.showerror('Username is required!!', 'Please enter a username to continue!')#error message incase users try and continue without filling in entry box
      elif len(name) > 15: # code to ensure that name entred is beetween 3-15 characters
        messagebox.showerror('an error has occurred!', 'please enter a name between 3 - 15 lestters')#error message incase user has entered a username less than 3 letters

      elif len(name) < 3: # code to ensure that name entred is beetween 3-15 characters
        messagebox.showerror('an error has occurred!', 'please enter a name between 3 - 15 letters')#error message incase user has entered a username more than 15 letters
      elif name.isnumeric():
            messagebox.showerror('an error has occurred!', 'Username must only contain of letters!')
      elif not name.replace(' ','').isalpha(): # This will ensure that the username entred will only contain of letters and not numbers
        messagebox.showerror('an error has occurred!', 'Username must only contain of letters!')
      else:# this will ensure that the username entred will only contain of letters and not symbols

            names.append(name)  # add name to names list declared at the beginning
            print (names)
            self.user_name.destroy() #destroys the user name widget
            self.name_box.destroy() #destroys the name box widget
            self.start_option.destroy() #destroys the start option widget
            Main_page(window) #opens to main page
            time.sleep(0.5)

names = [] #list
asked = []#list
score = 0 #start score

def qna_randomising (): #determines the order of questions
    global qnum  #the question number (eg:Q5)
    qnum = random.randint(1,10) # amount of questions, randomly generates anumber from 1-10
    if qnum not in asked:# list declared at the start
      asked.append(qnum)
    elif qnum in asked:
      qna_randomising()

quiz_qna = { #Questions for quiz
    1: ["What is the biggest continent in the world?", 'South America', 'Asia','Europe', 'Antartica' ,'Asia',2],#Qna 1
    2: ["Which state is Niagra falls in?",'California','New York','Los Angeles', 'Florida','New York',2],#Qna 2
    3: ["Where would you find the leaning tower of pisa?", 'Italy','Spain', 'Greece','Sweden','Italy',1],#Qna 3
    4: ["In which country is cricket the national sport?",'South Africa','India','Australia','England','England',4],#Qna 4
    5: ["Which pacific nation has suva as their capital?", 'Tonga','Samoa','Fiji','Niue','Fiji',3],#Qna 5
    6: ["Which ocean surrounds the north pole?",'Arctic Ocean','Atlantic Ocean','Pacific Ocean','Indian Ocean','Arctic Ocean',1],#Qna 6
    7: ["What is the netherlands also known as?",'Vend','Nether','Holland','Nent','Benfica',3],#Qna 7
    8: ["What is the official currency of india?",'Peso','Euro','Pound','Rupee','Rupee',4],#Qna 8
    9: ["How many large islands make up hawaii?",'5','7','6','8','8',4],#Qna 9
    10: ["What is the largest US state by area?",'California','Texas','Alaska','Arizona','Alaska',3],#Qna 10



  }

class Main_page: #Questions page

  def __init__(self, parent):
    background_color="lightblue" # background color
 
 
    self.quiz_frame = Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.place(x=10,y=350) #frame of quiz page

    qna_randomising() #question generating

    self.question_header=Label(window, text = quiz_qna [qnum][0], font =( "Tw Cen MT","18","bold")) #questions
    self.question_header.place(x=10,y=300)  

    self.alternative_generater=IntVar()

    self.alternative1 = Radiobutton(window, text = quiz_qna [qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.alternative_generater, pady=10)
    self.alternative1.place(x=20, y=350) #alt 1

    self.alternative2 = Radiobutton(window, text = quiz_qna [qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, variable=self.alternative_generater, pady=10)
    self.alternative2.place(x=20, y=400) #alt 2

    self.alternative3 = Radiobutton(window, text = quiz_qna [qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, variable=self.alternative_generater, pady=10)
    self.alternative3.place(x=20, y=450) #alt 3

    self.alternative4 = Radiobutton(window, text = quiz_qna [qnum][4], font=("Helvetica", "12"), bg=background_color, value=4, variable=self.alternative_generater, pady=10)
    self.alternative4.place(x=20, y=500) #alt 4

    self.confirm_option = Button(window, text="Confrim",bg="white",command=self.scoring_system)
    self.confirm_option.place(x=200, y=400)#the confirm option is a button which will take the user to the next page
    self.score_accesibility= Label(window, text ='score')
    self.score_accesibility.place(x=220, y=450)  
    
    self.Exit = Button(window, text='Exit', font=('Helvetica', '13', 'bold'), bg='red', command=self.end_page) #the leave button will take the user to the end page

    self.Exit.place(x=900, y=520)#Exit button location
    
     
     
  def question_orginisation(self):
     qna_randomising()
     self.alternative_generater.set(0)
     self.question_header.config(text=quiz_qna [qnum][0])
     self.alternative1.config(text=quiz_qna [qnum][1])
     self.alternative2.config(text=quiz_qna [qnum][2])
     self.alternative3.config(text=quiz_qna [qnum][3])
     self.alternative4.config(text=quiz_qna [qnum][4])

 #score mechanics 
  def scoring_system(self):
      global score # this will ensure that the current score is accesible to all users
      scr_label=self.score_accesibility
      choice=self.alternative_generater.get()# get the users answer, alternative_generater is the IntVar() method that stores the number chosen by the user
      if len(asked)>9: # in order to dertimine when to open the end page and when is the final question
        if choice == quiz_qna [qnum][6]: # checks if the user has answered correctly, in the value area key is stored in index 6
          score +=1 # score gets added by one once the user answers correctly
          scr_label.configure(text=score)  # will edit the previous score to show the user the new score once the point gets added
          self.confirm_option.config(text="Confirm") # text on the confirm button will resort back to saying confirm
          self.end_page() # in order to open end page once questions are up or user activates the leave option
        else:
          score+=0 # score will stay the same
          time.sleep (1.5)
          scr_label.configure(text="The correct answer was: "+ quiz_qna [qnum][5] ) # will inform the user of the right answer before moving on to the next page if aswred incorrectly
          self.confirm_option.config(text="confirm") # text on the confirm button will resort back to saying confirm
          self.end_page()
     
      else:
            if choice==0:  #if user does not choose an opotion
              self.confirm_option.config(text="Try Again, selct an option to continue :)" ) # this error message will help the user recver from their error
              choice=self.alternative_generater.get() # answer that the user chose 
            else:
              if choice == quiz_qna [qnum][6]:  # will check if the option chossen is correct
                score+=1  # score will icrease by one point if correct answer
                scr_label.configure(text=score) #will edit the score on the score displayer
                self.confirm_option.config(text="confirm") #text on the confirm button will resort back to saying confirm
                self.question_orginisation() # progresses to next question:
      
              else: # if users choice was incorrect 
                  score+=0 # score willremain unchanged
                  scr_label.configure(text="The correct answer was: " + quiz_qna [qnum][5]) #  will inform the user of the right answer before moving on to the next page if aswred incorrectly
                  self.confirm_option.config(text="Confirm") #text on the confirm button will resort back to saying confirm
                  self.question_orginisation() # progresses to next question:


  def end_page(self): # method to end page
    window.destroy()
    name = names[0]
    open_end_object = End()



class End:


  def __init__(self):
        background_color = 'lightblue' #Background color of the page
        global end_window
        end_window = Tk()
        end_window.title('Exit Box') #Window title
        end_window.geometry('600x600') #Window size

        self.end_frame = Frame(end_window, width=700, height=600,bg=background_color)
        self.end_frame.grid(row=1)

        self.end_heading = Label(end_window,text='Thanks for trying the quiz :) ',  font=('Tw Cen Mt', 22, 'bold'), bg='lightblue') #Code for main heading of the page
        self.end_heading.place(x=100, y=50) #Location of the heading


        self.exit_button = Button(end_window,text='Exit',width=10,bg='white',font=('Tw Cen Mt', 12, 'bold'),command=self.close_end,) #Code for the exit button
        self.exit_button.place(x=260, y=200) #Location of the heading

        self.list_label = Label(end_window, text='Hope you had fun' + str(names),font=('Tw Cen Mt', 12, 'bold'),width=40, bg='lightblue') #Code for label to try again
        self.list_label.place(x=110, y=110) #Location of the label
        
        self.final_score = Label(end_window, text='Your final score is ' + str(score), font=('Tw Cen Mt', 12, 'bold'), width=40, bg='lightblue') #Code for quiz summary
        self.final_score.place(x=110, y=150)#Location of the label
        
  
  
  def close_end(self):
      self.end_frame.destroy() #destroys the end frame label
      self.end_heading.destroy() #destroys the end heading label
      self.exit_button.destroy() #destroys the exit button
      self.list_label.destroy() #destroys the list label
      end_window.destroy() #destroys the end window
  
  
  
if __name__ == '__main__':
  window = Tk()
  window.title('12CSC Quiz')
  window.geometry('700x600')
  bg_image = Image.open('start_page.jpg')
  bg_image = bg_image.resize((1000, 600), Image.ANTIALIAS)
  bg_image = ImageTk.PhotoImage(bg_image)
  image_label = Label(window, image=bg_image)
  image_label.place(x=0, y=0, relwidth=1, relheight=1)
  start_object = StartPage1(window)
  window.mainloop()
