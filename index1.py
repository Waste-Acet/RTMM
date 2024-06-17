import streamlit as st
import datetime
import time
import pandas as pd
import numpy as np
from PIL import Image
#import plotly.graph_objects as go
#import plotly.express as px
import random
import base64

#from pymodbus.client import ModbusTcpClient
from streamlit_apexjs import st_apexcharts
#import matplotlib.pyplot as plt
from st_excel_table import Table


#SERVER_IP = '192.168.43.119'  # Replace with the IP address of your Modbus device
#SERVER_PORT = 502  # Default Modbus TCP port
#REGISTER_ADDRESS = 4000 # Replace with the starting address of your register
#NUM_REGISTERS = 15  

#client = ModbusTcpClient(SERVER_IP , port=SERVER_PORT)
st.set_page_config(page_title="Powder coating", page_icon="lls.png",layout="wide")

col1_row1, col2_row2 = st.columns((20,1))
# Title display
Title = '<p style = "font-family:Times New Roman; text-align: center; color:blue;font-size:48px;">LLS-POWDER COATING DEPARTMENT!</p>'
col1_row1.markdown(Title, unsafe_allow_html= True)

    # Logo display
original = Image.open('lls.png')
col2_row2.image(original)

data=[10,20,30,40,50,10,500,000,10,20,30,40,50,500,random.randrange(20,1000)]

