# -*- coding: utf-8 -*-
"""
Created on Sat Jun  5 10:34:43 2021

@author: 82102
"""
import cv2
import numpy as np
import PIL
import matplotlib.pyplot as plt
from tkinter import *


class MyInformation:

   
    def __init__(self) :
        self.window = Tk()
        self.window.title("개인정보")   
        self.window.geometry("750x320+700+10")
        self.window.resizable(True,True)
        
        self.finishButton = Button(self.window, text = "입력완료", command = self.print).place(x = 0, y = 265, width = 100)
        self.saveButton = Button(self.window, text = "저장", command = self.save).place(x = 150, y = 265, width = 100)
        self.printButton = Button(self.window, text = "출력", command = self.scan).place(x = 300, y = 265, width = 100)
        self.RCButton = Button(self.window, text = "RC circuit", command = self.RC_Circuit).place(x = 450, y = 265, width = 100)
        self.IPButton = Button(self.window, text = "Image processing", command = self.Image_Processing).place(x = 600, y = 265, width = 100)
        
        self.label1 = Label(self.window, text = "개인정보").grid(row = 1, column = 1)
        self.label2 = Label(self.window, text = "학점").grid(row = 9, column = 1)
        self.label3 = Label(self.window, text = "Image Processing").place(x = 250, y = 0)
        self.label4 = Label(self.window, text = "RC circuit").place(x = 550, y = 0)
        
        self.label_name = Label(self.window, text = "성명").grid(row = 2, column = 0)
        self.name = StringVar()
        self.entry_name = Entry(self.window, width = 17, textvariable = self.name)
        self.entry_name.grid(row = 2, column = 1)
        
     
        
        self.label_age = Label(self.window, text = "나이").grid(row = 3, column = 0)
        self.age = StringVar()
        self.entry_age = Entry(self.window, width = 17, textvariable = self.age)
        self.entry_age.grid(row = 3, column = 1)
        
        
        self.label_studentNumber = Label(self.window, text = "학번").grid(row = 4, column = 0)
        self.studentNumber = StringVar()
        self.entry_studentNumber = Entry(self.window, width = 17, textvariable = self.studentNumber)
        self.entry_studentNumber.grid(row = 4, column = 1)
        
        self.label_grade = Label(self.window, text = "학년").grid(row = 5, column = 0)
        self.grade = StringVar()
        self.entry_grade = Entry(self.window, width = 17, textvariable = self.grade)
        self.entry_grade.grid(row = 5, column = 1)
        
        self.label_major = Label(self.window, text = "전공").grid(row = 6, column = 0)
        self.major = StringVar()
        self.entry_major = Entry(self.window, width = 17, textvariable = self.major)
        self.entry_major.grid(row = 6, column = 1)
        
        self.label_email = Label(self.window, text = "email").grid(row = 7, column = 0)
        self.email = StringVar()
        self.entry_email = Entry(self.window, width = 17, textvariable = self.email)
        self.entry_email.grid(row = 7, column = 1)
        
        self.label_score1 = Label(self.window, text = "1학년").grid(row = 10, column = 0)
        self.score1 = StringVar()
        self.entry_score1 = Entry(self.window, width = 3, textvariable = self.score1)
        self.entry_score1.grid(row = 10, column = 1)
        
        self.label_score2 = Label(self.window, text = "2학년").grid(row = 11, column = 0)
        self.score2 = StringVar()
        self.entry_score2 = Entry(self.window, width = 3, textvariable = self.score2)
        self.entry_score2.grid(row = 11, column = 1)
        
        self.label_score3 = Label(self.window, text = "3학년").grid(row = 12, column = 0)
        self.score3 = StringVar()
        self.entry_score3 = Entry(self.window, width = 3, textvariable = self.score3)
        self.entry_score3.grid(row = 12, column = 1)
        
        self.label_score4 = Label(self.window, text = "4학년").grid(row = 13, column = 0)
        self.score4 = StringVar()
        self.entry_score4 = Entry(self.window, width = 3, textvariable = self.score4)
        self.entry_score4.grid(row = 13, column = 1)
        
        self.window.mainloop()
    

    def print(self) :
        print("이름 :", self.name.get())
        print("나이 :", self.age.get())
        print("학번 :", self.studentNumber.get())
        print("학년 :", self.grade.get())
        print("전공 :", self.major.get())
        print("email :", self.email.get())
        print("1학년 학점 :", self.score1.get())
        print("2학년 학점 :", self.score2.get())
        print("3학년 학점 :", self.score3.get())
        print("4학년 학점 :", self.score4.get())
       
    def save(self) :
        f = open("20205220_이바다.txt", 'w')
        f.write("{}\n".format(self.name.get()))
        f.write("{}\n".format(self.age.get()))
        f.write("{}\n".format(self.studentNumber.get()))
        f.write("{}\n".format(self.grade.get()))
        f.write("{}\n".format(self.major.get()))
        f.write("{}\n".format(self.email.get()))
        f.write("{}\n".format(self.score1.get()))
        f.write("{}\n".format(self.score2.get()))
        f.write("{}\n".format(self.score3.get()))
        f.write(self.score4.get())
   
        f.close()
        print("파일에 저장되었습니다.")
        
    def scan(self) :
        f = open("20205220_이바다.txt", 'r')
        self.entry_name.delete(0,END)
        self.entry_age.delete(0,END)
        self.entry_studentNumber.delete(0,END)
        self.entry_grade.delete(0,END)
        self.entry_major.delete(0,END)
        self.entry_email.delete(0,END)
        self.entry_score1.delete(0,END)
        self.entry_score2.delete(0,END)
        self.entry_score3.delete(0,END)
        self.entry_score4.delete(0,END)

        self.entry_name.insert(0, f.readline())
        self.entry_age.insert(0, f.readline())
        self.entry_studentNumber.insert(0, f.readline())
        self.entry_grade.insert(0, f.readline())
        self.entry_major.insert(0, f.readline())
        self.entry_email.insert(0, f.readline())
        self.entry_score1.insert(0, f.readline())
        self.entry_score2.insert(0, f.readline())
        self.entry_score3.insert(0, f.readline())
        self.entry_score4.insert(0, f.readline())
        
        f.close()
        

    def Image_Processing(self) :
        image_shape = (384, 384, 3)
        working_dir = ".//"
        def lr_images(images_real, downscale) :
            images = []
            images.append(np.array(PIL.Image.fromarray(images_real).resize([images_real.shape[0]//downscale,images_real.shape[1]//downscale],
                                                                           resample=PIL.Image.BICUBIC)))
            images_lr = np.array(images)
            return images_lr            
        
        img2 = cv2.imread(working_dir + 'Pic1.png', cv2.IMREAD_UNCHANGED)
        print("img2", img2)
        print("img2 size :", img2.size)
        print("img2 shape :", img2.shape)
        
        img3 = np.reshape(img2[:,:,:3],(384,384,3))
        print("img3",img3)
        print("img3 size :",img3.size)
        print("img3 shape :",img3.shape)
        
        img4 = lr_images(img3,4)
        print("img4",img4)
        print("img4 size :",img4.size)
        print("img4 shape :",img4.shape)
        
        figsize = (24, 10)
        dim = (1, 2)
        plt.figure(figsize=figsize)
        plt.subplot(dim[0], dim[1], 1)
        plt.imshow(img2, interpolation = 'nearest')
        plt.title('Original : 384x384 ')
        plt.subplot(dim[0], dim[1], 2)
        plt.imshow(img4[0], interpolation = 'nearest')
        plt.title('Origianal Low Resolution : 96x96 ')
        plt.savefig("o1.png")
        plt.show()
        
        cv2.imwrite(working_dir + 'Pic1.png', img4[0])
        
        img2 = cv2.imread(working_dir + 'Pic2.png', cv2.IMREAD_UNCHANGED)
        print("img2", img2)
        print("img2 size :", img2.size)
        print("img2 shape :", img2.shape)
        
        img3 = np.reshape(img2[:,:,:3],(384,384,3))
        print("img3",img3)
        print("img3 size :",img3.size)
        print("img3 shape :",img3.shape)
        
        img4 = lr_images(img3,4)
        print("img4",img4)
        print("img4 size :",img4.size)
        print("img4 shape :",img4.shape)
        
        figsize = (24, 10)
        dim = (1, 2)
        plt.figure(figsize=figsize)
        plt.subplot(dim[0], dim[1], 1)
        plt.imshow(img2, interpolation = 'nearest')
        plt.title('Original : 384x384 ')
        plt.subplot(dim[0], dim[1], 2)
        plt.imshow(img4[0], interpolation = 'nearest')
        plt.title('Origianal Low Resolution : 96x96 ')
        plt.savefig("o2.png")
        plt.show()
        
        cv2.imwrite(working_dir + 'Pic2.png', img4[0])
        
        photo = cv2.imread("o1.png", cv2.IMREAD_UNCHANGED)
        photo_resize = cv2.resize(photo, dsize=(200, 100), interpolation=cv2.INTER_AREA)
        cv2.imwrite(working_dir + 'o1.png', photo_resize)
        self.photo1 = PhotoImage(file = 'o1.png')
        self.photo1_label = Label(self.window, image = self.photo1).place(x = 200, y = 25)
        
        
        photo = cv2.imread("o2.png", cv2.IMREAD_UNCHANGED)
        photo_resize = cv2.resize(photo, dsize=(200, 100), interpolation=cv2.INTER_AREA)
        cv2.imwrite(working_dir + 'o2.png', photo_resize)
        self.photo = PhotoImage(file = 'o2.png')
        self.photo_label = Label(self.window, image = self.photo).place(x = 200, y = 125)
        
        img_destroy = 1
        while img_destroy == 1 :
            img_destroy = int(input("input 0 to clear images."))
        else :
            cv2.destroyAllWindows()
        
        self.window.mainloop()

        
    def RC_Circuit(self) :
        Ydat = []
        Xdat = []
        Ndat = []
        n_max=6000
        
        R = 10000
        C = 0.000001
        dt = 0.00001
        
        Ytemp =0
        Xdat.append(Ytemp)
        Ydat.append(Ytemp)
        num = dt/R/C
        for n in range(0, n_max) :
            Xtemp=1
            Ytemp1=Ytemp
            Ytemp=(1-num)*Ytemp1+num*Xtemp
            Xdat.append(n*dt)
            Ydat.append(Ytemp)
            Ndat.append(n)
        print(Ydat)
        
 
       
        plt.figure(1)
        
        plt.plot(Xdat, Ydat)
        plt.xlabel('Time(sec)')
        plt.ylabel('VC', fontsize=20)
        plt.axis([0,0.1,0,2])
        plt.title("Step Response")
        plt.grid(True)
        plt.savefig('graph.png', dpi=45)
        
        self.gImage = PhotoImage(file = 'graph.png')
        self.label_g = Label(self.window, image = self.gImage).place(x = 450, y = 25)
        self.window.mainloop()
        
        
      
        
myinformation = MyInformation()

    
    