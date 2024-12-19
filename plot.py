import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter


def PrintFucntion():
    # this is for plotting the annual load variation details
    data = pd.read_csv("Result_10.csv")
    x1 = data['Hours']
    x = data['Load_Level']
    #print(data)
    y1 = data['DG Power (kW)']
    y2 = data['Ploss (kW)']
  
    plt.figure(figsize=(12, 4))
    plt.subplot(2, 1, 1)
    y_pos = np.arange(len(x))
    #performance = [10,8,6,4,2,1]
    plt.bar(y_pos, y1, align='center', alpha=0.6, color='blue') # alpha=0.5
    plt.xlim(1, 96)
    plt.xticks([],[])
    #plt.xticks(y_pos, round(x, 2))
    plt.xticks(rotation=90)
    plt.ylabel('DG Power (kW)', fontweight='bold')
    plt.title('DG Power Injection for different load levels', fontweight='bold')
    #plt.title('Programming language usage')
    plt.subplot(2, 1, 2)
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y2, align='center', alpha = 0.6, color='red') # alpha=0.5
    plt.xlim(1, 96)
    plt.xticks(y_pos, round(x, 2))
    plt.xticks(rotation=90)
    plt.ylabel('Power loss(kW)', fontweight='bold')
    plt.xlabel('Normalized load levels', fontweight='bold')
    plt.title('Power loss incured at different load levels', fontweight='bold')
    plt.tight_layout()
    
    
    data = pd.read_csv("Result_30.csv")
    x1 = data['Hours']
    x = data['Load_Level']
    #print(data)
    y1 = data['DG Power (kW)']
    y2 = data['Ploss (kW)']
  
    plt.figure(figsize=(12, 4))
    plt.subplot(2, 1, 1)
    y_pos = np.arange(len(x))
    #performance = [10,8,6,4,2,1]
    plt.bar(y_pos, y1, align='center', alpha=0.6, color='blue') # alpha=0.5
    plt.xlim(1, 96)
    plt.xticks([],[])
    #plt.xticks(y_pos, round(x, 2))
    plt.xticks(rotation=90)
    plt.ylabel('DG Power (kW)', fontweight='bold')
    plt.title('DG Power Injection for different load levels', fontweight='bold')
    #plt.title('Programming language usage')
    plt.subplot(2, 1, 2)
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y2, align='center', alpha = 0.6, color='red') # alpha=0.5
    plt.xlim(1, 96)
    plt.xticks(y_pos, round(x, 2))
    plt.xticks(rotation=90)
    plt.ylabel('Power loss(kW)', fontweight='bold')
    plt.xlabel('Normalized load levels', fontweight='bold')
    plt.title('Power loss incured at different load levels', fontweight='bold')
    plt.tight_layout()
    
    
    data = pd.read_csv("Result_50.csv")
    x1 = data['Hours']
    x = data['Load_Level']
    #print(data)
    y1 = data['DG Power (kW)']
    y2 = data['Ploss (kW)']
  
    plt.figure(figsize=(12, 4))
    plt.subplot(2, 1, 1)
    y_pos = np.arange(len(x))
    #performance = [10,8,6,4,2,1]
    plt.bar(y_pos, y1, align='center', alpha=0.6, color='blue') # alpha=0.5
    plt.xlim(1, 96)
    plt.xticks([],[])
    #plt.xticks(y_pos, round(x, 2))
    plt.xticks(rotation=90)
    plt.ylabel('DG Power (kW)', fontweight='bold')
    plt.title('DG Power Injection for different load levels', fontweight='bold')
    #plt.title('Programming language usage')
    plt.subplot(2, 1, 2)
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y2, align='center', alpha = 0.6, color='red') # alpha=0.5
    plt.xlim(1, 96)
    plt.xticks(y_pos, round(x, 2))
    plt.xticks(rotation=90)
    plt.ylabel('Power loss(kW)', fontweight='bold')
    plt.xlabel('Normalized load levels', fontweight='bold')
    plt.title('Power loss incured at different load levels', fontweight='bold')
    plt.tight_layout()
    plt.show()
      
