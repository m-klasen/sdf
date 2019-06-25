
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from functions import *
from kalman_function import *
import tkinter as tk
from tkinter import Frame,Label,Entry,Button,Checkbutton,Radiobutton,IntVar,BooleanVar
import tkinter.ttk as ttk
import sys
from matplotlib.patches import Ellipse
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.axes_grid1 import host_subplot



class Window(Frame):
		
	def __init__(self, master = None):
		Frame.__init__(self, master)
		self.master = master
		self.sen1 = BooleanVar()
		self.sen2 = BooleanVar()
		self.sen3 = BooleanVar()
		self.sen4 = BooleanVar()
		self.measure = IntVar()
		self.multsen = BooleanVar()
		self.plot_ell = BooleanVar()
		self.kalm1 = BooleanVar()
		self.kalm2 = BooleanVar()
		self.kalm3 = BooleanVar()
		self.kalm4 = BooleanVar()
		self.multsen_kalm = BooleanVar()
		self.init_window()

	def clear(self):
		self.ax.cla()
		self.init_plots()

	def init_plots(self):

		### Initialization of all Plots


		self.x_line1=[]
		self.y_line1=[]		
		self.x_line2=[]
		self.y_line2=[]
		self.x_line3=[]
		self.y_line3=[]
		self.x_line4=[]
		self.y_line4=[]
		self.z_k_fusion_x=[]
		self.z_k_fusion_y=[]

		### Ground Truth Plot
		self.ground = self.ax.plot([calcPosition(i)[0] for i in range(0,1000)],[calcPosition(i)[1] for i in range(0,1000)],c="b")
		
		### Current Position Plot
		self.scat2 = self.ax.scatter(0, 0, vmin=0, vmax=1,c=["r"], edgecolor="k")
		
		### Visual display Plot of Sensor 1-4
		self.sen1_scat = self.ax.scatter(self.sen1_pos[0],self.sen1_pos[1],c=["r"], edgecolor="k")
		self.sen2_scat = self.ax.scatter(self.sen2_pos[0],self.sen2_pos[1],c='#0343df', edgecolor="k")
		self.sen3_scat = self.ax.scatter(self.sen3_pos[0],self.sen3_pos[1],c='#fe01b1', edgecolor="k")
		self.sen4_scat = self.ax.scatter(self.sen4_pos[0],self.sen4_pos[1],c='#d5b60a', edgecolor="k")


		self.pltsen1, = self.ax.plot([],[],marker="x",c='r', markerfacecolor="r")
		self.pltsen2, = self.ax.plot([],[],marker="x",c='#0343df', markerfacecolor="r")
		self.pltsen3, = self.ax.plot([],[],marker="x",c='#fe01b1', markerfacecolor="r")
		self.pltsen4, = self.ax.plot([],[],marker="x",c='#d5b60a', markerfacecolor="r")
		self.pltsen5, = self.ax.plot([],[],marker="x", markerfacecolor="r")

		### Sensorfusion
		self.multisen, = self.ax.plot([],[],marker="x", markerfacecolor="b")

		self.ell1 = Ellipse(xy=(0,0),width=1, height=1,angle=2,facecolor="r",alpha=0.5)
		self.ax.add_patch(self.ell1)

		self.ell2 = Ellipse(xy=(0,0),width=1, height=1,angle=2,facecolor='#0343df',alpha=0.5)
		self.ax.add_patch(self.ell2)

		self.ell3 = Ellipse(xy=(0,0),width=1, height=1,angle=2,facecolor='#fe01b1',alpha=0.5)
		self.ax.add_patch(self.ell3)

		self.ell4 = Ellipse(xy=(0,0),width=1, height=1,angle=2, facecolor='#d5b60a',alpha=0.5)
		self.ax.add_patch(self.ell4)

		self.ell_p = Ellipse(xy=(0,0),width=1, height=1,angle=2, facecolor='#d5b60a',alpha=0.5)
		self.ax.add_patch(self.ell_p)




		self.ax.axis([-1500, 1500, -1500, 1500])
		self.bx.axis([0, 1000, 0, 1000])		
	def init_window(self):
		### Window Interface
		self.kart = Radiobutton(self, text="Kart Messung", variable=self.measure,value=1)
		self.kart.grid(row=0,column=0)

		self.polar = Radiobutton(self, text="Polar Messung", variable=self.measure,value=0)
		self.polar.grid(row=0,column=1)

		self.sensor1 = Checkbutton(self, text="Sensor 1", variable=self.sen1)
		self.sensor1.grid(row=1,column=0)

		self.sensor2 = Checkbutton(self, text="Sensor 2", variable=self.sen2,onvalue = 1, offvalue = 0)
		self.sensor2.grid(row=2,column=0)

		self.sensor3 = Checkbutton(self, text="Sensor 3", variable=self.sen3,onvalue = 1, offvalue = 0)
		self.sensor3.grid(row=3,column=0)

		self.sensor4 = Checkbutton(self, text="Sensor 4", variable=self.sen4,onvalue = 1, offvalue = 0)
		self.sensor4.grid(row=4,column=0)

		self.senfus = Checkbutton(self, text="Multisensor", variable=self.multsen,onvalue = 1, offvalue = 0)
		self.senfus.grid(row=5,column=0)

		self.plot_ellipses = Checkbutton(self, text="Cov. Ellipses (polar only)", variable=self.plot_ell ,onvalue = 1, offvalue = 0)
		self.plot_ellipses.grid(row=0,column=3)

		self.kalman1 = Checkbutton(self, text="Kalman 1", variable=self.kalm1, offvalue = 0,onvalue = 1)
		self.kalman1.grid(row=1,column=1)

		self.kalman2 = Checkbutton(self, text="Kalman 2", variable=self.kalm2,onvalue = 1, offvalue = 0)
		self.kalman2.grid(row=2,column=1)

		self.kalman3 = Checkbutton(self, text="Kalman 3", variable=self.kalm3,onvalue = 1, offvalue = 0)
		self.kalman3.grid(row=3,column=1)

		self.kalman4 = Checkbutton(self, text="Kalman 4", variable=self.kalm4,onvalue = 1, offvalue = 0)
		self.kalman4.grid(row=4,column=1)

		self.kalm_fus = Checkbutton(self, text="Kalman Fusion", variable=self.multsen_kalm,onvalue = 1, offvalue = 0)
		self.kalm_fus.grid(row=5,column=1)

		self.clear_button = Button(self, text="Clear Plot", command=self.clear)
		self.clear_button.grid(row=6,column=1)

		self.close_button = Button(self, text="Close", command=self.quit)
		self.close_button.grid(row=6,column=2)

		### Sensor Placement init
		self.sen1_pos = [500,0]
		self.sen2_pos = [0,500]
		self.sen3_pos = [-500,0]
		self.sen4_pos = [0,-500]

		self.gTruth =[]
		self.measure_r =[]
		self.measureX=[]
		self.measureY =[]
		self.kFilter =[]		
		self.kFilter1 =[]
		self.kFilter2 =[]
		self.kFilter3 =[]
		self.kFilter4 =[]
		self.kFilterY =[]
		self.kFilterY1 =[]
		self.kFilterY2 =[]
		self.kFilterY3 =[]
		self.kFilterY4 =[]
		self.x_all=[]
		self.predictions_x=[]
		self.predictions_y=[]
		self.predictions_x1=[]
		self.predictions_y1=[]
		self.predictions_x2=[]
		self.predictions_y2=[]
		self.predictions_x3=[]
		self.predictions_y3=[]
		self.predictions_x4=[]
		self.predictions_y4=[]

		self.fig = plt.figure(figsize=(5,8))
		self.ax = self.fig.add_subplot(211)
		self.bx = self.fig.add_subplot(212)
		self.init_plots()

		### Kalman
		self.kalm_rad, = self.bx.plot([],[], markerfacecolor="o", label="Radar deviation to truth ")	
		self.kalm_filt, = self.bx.plot([],[], markerfacecolor="b", label="Kalman Sensorfusion")
		self.kalm_filt1, = self.bx.plot([],[], markerfacecolor="b", label="Kalman1")	
		self.kalm_filt2, = self.bx.plot([],[], markerfacecolor="b", label="Kalman2")	
		self.kalm_filt3, = self.bx.plot([],[], markerfacecolor="b", label="Kalman3")	
		self.kalm_filt4, = self.bx.plot([],[], markerfacecolor="b", label="Kalman4")		
		self.bx.legend()
		
		### Kalman Init from kalman_function.py
		t = 1/5
		F= np.array([[1,t,0.5*t**2],
					 [0,1,t],
					 [0,0,1]])
		D = np.array([[0.25*t**4,0.5*t**3, 0.5*t**2],
					 [0.5*t**3,t**2,t],
					 [0.5*t**2,t,1]])*0.6**2
		H = np.array([[1,0,0],
					  [1,0,0]]).reshape(2, 3)
		R = np.eye(2)*50**2
		P = np.eye(3)*10

		kf = Kalman(F = F,P=P, H = H, D = D, R = R)
		kf1 = Kalman(F = F,P=P, H = H, D = D, R = R)
		kf2 = Kalman(F = F,P=P, H = H, D = D, R = R)
		kf3 = Kalman(F = F,P=P, H = H, D = D, R = R)
		kf4 = Kalman(F = F,P=P, H = H, D = D, R = R)

		### Helper funktions for Ellipse Plotting 
		def cart_error_covar(pos,p1):
			[x_k,y_k] = pos
			[x_p,y_p] = p1

			phi = np.arctan2((y_p-y_k),(x_p-x_k))
			r = np.linalg.norm(np.array(p1)-np.array(pos))
			R = np.array([[20**2,0],[0,(r*0.2)**2]])
			D = np.array([[math.cos(phi),-math.sin(phi)],
						[math.sin(phi),math.cos(phi)]])
			R_k = D @ R @ D.T
			return R_k

		def cov_ellipse(cov, nstd=2):
			vals, vecs = np.linalg.eigh(cov)
			theta = np.degrees(np.arctan2(*vecs[:, 0][::-1]))
			width,height = 2 * nstd * np.sqrt(vals)
			return width, height, theta


		def update(i):
			z_k=[]
			###Get data all kinds of data
			### Polar_radar(t,x_r,y_r) -> [x,y],range,azimuth
			p1,r_1,phi_1 = polar_RadarPunkt(i, self.sen1_pos[0], self.sen1_pos[1])
			p2,r_2,phi_2 = polar_RadarPunkt(i, self.sen2_pos[0], self.sen2_pos[1])
			p3,r_3,phi_3 = polar_RadarPunkt(i, self.sen3_pos[0], self.sen3_pos[1])
			p4,r_4,phi_4 = polar_RadarPunkt(i, self.sen4_pos[0], self.sen4_pos[1])
			p1_ra,_,_ = polar_coord(i, self.sen1_pos[0], self.sen1_pos[1])
			p2_ra,_,_ = polar_coord(i, self.sen2_pos[0], self.sen2_pos[1])
			p3_ra,_,_ = polar_coord(i, self.sen3_pos[0], self.sen3_pos[1])
			p4_ra,_,_  = polar_coord(i, self.sen4_pos[0], self.sen4_pos[1])
			c1,x_d1,y_d1 = cart_coord(i,50)
			c2,x_d2,y_d2 = cart_coord(i,50)
			c3,x_d3,y_d3 = cart_coord(i,50)
			c4,x_d4,y_d4 = cart_coord(i,50)
			xy = [calcPosition(i),p1,p2,p3,p4,c1,c2,c3,c4]
			tmp = np.c_[np.array(xy).T[0], np.array(xy).T[1]]
			### Plot Current position
			self.scat2.set_offsets(tmp[0,:2])

			if self.measure.get()==0:
				R_1 = np.array([[r_1[0]**2,0],[0,(p1_ra[0]*phi_1[0])**2]])
				R_2 = np.array([[r_2[0]**2,0],[0,(p2_ra[0]*phi_2[0])**2]])
				R_3 = np.array([[r_3[0]**2,0],[0,(p3_ra[0]*phi_3[0])**2]])
				R_4 = np.array([[r_4[0]**2,0],[0,(p4_ra[0]*phi_4[0])**2]])

			elif self.measure.get()==1:
				R_1 = np.array([[x_d1[0]**2,0],[0,y_d1[0]**2]])
				R_2 = np.array([[x_d2[0]**2,0],[0,y_d2[0]**2]])
				R_3 = np.array([[x_d3[0]**2,0],[0,y_d3[0]**2]])
				R_4 = np.array([[x_d4[0]**2,0],[0,y_d4[0]**2]])
			### Plot Sensor Measurements for Cart. or Polar
			if i%5==0:
				### Kart. or Polar.
				if self.measure.get()==0:
					self.x_line1.append(tmp[1][0])
					self.y_line1.append(tmp[1][1])
					self.x_line2.append(tmp[2][0])
					self.y_line2.append(tmp[2][1])
					self.x_line3.append(tmp[3][0])
					self.y_line3.append(tmp[3][1])
					self.x_line4.append(tmp[4][0])
					self.y_line4.append(tmp[4][1])


				elif self.measure.get()==1:
					self.x_line1.append(tmp[5][0])
					self.y_line1.append(tmp[5][1])
					self.x_line2.append(tmp[6][0])
					self.y_line2.append(tmp[6][1])
					self.x_line3.append(tmp[7][0])
					self.y_line3.append(tmp[7][1])
					self.x_line4.append(tmp[8][0])
					self.y_line4.append(tmp[8][1])

				if self.sen1.get()==True:
					###Plot Radar Measurements which occur every 5sec
					self.pltsen1.set_data(self.x_line1,self.y_line1)

					###Plot measurement error covariance ellipse
					if self.plot_ell.get()==True:
						width,height,theta=cov_ellipse(cart_error_covar(self.sen1_pos,p1))
						self.ell1.center=(p1[0], p1[1])
						self.ell1.width=width
						self.ell1.height=height
						self.ell1.angle=theta				
				if self.sen2.get()==True:
					###Plot Radar Measurements which occur every 5sec
					self.pltsen2.set_data(self.x_line2,self.y_line2)

					###Plot measurement error covariance ellipse
					if self.plot_ell.get()==True:
						width,height,theta=cov_ellipse(cart_error_covar(self.sen2_pos,p2))
						self.ell2.center=(p2[0], p2[1])
						self.ell2.width=width
						self.ell2.height=height
						self.ell2.angle=theta	

				if self.sen3.get()==True:
					###Plot Radar Measurements which occur every 5sec
					self.pltsen3.set_data(self.x_line3,self.y_line3)

					###Plot measurement error covariance ellipse
					if self.plot_ell.get()==True:
						width,height,theta=cov_ellipse(cart_error_covar(self.sen3_pos,p3))
						self.ell3.center=(p3[0], p3[1])
						self.ell3.width=width
						self.ell3.height=height
						self.ell3.angle=theta	
				if self.sen4.get()==True:
					###Plot Radar Measurements which occur every 5sec
					self.pltsen4.set_data(self.x_line4,self.y_line4)

					###Plot measurement error covariance ellipse
					if self.plot_ell.get()==True:
						width,height,theta=cov_ellipse(cart_error_covar(self.sen4_pos,p4))
						self.ell4.center=(p4[0], p4[1])
						self.ell4.width=width
						self.ell4.height=height
						self.ell4.angle=theta
	
				### Multisensor-fusion für Kartesisch oder Polar
				R_k = np.linalg.inv((np.linalg.inv(R_1)+
									np.linalg.inv(R_2)+
									np.linalg.inv(R_3)+
									np.linalg.inv(R_4)))
				### Fuse polar measurements 
				if self.measure.get()==1:
					z_k = R_k.dot((np.linalg.inv(R_1).dot(tmp[5].T)+
								  np.linalg.inv(R_2).dot(tmp[6].T)+
								  np.linalg.inv(R_3).dot(tmp[7].T)+
								  np.linalg.inv(R_4).dot(tmp[8].T)))
				### Fuse Cart. Measurements
				if self.measure.get()==0:
					z_k = R_k.dot((np.linalg.inv(R_1).dot(tmp[1].T)+
								  np.linalg.inv(R_2).dot(tmp[2].T)+
								  np.linalg.inv(R_3).dot(tmp[3].T)+
								  np.linalg.inv(R_4).dot(tmp[4].T)))						
				self.z_k_fusion_x.append(z_k[0])
				self.z_k_fusion_y.append(z_k[1])
				if self.multsen.get()==True:	
					self.multisen.set_data(self.z_k_fusion_x,self.z_k_fusion_y)



			predict = H @ kf.predict()
			self.predictions_x.append(predict[0][0])
			self.predictions_y.append(predict[1][0])	
			self.kFilter.append([self.predictions_x[-1][0],self.predictions_y[-1][0]])	

			predict_1 = H @ kf1.predict()
			self.predictions_x1.append(predict_1[0][0])
			self.predictions_y1.append(predict_1[1][0])	
			self.kFilter1.append([self.predictions_x1[-1][0],self.predictions_y1[-1][0]])
	
			predict_2 = H @ kf2.predict()
			self.predictions_x2.append(predict_2[0][0])
			self.predictions_y2.append(predict_2[1][0])	
			self.kFilter2.append([self.predictions_x2[-1][0],self.predictions_y2[-1][0]])	

			predict_3 = H @ kf3.predict()
			self.predictions_x3.append(predict_3[0][0])
			self.predictions_y3.append(predict_3[1][0])	
			self.kFilter3.append([self.predictions_x3[-1][0],self.predictions_y3[-1][0]])	

			predict_4 = H @ kf4.predict()
			self.predictions_x4.append(predict_4[0][0])
			self.predictions_y4.append(predict_4[1][0])	
			self.kFilter4.append([self.predictions_x4[-1][0],self.predictions_y4[-1][0]])	

			self.x_all.append(i)
			self.gTruth.append(calcPosition(i))
			if (i%5==0) or (i==0):
				kf.update(z_k)
				kf1.update(p1)
				kf2.update(p2)
				kf3.update(p3)
				kf4.update(p4)				

				self.measure_r.append(p1)
				self.measureX.append(i)
				self.measureY.append(coord_Distanz(self.measure_r[-1], self.gTruth[i]))


			
				

			self.kFilterY.append(coord_Distanz(self.kFilter[i], self.gTruth[i]))
			self.kFilterY1.append(coord_Distanz(self.kFilter1[i], self.gTruth[i]))			
			self.kFilterY2.append(coord_Distanz(self.kFilter2[i], self.gTruth[i]))
			self.kFilterY3.append(coord_Distanz(self.kFilter3[i], self.gTruth[i]))
			self.kFilterY4.append(coord_Distanz(self.kFilter4[i], self.gTruth[i]))
			self.kalm_rad.set_data(self.measureX, self.measureY)

			if self.kalm1.get()==True:
				self.kalm_filt1.set_data(self.x_all , self.kFilterY1)		
			if self.kalm2.get()==True:
				self.kalm_filt2.set_data(self.x_all , self.kFilterY2)
			if self.kalm3.get()==True:
				self.kalm_filt3.set_data(self.x_all , self.kFilterY3)
			if self.kalm4.get()==True:
				self.kalm_filt4.set_data(self.x_all , self.kFilterY4)
			if self.multsen_kalm.get()==True:
				self.kalm_filt.set_data(self.x_all , self.kFilterY)			
			
			
			
			self.bx.set_xlim(i-50,i+50)
			self.bx.set_xlabel(i)   

			return self.scat2,self.pltsen1,self.pltsen2,self.pltsen3,self.pltsen4,self.pltsen5,self.multisen,self.kalm_filt,self.kalm_filt1,self.kalm_filt2,self.kalm_filt3,self.kalm_filt4,self.kalm_rad,self.ell1,self.ell2,self.ell3,self.ell4,self.ell_p
		


		self.master.title("Sensorfusion Kalman")
		self.pack(fill='both', expand=1)

		self.canvas = FigureCanvasTkAgg(self.fig, master=self)
		self.canvas.get_tk_widget().grid(column=3,row=6)



		self.ani = animation.FuncAnimation(self.fig, update, interval=100,blit=True)



root = tk.Tk()
app = Window(root)
tk.mainloop()

