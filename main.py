from tkinter import * # Gui
import random # randomise
from PIL import Image, ImageTk # images
from tkinter import messagebox  # message box

names = [] # names list
asked = [] # asked list
score = 0  # score list

def question_randomiser():  # ensures that the order of questions is random
    global qnum
    qnum = random.randint(1, 10)  # randomly generates a number from 1-10 which corresponds to which question is asked
    if qnum not in asked:
        asked.append(qnum)
    elif qnum in asked:
        question_randomiser()


class startpage1:  # The start up page

    def __init__(self, parent):
        background_color = 'lightgrey'  # Background color 

        self.var1 = IntVar()

        self.user_heading = Label(window,
                text='Please Enter Your name Below:', font=('Times'
                , '18', 'bold'), bg=background_color)  # username instruction heading
        self.user_heading.place(x=10, y=350)  # heading location

        self.name_box = Button(window)  # username entry box
        self.name_box.place(x=10, y=400)  # username box location

        self.start_option = Button(window, text='Start quiz',
                                   font=('Helvetica', ' 13', 'bold'),
                                   bg='forestgreen',
                                   command=self.name_storing)  # start option (continues to next page)
        self.start_option.place(x=10, y=440)  # start option location

    def names_storing(self): #storing name
        name = self.name_box.get()
      # error managment
        if name == '':
            messagebox.showerror('Username required!!',
                                 'please enter a name to continue!') # error message if username box has not been filled (ensures a username)
        elif len(name) > 15:
            messagebox.showerror('an error has occurred!',
                                 'name must be beetween 3-15 characters, Try again!') #error message if username is more than 15 letters
        elif len(name) < 3:
            messagebox.showerror('an error has occurred!',
                                                                  'name must be beetween 3-15 characters, Try again!') #error message if username is less than 15 letters
        elif name.isnumeric():
            messagebox.showerror('an error has occurred!',
                                 'Name must only consist of letters, Please try again!') #Error message if user has typed in letters in the username box
        elif not name.isalpha():
            messagebox.showerror('an error has occurred!',
                                 'Name must onl consist of letters, Please try again!') #Error message if user has typed in symbols in the usernmae box
        else:
            names.append(name) #as declared at the start, will add names to the name list
            print (names)
            self.user_heading.destroy()  # Destroys user heading
            self.name_box.destroy()  # Destroys name box
            self.start_option.destroy()  # Destroys start option
            Quiz_questions(window) # Question page open
          

quiz_questions_answers = { #Quiz questions
    1: ["What is the biggest continent in the world?", 'South America', 'Asia','Europe', 'Antartica' ,'Asia',2],#Q1
    2: ["Which state is Niagra falls in?",'California','New York','Los Angeles', 'Florida','New York',2],#Q2
    3: ["Where would you find the leaning tower of pisa?", 'Italy','Spain', 'Greece','Sweden','Italy',1],#Q3
    4: ["In which country is cricket the national sport?",'South Africa','India','Australia','England','England',4],#Q4
    5: ["Which pacific nation has suva as their capital?", 'Tonga','Samoa','Fiji','Niue','Fiji',3],#Q5


}