def PrintZerobus():
    # this is to plotting the variable power injection versus zero bus
    data = pd.read_csv("Bus33Zero_10_CP.csv")
    #print(data)
    x = data['ZeroBus Number']
    #print(x)
    y2 = data['RealPower Loss (kW)']
    #print(y2)
    y1 = data[' DG Real power(kW)']
    #print(y1)
    y3 = data[' Power Injection (kW)']
    #print(y3)
    plt.figure(figsize=(12, 4))
    plt.subplot(3, 1, 1)
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y1, align='center', alpha=0.6, color='blue') # alpha=0.5
    plt.xticks([],[])
    plt.xlim(0,33)
    #plt.xticks(y_pos, x)
    plt.ylim(3400, 4100) 
    #plt.xticks(rotation=90)
    plt.ylabel('DG Power (kW)', fontweight='bold')
    plt.title('DG Power Injection at zero bus', fontweight='bold')
    plt.subplot(3, 1, 2)
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y2, align='center', alpha = 0.6, color='red') # alpha=0.5
    plt.ylabel('Power loss (kW)', fontweight='bold')
    plt.xlim(0,33)
    plt.xticks([],[])
    plt.title('Power loss in kW', fontweight='bold')
    plt.subplot(3, 1, 3)
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y3, align='center', alpha = 0.6, color='green') # alpha=0.5
    plt.xticks(y_pos, x)
    plt.ylabel('10% of Peak Power drawn', fontweight='bold')
    plt.ylim(350, 400) 
    plt.xlim(0,33)
    #plt.xticks(y_pos, round(x, 2))
    #plt.xticks(rotation=90)
    plt.xlabel('Zero bus number', fontweight='bold')
    plt.title('Power Injection at Substation bus', fontweight='bold')
    #plt.tight_layout()
    #plt.show()
    
    
    data = pd.read_csv("Bus33Zero_30_CP.csv")
    #print(data)
    x = data['ZeroBus Number']
    #print(x)
    y2 = data['RealPower Loss (kW)']
    #print(y2)
    y1 = data[' DG Real power(kW)']
    #print(y1)
    y3 = data[' Power Injection (kW)']
    #print(y3)
    plt.figure(figsize=(12, 4))
    plt.subplot(3, 1, 1)
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y1, align='center', alpha=0.6, color='blue') # alpha=0.5
    plt.xticks([],[])
    plt.xlim(0,33)
    #plt.xticks(y_pos, x)
    plt.ylim(2500, 3000)  # plt.ylim(3250, 4000) 
    #plt.xticks(rotation=90)
    plt.ylabel('DG Power (kW)', fontweight='bold')
    plt.title('DG Power Injection at zero bus', fontweight='bold')
    plt.subplot(3, 1, 2)
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y2, align='center', alpha = 0.6, color='red') # alpha=0.5
    plt.ylabel('Power loss (kW)', fontweight='bold')
    plt.xlim(0,33)
    plt.xticks([],[])
    plt.title('Power loss in kW', fontweight='bold')
    plt.subplot(3, 1, 3)
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y3, align='center', alpha = 0.6, color='green') # alpha=0.5
    plt.xticks(y_pos, x)
    plt.ylabel('30% of Peak Power drawn', fontweight='bold')
    plt.ylim(1000, 1200)  # plt.ylim(350, 400) 
    plt.xlim(0,33)
    #plt.xticks(y_pos, round(x, 2))
    #plt.xticks(rotation=90)
    plt.xlabel('Zero bus number', fontweight='bold')
    plt.title('Power Injection at Substation bus', fontweight='bold')
    #plt.tight_layout()
    #plt.show()
    
    
    data = pd.read_csv("Bus33Zero_50_CP.csv")
    #print(data)
    x = data['ZeroBus Number']
    #print(x)
    y2 = data['RealPower Loss (kW)']
    #print(y2)
    y1 = data[' DG Real power(kW)']
    #print(y1)
    y3 = data[' Power Injection (kW)']
    #print(y3)
    plt.figure(figsize=(12, 4))
    plt.subplot(3, 1, 1)
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y1, align='center', alpha=0.6, color='blue') # alpha=0.5
    plt.xticks([],[])
    plt.xlim(0,33)
    #plt.xticks(y_pos, x)
    plt.ylim(1900, 2150)  
    #plt.xticks(rotation=90)
    plt.ylabel('DG Power (kW)', fontweight='bold')
    plt.title('DG Power Injection at zero bus', fontweight='bold')
    plt.subplot(3, 1, 2)
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y2, align='center', alpha = 0.6, color='red') # alpha=0.5
    plt.ylabel('Power loss (kW)', fontweight='bold')
    plt.xlim(0,33)
    plt.xticks([],[])
    plt.title('Power loss in kW', fontweight='bold')
    plt.subplot(3, 1, 3)
    y_pos = np.arange(len(x))
    plt.bar(y_pos, y3, align='center', alpha = 0.6, color='green') # alpha=0.5
    plt.xticks(y_pos, x)
    plt.ylabel('50% of Peak Power drawn', fontweight='bold')
    #plt.ylim(1850, 2100)
    plt.ylim(1800, 1950) 
    plt.xlim(0,33)
    #plt.xticks(y_pos, round(x, 2))
    #plt.xticks(rotation=90)
    plt.xlabel('Zero bus number', fontweight='bold')
    plt.title('Power Injection at Substation bus', fontweight='bold')
    #plt.tight_layout()
    plt.show()
    

def Voltageplot():
    data = pd.read_csv("VoltageComp.csv")
    X = data['Bus no.']
    #y1 = data['Constant Power']
    #y2 = data['Constant Current']
    #y3 = data['Constant Impedance']
    
    plt.figure(figsize=(12, 4))
    plt.bar(X + 0.00, data['Constant Power'], color = 'b', width = 0.25,  label='Constant Power')
    plt.bar(X + 0.25, data['Constant Current'], color = 'g', width = 0.25,  label='Constant Current')
    plt.bar(X + 0.50, data['Constant Impedance'], color = 'r', width = 0.25,  label='Constant Impedance')
    plt.xlim(1,34)
    plt.ylim(0.9120,1.001)
    plt.ylabel('Voltage in pu', fontweight='bold')
    plt.xlabel('Bus number', fontweight='bold')
    plt.legend()
    plt.show()

if __name__ == '__main__':
    #PrintFucntion()
    PrintZerobus()
    #Voltageplot()
    #plt.show()