def index1():
    #st.write("hello")
   # with open("style1.css", "r") as f:
      #  css = f.read()
       # st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
   # def read_modbus_registers(ip, port, address, num_registers): 
    #def register():
         # Connect to Modbus server
       # client = ModbusTcpClient(ip, port)
        #client.connect()
        # Read registers
   # def Data_out():
        #data=[10,20,30,40,50,10,0,1000,10,20,30,40,50]
            #response = client.read_holding_registers(address, num_registers, unit=1)
        # Check if the response is valid
            #if not response.isError():
               # data = response.registers
               # print("Data from Modbus registers:")
               # for i in range(num_registers):
                  #  print(f"Register {address + i}: {response.registers[i]}")
           # else:
              #  print("Error reading Modbus registers:", response)
            

        #return data

     

    #data=Data_out()

 
    
    
    col1_row2, col2_row2, col3_row2 = st.columns((1,1,1))
    Date = col1_row2.empty()
    Time = col2_row2.empty()
    Shift = col3_row2.empty()

        

    st.header("Machine Status")
    if(data[6]==500):
  
        st.write("M_OFF")
        rectangle_style = f"background-color: red ; width: 40px; height: 20px"
        st.markdown(f'<div style="{rectangle_style}"></div>', unsafe_allow_html=True)
       # print(f"Elapsed time: {hours} hours, {minutes} minutes, {seconds} seconds")
        t10=st.empty()

    elif(data[7]==1000):
            
        st.write("M_ON")
        rectangle_style1 = f"background-color: #008000 ; width: 40px; height: 20px"
        st.markdown(f'<div style="{rectangle_style1}"></div>', unsafe_allow_html=True)
       # print(f"Elapsed time: {hours} hours, {minutes} minutes, {seconds} seconds")
        t11=st.empty()

    else:
        st.write("machine power off State")

    st.header("Station Emergency")
    if(data[8]==10):
        st.write("Station_EMG_1_ON")
        rectangle_style = f"background-color: red ; width: 40px; height: 20px"
        st.markdown(f'<div style="{rectangle_style}"></div>', unsafe_allow_html=True)
    if(data[9]==20):
        st.write("Station_EMG_2_ON")
        rectangle_style = f"background-color: red ; width: 40px; height: 20px"
        st.markdown(f'<div style="{rectangle_style}"></div>', unsafe_allow_html=True)
    if(data[10]==30):
        st.write("Station_EMG_3_ON")
        rectangle_style = f"background-color: red ; width: 40px; height: 20px"
        st.markdown(f'<div style="{rectangle_style}"></div>', unsafe_allow_html=True)
    if(data[11]==40):
        st.write("Station_EMG_4_ON")
        rectangle_style = f"background-color: red ; width: 40px; height: 20px"
        st.markdown(f'<div style="{rectangle_style}"></div>', unsafe_allow_html=True)
    if(data[12]==50):
        st.write("Station_EMG_5_ON")
        rectangle_style = f"background-color: red ; width: 40px; height: 20px"
        st.markdown(f'<div style="{rectangle_style}"></div>', unsafe_allow_html=True)
    if(data[8]!=10 and data[9]!=20 and data[10]!=30 and data[11]!=40 and data[12]!=50):
        st.write("NO_EMG_PRESSED")

        #client.close()




    st.write("data_1_value:")
    t1=st.empty()
       # col1, col2 = st.columns(2)
    st.write("data_2_value:")
    t2=st.empty()
    st.write("data_3_value:")
    t3=st.empty()
    t4=st.empty()
    t5=st.empty()
    t6=st.empty()
    t7=st.empty()

        #timer plc to python
    #elapsed_seconds = data[13]
   # hours = int(elapsed_seconds // 3600)
   # elapsed_seconds %= 3600
    #minutes = int(elapsed_seconds // 60)
    #seconds = int(elapsed_seconds % 60)
    #Timer=[hours, minutes, seconds]

    
   # is_running = False


    while True:
        #data=[10,20,30,40,50,10,500,000,10,20,30,40,50,500,random.randrange(20,1000)]
        now = datetime.datetime.now()
        Today_Date = now.strftime("%d-%m-%Y")
        Current_Time = now.strftime("%H:%M:%S")
        Hour = now.strftime("%H")
        Min = now.strftime("%M")
    #print(type(Hour))
        Hours_and_Min = int(Hour + Min)
    #print(Hours_and_Min)

        Date_text = f'<p style = "font-family:Times New Roman; text-align: center; color:#FF5733;font-size:20px;">DATE: {Today_Date}</p>'
        Date.markdown(Date_text, unsafe_allow_html= True)
    
    #Date.write(f"DATE : {Today_Date}")
        Time_Text = f'<p style = "font-family:Times New Roman; text-align: center; color:#FF5733;font-size:20px;">TIME: {Current_Time}</p>'
        Time.markdown(Time_Text, unsafe_allow_html= True)
    
    #Time.write(f"TIME : {Current_Time}")
        if Hours_and_Min in range(100,800):
            Shift_Text = '<p style = "font-family:Times New Roman; text-align: center; color:#FF5733;font-size:20px;">SHIFT : A</p>'
            Shift.markdown(Shift_Text, unsafe_allow_html= True)
        #Shift.write("SHIFT : A")
        elif Hours_and_Min in range(801,1630):
            Shift_Text = '<p style = "font-family:Times New Roman; text-align: center; color:#FF5733;font-size:20px;">SHIFT : B</p>'
            Shift.markdown(Shift_Text, unsafe_allow_html= True)
        #Shift.write("SHIFT : B")
        #print("SHIFT : B")
        else:
            Shift_Text = '<p style = "font-family:Times New Roman; text-align: center; color:#FF5733;font-size:20px;">SHIFT : C</p>'
            Shift.markdown(Shift_Text, unsafe_allow_html= True)
        #Shift.write("SHIFT : C")

        elapsed_seconds1 = data[14]
        hours1 = int(elapsed_seconds1 // 3600)
        elapsed_seconds1 %= 3600
        minutes1 = int(elapsed_seconds1 // 60)
        seconds1 = int(elapsed_seconds1 % 60)
        Timer1=[hours1, minutes1, seconds1]


        elapsed_seconds2 = data[14]
        hours2 = int(elapsed_seconds2 // 3600)
        elapsed_seconds2 %= 3600
        minutes2 = int(elapsed_seconds2 // 60)
        seconds2 = int(elapsed_seconds2 % 60)
        Timer2=[hours2, minutes2, seconds2]


        if (data[6]==500):
           # timer.start()
           # is_running = True
            t10.markdown(f"Elapsed time1: {hours1}:{minutes1}:{seconds1}")
            
        elif (data[7]==1000):
            #timer.stop()
            #is_running = False
            #hours, minutes, seconds = timer.elapsed_time()
            t11.markdown(f"Elapsed time2:{hours2}:{minutes2}:{seconds2}")
            


        t1.markdown(data[0])
        t2.markdown(data[1])
        t3.text(data[2])
        t4.markdown(data[3])
        t5.markdown(data[4])
        t6.markdown(data[5])
        t7.markdown(data[6])

       # data=Data_out()
        time.sleep(1)

   # read_modbus_registers(SERVER_IP, SERVER_PORT, REGISTER_ADDRESS, NUM_REGISTERS)

if __name__ == "__main__":
    index1()