class mainpage2: # main Quiz page

  def __init__(self, parent):
    background_color="lightblue"#page background color
 
 
    self.quiz_frame = Frame(parent, bg = background_color, padx=40, pady=40)
    self.quiz_frame.place(x=10,y=350) #frame of quiz page

    question_randomiser() #question randomiser

    self.question_heading=heading(window, text = questions_answers[qnum][0], font =( "Tw Cen MT","18","bold")) #questions
    self.question_label.place(x=10,y=350)  

    self.var1=IntVar()

    self.alternative1 = Radiobutton(window, text = questions_answers[qnum][1], font=("Helvetica", "12"), bg=background_color, value=1, variable=self.var1, pady=10)
    self.alternative1.place(x=20,y=350) #alternative 1 location

    self.alternative2 = Radiobutton(window, text = questions_answers[qnum][2], font=("Helvetica", "12"), bg=background_color, value=2, variable=self.var1, pady=10)
    self.alternative2.place(x=20,y=400) #alternative 2 location

    self.alternative3 = Radiobutton(window, text = questions_answers[qnum][3], font=("Helvetica", "12"), bg=background_color, value=3, variable=self.var1, pady=10)
    self.alternative3.place(x=20,y=450) #alternative 3 location

    self.alternative4 = Radiobutton(window, text = questions_answers[qnum][4], font=("Helvetica", "12"), bg=background_color, value=4, variable=self.var1, pady=10)
    self.alternative4.place(x=20,y=500) #alternative 4 location

    self.confirm_option = option(window, text="Confrim",bg="white",command=self.test_progress)
    self.confirm_option.place(x=200, y=400)#confirm option (progreses to next page)
    self.score_label = Label(window, text ='score')
    self.score_label.place(x=220, y=450)  
    
    self.leave = Option(window, text='Leave', font=('Helvetica', '13', 'bold'), bg='red', command=self.result_screen) #leave option (progresses to end page)

    self.leave.place(x=900, y=10)  
    
    
     
     
  def questions_organising(self):
     question_randomiser()
     self.var1.set(0)
     self.question_heading.config(text=questions_answers[qnum][0])
     self.alternative1.config(text=questions_answers[qnum][1])
     self.alternative2.config(text=questions_answers[qnum][2])
     self.alternative3.config(text=questions_answers[qnum][3])
     self.alternative4.config(text=questions_answers[qnum][4])

   #score mechanics 
  def scoring_system(self):
      global score # score must be accesibale to all users
      scr_label=self.score_label
      choice=self.var1.get()# get the user choice, remember are con1 is the IntVar() method that stores the number chosen
      if len(asked)>9: # in order to determine when to end the quiz after last question
        if choice == questions_answers[qnum][6]: # to check if the key has the correct answer which (stored in index 6 of the value area)
          score +=1 # adds a point to the score once correct answer
          scr_label.configure(text=score)  # this will change the heading to the new score once correct answer
          self.confirm_option.config(text="Confirm") # text on the confirm option will be confirm
          self.result_screen() # this will lead to the end page once the quiz is complete or user has activated the leave option
        else:
          score+=0 # score will remain unchanged once user does not get a correct answer
          scr_label.configure(text="The correct answer was: "+ questions_answers[qnum][5] ) # instead of showing the score, the coreect answer shall display
          self.confirm_option.config(text="confirm") # option
     
      else:
            if choice==0:  # if user does not select an option
              self.confirm_option.config(text="Try Again, you didn't select an option then submit again" ) # error message
              choice=self.var1.get() # still get the answer if they choose it
            else:
              if choice == questions_answers[qnum][6]:  # if the right choice is made
                score+=1  # adds a point to the score once correct answer
                scr_label.configure(text=score)
                self.confirm_option.config(text="confirm")
                self.questions_setup() # progresses to next question:
      
              else: # if wrong option was chosen
                  score+=0 # score will stay the same once wrong answer
                  scr_label.configure(text="The correct answer was: " + questions_answers[qnum][5]) # error message
                  self.confirm_option.config(text="Confirmn")
                  self.questions_setup() # progresses to next question:


  def final_screen(self): # end screen
    window.destroy() # destroys window
    name = names[0]
    open_end_object = end() #opens end page

class end:


  def __init__(self):
        background_color = 'lightblue' #Background color of the page
        global end_window
        end_window = Tk()
        end_window.title('Exit Box') #window title
        end_window.geometry('700x600') #window dimensions

        self.finish_frame = Frame(end_window, width=700, height=600,bg=background_color)
        self.finish_frame.grid(row=1)

        self.finish_heading = Label(end_window,text='Thanks For Trying Out The Quiz  ',  font=('Tw Cen Mt', 22, 'bold'), bg='white') #window main heading code
        self.finish_heading.place(x=100, y=50) #main heading location

        self.finish_heading2 = Label(window2,text='Hope you had fun ', font=('Tw Cen Mt', 17, 'bold'), 
 bg=background_color)
        self.finish_heading2.place(x=200, y=100)

        self.exit_option = option(end_window,text='Exit ',width=10,bg='red',font=('Tw Cen Mt', 12, 'bold'),command=self.close_end,) #exit option code
        self.exit_option.place(x=260, y=200) #heading location

        self.list_label = Label(end_window, text='Feel no hesitation to try again :)' + str(names),font=('Tw Cen Mt', 12, 'bold'),width=40, bg='lightblue') #Code for label to try again
        self.list_label.place(x=100, y=140) #Location of the label
        
        self.summary_score = Label(end_window, text='Your final score is ' + str(score), font=('Tw Cen Mt', 12, 'bold'), width=40, bg='white') #Code for quiz summary
        self.final_score.place(x=110, y=150)#Location of the label
        
  
  
  def close_end(self):
      self.end_frame.destroy() #destroys the end frame label
      self.finish_heading.destroy() #destroys the finish heading label
      self.exit_option.destroy() #destroys the exit option
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
  start_object = startpage1(window)
  window.mainloop()