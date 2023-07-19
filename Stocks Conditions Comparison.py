import talib
import tkinter as tk
from tkinter import ttk
import talib.abstract as ta
import time
import datetime
import pandas as pd
import numpy as np

window = tk.Tk()
window.title("Program")
window.geometry("1200x1000")



flag_algoStarted = 0
prev_close = {}
prev_high = {}
prev_open = {}
prev_low = {}
hist_data = {}
sample_data = {}
sample_data_copy = {}

A_input_values = []
A_dict = {}
indexA = {}
A_result = {}

B_input_values = []
B_result = {}
indexB = {}
B_dict = {}

flag_compare = {}


flag_condition = 0
Aentry = None
Bentry = None
flag = 0
A_arg_flag2 = 0
B_arg_flag2= 0
A_arg_list2 = []
A_input_values2 = []
B_arg_list2 = []
B_input_values2 = []
Return = {}


A_all_result = {}
B_all_result = {}
flag_all_compare = {}


condition={}
A_subInd = {}
B_subInd = {}
A_Ind = {}
B_Ind = {}


tk.Label(window, text="Enter Time Period:").grid(row=0, column=6)
tk.Label(window, text="Time Period:").grid(row=1, column=6)
tf_input = tk.Entry(window)
tf_input.grid(row=1, column=7)



def scan():

    def ok():
        global flag_condition
        global flag, Return, AIndex,BIndex
        global A_parameters2, A_arg_flag2, A_Indicator2, A_arg_list2, A_subIndicator2, A_Indicator2, A_input_names2, A_output_names2, A_Function_Group2
        global B_parameters2, B_arg_flag2, B_Indicator2, B_arg_list2, B_subIndicator2, B_Indicator2, B_input_names2, B_output_names2, B_Function_Group2
        global condition2, new_flag, new_flag2
        global flag_condition, A_arg_list2, B_arg_list2 
        if len(A_Function_Group2.get())!=0 and len(A_Indicator2.get())!=0 and len(B_Function_Group2.get())!=0 and len(B_Indicator2.get())!=0:
            if A_subIndicator2['state'] == 'disabled' and B_subIndicator2['state'] == 'disabled':
                single_Condition ={flag-1 : {"A": {"AIndex":AIndex,"A_Function_Group2":A_Function_Group2,"A_parameters":A_parameters2, "new_flag":new_flag, "A_Indicator":A_Indicator2, "A_arg_list": A_arg_list2, "A_subIndicator":None, "A_Indicator": A_Indicator2, "A_input_names":A_input_names2, "A_output_names":A_output_names2}, "B":{"BIndex":BIndex,"B_Function_Group2":B_Function_Group2,"B_parameters":B_parameters2, "new_flag2":new_flag2, "B_Indicator":B_Indicator2, "B_arg_list":B_arg_list2, "B_subIndicator":None, "B_Indicator":B_Indicator2, "B_input_names":B_input_names2, "B_output_names":B_output_names2}, "condition": condition2}}
                Return.update(single_Condition)
            elif A_subIndicator2['state'] == 'disabled':
                single_Condition ={flag-1 : {"A": {"AIndex":AIndex,"A_Function_Group2":A_Function_Group2,"A_parameters":A_parameters2, "new_flag":new_flag, "A_Indicator":A_Indicator2, "A_arg_list": A_arg_list2, "A_subIndicator":None, "A_Indicator": A_Indicator2, "A_input_names":A_input_names2, "A_output_names":A_output_names2}, "B":{"BIndex":BIndex,"B_Function_Group2":B_Function_Group2,"B_parameters":B_parameters2, "new_flag2":new_flag2, "B_Indicator":B_Indicator2, "B_arg_list":B_arg_list2, "B_subIndicator":B_subIndicator2, "B_Indicator":B_Indicator2, "B_input_names":B_input_names2, "B_output_names":B_output_names2}, "condition": condition2}}
                Return.update(single_Condition)
            elif B_subIndicator2['state'] == 'disabled':
                single_Condition ={flag-1 : {"A": {"AIndex":AIndex,"A_Function_Group2":A_Function_Group2,"A_parameters":A_parameters2, "new_flag":new_flag, "A_Indicator":A_Indicator2, "A_arg_list": A_arg_list2, "A_subIndicator":A_subIndicator2, "A_Indicator": A_Indicator2, "A_input_names":A_input_names2, "A_output_names":A_output_names2}, "B":{"BIndex":BIndex,"B_Function_Group2":B_Function_Group2,"B_parameters":B_parameters2, "new_flag2":new_flag2, "B_Indicator":B_Indicator2, "B_arg_list":B_arg_list2, "B_subIndicator":None, "B_Indicator":B_Indicator2, "B_input_names":B_input_names2, "B_output_names":B_output_names2}, "condition": condition2}}
                Return.update(single_Condition)
            else:
                single_Condition ={flag-1 : {"A": {"AIndex":AIndex,"A_Function_Group2":A_Function_Group2,"A_parameters":A_parameters2, "new_flag":new_flag, "A_Indicator":A_Indicator2, "A_arg_list": A_arg_list2, "A_subIndicator":A_subIndicator2, "A_Indicator": A_Indicator2, "A_input_names":A_input_names2, "A_output_names":A_output_names2}, "B":{"BIndex":BIndex,"B_Function_Group2":B_Function_Group2,"B_parameters":B_parameters2, "new_flag2":new_flag2, "B_Indicator":B_Indicator2, "B_arg_list":B_arg_list2, "B_subIndicator":B_subIndicator2, "B_Indicator":B_Indicator2, "B_input_names":B_input_names2, "B_output_names":B_output_names2}, "condition": condition2}}
                Return.update(single_Condition)
            add_condition_button['state'] = 'active'
            A_arg_list2 = []
            B_arg_list2 = []
        else:
            add_condition_button['state'] = 'disabled'

        flag_condition = max(int(A_subIndicator2.grid_info()["row"]) + 1, int(B_subIndicator2.grid_info()["row"]) + 1)

    ok()


    print("----------!!!!!!!!!!----------------------")
    global flag_algoStarted
    global tf, radio_var
    global prev_close, prev_high, prev_open, prev_low
    global Return, condition, A_subInd, B_subInd, A_Ind, B_Ind, new_flag, new_flag2, numberA, numberB, price

    for j in range(len(Return)):
        if Return[j]["A"]["A_Function_Group2"].get() == "Number":

            if Return[j]["A"]["A_Indicator"].get() == "Number":
                entry_widget = window.grid_slaves(row=int(Return[j]["A"]["A_Indicator"].grid_info()["row"]) + 1, column=1)[0]
                numberA = int(entry_widget.get())
            else:
                price = str(Return[j]["A"]["A_subIndicator"].get())
                entry_widget = window.grid_slaves(row=int(Return[j]["A"]["A_Indicator"].grid_info()["row"]) + 1, column=1)[0]
                indexA[j] = int(entry_widget.get())

        elif len(Return[j]["A"]["A_parameters"]) != 0:

            A_input_values.append([])
            for i in range(0,Return[j]["A"]["new_flag"]-1):
                if Return[j]["A"]["AIndex"] != None:
                    indexA[j] = int(Return[j]["A"]["AIndex"].get())

                entry_widget = window.grid_slaves(row=int(Return[j]["A"]["A_Indicator"].grid_info()["row"]) + 1+i, column=1)[0]
                value = entry_widget.get()
                A_input_values[j].append(value)
                
            A_dict[j] = {Return[j]["A"]["A_arg_list"][i] : A_input_values[j][i] for i in range(0,len(A_input_values[j]))}
        else:
            A_input_values.append([])
            A_dict[j] = {}
            if Return[j]["A"]["AIndex"] != None:
                entry_widget = window.grid_slaves(row=int(Return[j]["A"]["A_Indicator"].grid_info()["row"]) + 1, column=1)[0]
                indexA[j] = int(entry_widget.get())




        if Return[j]["B"]["B_Function_Group2"].get() == "Number":

            if Return[j]["B"]["B_Indicator"].get() == "Number":
                entry_widget = window.grid_slaves(row=int(Return[j]["B"]["B_Indicator"].grid_info()["row"]) + 1, column=3)[0]
                numberB = int(entry_widget.get())
            else:
                price = str(Return[j]["B"]["B_subIndicator"].get())
                entry_widget = window.grid_slaves(row=int(Return[j]["B"]["B_Indicator"].grid_info()["row"]) + 1, column=3)[0]
                indexB[j] = int(entry_widget.get())

        elif len(Return[j]["B"]["B_parameters"]) != 0:
            B_input_values.append([])
            for i in range(0,Return[j]["B"]["new_flag2"]-1):
                if Return[j]["B"]["new_flag2"] != None:
                    # entry_widget = window.grid_slaves(row=int(Return[j]["B"]["B_Indicator"].grid_info()["row"]) + 1+i, column=3)[0]
                    # indexB[j] = int(entry_widget.get())
                    indexB[j] = int(Return[j]["B"]["BIndex"].get())

                entry_widget = window.grid_slaves(row=int(Return[j]["B"]["B_Indicator"].grid_info()["row"]) + 1+i, column=3)[0]
                value = entry_widget.get()
                B_input_values[j].append(value)
                
            B_dict[j] = {Return[j]["B"]["B_arg_list"][i] : B_input_values[j][i] for i in range(0,len(B_input_values[j]))}
        else:
            B_input_values.append([])
            B_dict[j] = {}
            if Return[j]["B"]["new_flag2"] != None:
                entry_widget = window.grid_slaves(row=int(Return[j]["B"]["B_Indicator"].grid_info()["row"]) + 1, column=3)[0]
                indexB[j] = int(entry_widget.get())



    tf = int(tf_input.get())
    radio_var = int(radio_var.get())

    for j in range(len(Return)):
        condition[j] = str(Return[j]["condition"].get())
        A_subInd[j] = str(Return[j]["A"]["A_subIndicator"].get())
        B_subInd[j] = str(Return[j]["B"]["B_subIndicator"].get())
        A_Ind[j] = str(Return[j]["A"]["A_Indicator"].get())
        B_Ind[j] = str(Return[j]["B"]["B_Indicator"].get())

    flag_algoStarted = 1
    print("Algorithm started.")




def calculate(open, high, low, close, input_names, parameters, Dict, Ind, output_names, subInd, index):
    global price_dict
    
    input_values = []
    price_dict = {"open":np.array(open), "high": np.array(high), "low": np.array(low), "close": np.array(close)}
    
    if type(list(input_names.values())[0]) == type("abc"):
        for i in range(len(list(input_names.values()))):
            input_values.append(price_dict[list(input_names.values())[i]])
    else:
        for i in range(len(list(input_names.values())[0])):
            input_values.append(price_dict[list(input_names.values())[0][i]])
    
    
    if len(parameters) != 0:
        for i in range(len(Dict)):
            input_values.append(float(list(Dict.values())[i]))
        

    selected_function = Ind

    if len(output_names) == 1 : 
        if selected_function in talib.__dict__:
            function_object = talib.__dict__[selected_function]
            if callable(function_object):
                result = function_object(*input_values)
            else:
                print("Selected function is not callable")
        else:
            print("Selected function is not valid")
        
    else:
        if selected_function in talib.__dict__:
            function_object = talib.__dict__[selected_function]
            if callable(function_object):
                output = function_object(*input_values)
                subInd_dict = {output_names[i] : output[i] for i in range(len(output_names))}
            else:
                print("Selected function is not callable")
        else:
            print("Selected function is not valid")
        result = subInd_dict[subInd]

    return result[-(index)]



def compare_results(result_A, result_B,condition):

    newoperator = {
    '>': lambda a, b: a > b,
    '<': lambda a, b: a < b,
    '>=': lambda a, b: a >= b,
    '<=': lambda a, b: a <= b,
    '==': lambda a, b: a == b,
    '!=': lambda a, b: a != b
    }
    operator = newoperator[condition]
    result = operator(result_A, result_B)
    return result



    

def mainloop():
    
    global main_data, hist_data, sample_data, symbol_list
    global flag_algoStarted
    global tf, condition, A_Ind, B_Ind, A_dict, B_dict
    global prev_close, prev_high, prev_open, prev_low
    global Return, condition, A_subInd, B_subInd, A_Ind, B_Ind, numberA, numberB, price
    stock_list = {}
    final_list = []

    main_data = pd.read_csv("HistoricalData/Merged.csv")
    symbol_list = main_data.Symbol.unique()

    for symbol in symbol_list:
        prev_close[symbol]=[]
        prev_high[symbol]=[]
        prev_low[symbol]=[]
        prev_open[symbol]=[]
        hist_data[symbol]=0
        sample_data[symbol]=0
        A_result[symbol] = []
        B_result[symbol] = []
        sample_data_copy[symbol] = 0
  
    
    if(flag_algoStarted == 1):

        for symbol in symbol_list:
            sample_data[symbol] = main_data.loc[main_data['Symbol'] == symbol]
            

            sample_data_copy[symbol] = sample_data[symbol].copy()
            sample_data_copy[symbol]['Datetime'] = pd.to_datetime(sample_data_copy[symbol]['Datetime'], format='%Y-%m-%d %H:%M:%S%z')
            sample_data_copy[symbol].set_index('Datetime', inplace=True)


            hist_data[symbol] = sample_data_copy[symbol].resample(f'{tf}T').interpolate()

            prev_close[symbol] = hist_data[symbol]['Close'].tolist()   
            prev_high[symbol] = hist_data[symbol]['High'].tolist()    
            prev_open[symbol] = hist_data[symbol]['Open'].tolist()       
            prev_low[symbol] = hist_data[symbol]['Low'].tolist()


            for j in range(len(Return)):

                if Return[j]["A"]["A_Function_Group2"].get() != "Number":
                    A_result[symbol] = calculate(prev_open[symbol], prev_high[symbol], prev_low[symbol], prev_close[symbol],Return[j]["A"]["A_input_names"] , Return[j]["A"]["A_parameters"], A_dict[j], A_Ind[j], Return[j]["A"]["A_output_names"], A_subInd[j], indexA[j])
                else:
                    if Return[j]["A"]["A_Indicator"].get() == "Number":
                        A_result[symbol] = numberA
                    else:
                        if price == "Open":
                            A_result[symbol] = prev_open[symbol][-(indexB[j])]
                        elif price == "High":
                            A_result[symbol] = prev_high[symbol][-(indexB[j])]
                        elif price == "Low":
                            A_result[symbol] = prev_low[symbol][-(indexB[j])]
                        else:
                            A_result[symbol] = prev_close[symbol][-(indexB[j])]


                if Return[j]["B"]["B_Function_Group2"].get() != "Number":
                    B_result[symbol] = calculate(prev_open[symbol], prev_high[symbol], prev_low[symbol], prev_close[symbol], Return[j]["B"]["B_input_names"], Return[j]["B"]["B_parameters"], B_dict[j], B_Ind[j], Return[j]["B"]["B_output_names"], B_subInd[j], indexB[j])
                else:
                    if Return[j]["B"]["B_Indicator"].get() == "Number":
                        B_result[symbol] = numberB
                    else:
                        if price == "Open":
                            B_result[symbol] = prev_open[symbol][-(indexB[j])]
                        elif price == "High":
                            B_result[symbol] = prev_high[symbol][-(indexB[j])]
                        elif price == "Low":
                            B_result[symbol] = prev_low[symbol][-(indexB[j])]
                        else:
                            B_result[symbol] = prev_close[symbol][-(indexB[j])]
                            

                A_all_result[j] = A_result
                B_all_result[j] = B_result
                flag_compare[symbol] = compare_results(A_all_result[j][symbol], B_all_result[j][symbol],condition[j])

                flag_all_compare[j] = flag_compare


                if flag_all_compare[j][symbol] == 1:
                    if j not in stock_list:
                        stock_list[j] = []
                    stock_list[j].append(symbol)
                else:
                    if j not in stock_list:
                        stock_list[j] = []

        for j in range(len(Return)):
            print("A_all_result[j]: ",A_all_result[j])
            # print("B_all_result[j]: ",B_all_result[j])
            # print("A_all_result[j]: ",A_all_result[j])
            # print("A_all_result[j]: ",A_all_result[j])


        if radio_var == 1:
            for i in range(len(Return)):
                for j in stock_list[i] : 
                    if j not in final_list:
                        final_list.extend([j])
        else:
            final_list = stock_list[0]
            for i in range(len(Return)):
                temp_list = []
                for item in final_list:
                    if item in stock_list[i]:
                        temp_list.append(item)
                final_list = temp_list


        print("Final List : ",final_list)
        # for i in final_list:
        #     print(i,"-----",A_all_result[0][i])
        #     print(i,"-----",A_all_result[1][i])

        exit(0)

        time.sleep(0.1)
    
    window.after(100, mainloop)




def add_condition():

    global flag_condition
    global flag, Return
    global A_parameters2, A_arg_flag2, A_Indicator2, A_arg_list2, A_subIndicator2, A_Indicator2, A_input_names2, A_output_names2, A_Function_Group2
    global B_parameters2, B_arg_flag2, B_Indicator2, B_arg_list2, B_subIndicator2, B_Indicator2, B_input_names2, B_output_names2, B_Function_Group2
    global condition2, new_flag, new_flag2, AIndex, BIndex


    if flag!=0:
        def ok():
            global flag_condition
            global flag, Return, AIndex,BIndex
            global A_parameters2, A_arg_flag2, A_Indicator2, A_arg_list2, A_subIndicator2, A_Indicator2, A_input_names2, A_output_names2, A_Function_Group2
            global B_parameters2, B_arg_flag2, B_Indicator2, B_arg_list2, B_subIndicator2, B_Indicator2, B_input_names2, B_output_names2, B_Function_Group2
            global condition2, new_flag, new_flag2
            global flag_condition, A_arg_list2, B_arg_list2 
            if len(A_Function_Group2.get())!=0 and len(A_Indicator2.get())!=0 and len(B_Function_Group2.get())!=0 and len(B_Indicator2.get())!=0:
                if A_subIndicator2['state'] == 'disabled' and B_subIndicator2['state'] == 'disabled':
                    single_Condition ={flag-1 : {"A": {"AIndex":AIndex,"A_Function_Group2":A_Function_Group2,"A_parameters":A_parameters2, "new_flag":new_flag, "A_Indicator":A_Indicator2, "A_arg_list": A_arg_list2, "A_subIndicator":None, "A_Indicator": A_Indicator2, "A_input_names":A_input_names2, "A_output_names":A_output_names2}, "B":{"BIndex":BIndex,"B_Function_Group2":B_Function_Group2,"B_parameters":B_parameters2, "new_flag2":new_flag2, "B_Indicator":B_Indicator2, "B_arg_list":B_arg_list2, "B_subIndicator":None, "B_Indicator":B_Indicator2, "B_input_names":B_input_names2, "B_output_names":B_output_names2}, "condition": condition2}}
                    Return.update(single_Condition)
                elif A_subIndicator2['state'] == 'disabled':
                    single_Condition ={flag-1 : {"A": {"AIndex":AIndex,"A_Function_Group2":A_Function_Group2,"A_parameters":A_parameters2, "new_flag":new_flag, "A_Indicator":A_Indicator2, "A_arg_list": A_arg_list2, "A_subIndicator":None, "A_Indicator": A_Indicator2, "A_input_names":A_input_names2, "A_output_names":A_output_names2}, "B":{"BIndex":BIndex,"B_Function_Group2":B_Function_Group2,"B_parameters":B_parameters2, "new_flag2":new_flag2, "B_Indicator":B_Indicator2, "B_arg_list":B_arg_list2, "B_subIndicator":B_subIndicator2, "B_Indicator":B_Indicator2, "B_input_names":B_input_names2, "B_output_names":B_output_names2}, "condition": condition2}}
                    Return.update(single_Condition)
                elif B_subIndicator2['state'] == 'disabled':
                    single_Condition ={flag-1 : {"A": {"AIndex":AIndex,"A_Function_Group2":A_Function_Group2,"A_parameters":A_parameters2, "new_flag":new_flag, "A_Indicator":A_Indicator2, "A_arg_list": A_arg_list2, "A_subIndicator":A_subIndicator2, "A_Indicator": A_Indicator2, "A_input_names":A_input_names2, "A_output_names":A_output_names2}, "B":{"BIndex":BIndex,"B_Function_Group2":B_Function_Group2,"B_parameters":B_parameters2, "new_flag2":new_flag2, "B_Indicator":B_Indicator2, "B_arg_list":B_arg_list2, "B_subIndicator":None, "B_Indicator":B_Indicator2, "B_input_names":B_input_names2, "B_output_names":B_output_names2}, "condition": condition2}}
                    Return.update(single_Condition)
                else:
                    single_Condition ={flag-1 : {"A": {"AIndex":AIndex,"A_Function_Group2":A_Function_Group2,"A_parameters":A_parameters2, "new_flag":new_flag, "A_Indicator":A_Indicator2, "A_arg_list": A_arg_list2, "A_subIndicator":A_subIndicator2, "A_Indicator": A_Indicator2, "A_input_names":A_input_names2, "A_output_names":A_output_names2}, "B":{"BIndex":BIndex,"B_Function_Group2":B_Function_Group2,"B_parameters":B_parameters2, "new_flag2":new_flag2, "B_Indicator":B_Indicator2, "B_arg_list":B_arg_list2, "B_subIndicator":B_subIndicator2, "B_Indicator":B_Indicator2, "B_input_names":B_input_names2, "B_output_names":B_output_names2}, "condition": condition2}}
                    Return.update(single_Condition)
                add_condition_button['state'] = 'active'
                A_arg_list2 = []
                B_arg_list2 = []
            else:
                add_condition_button['state'] = 'disabled'

            flag_condition = max(int(A_subIndicator2.grid_info()["row"]) + 1, int(B_subIndicator2.grid_info()["row"]) + 1)

        ok()

    flag = flag+1


    conditions2 = ['>', '<', '>=', '<=', '=', '!=']
    selected_condition2 = tk.StringVar()
    tk.Label(window, text="Select a Condition:").grid(row=flag_condition, column=4)
    tk.Label(window, text="Condition:").grid(row=flag_condition+1, column=4)
    condition2 = ttk.Combobox(window, textvariable=selected_condition2, values=conditions2)
    condition2.grid(row=flag_condition+1, column=5)


    indicator_groups2 = talib.get_function_groups()

    def A_drop1_select2(event):
        global A_parameters2, A_arg_flag2, A_Indicator2, A_arg_list2, A_subIndicator2, A_Indicator2, A_input_names2, A_output_names2
        selected_value2A = A_Function_Group2.get()

        A_Indicator2.set('')
        A_Indicator2['values'] = ()
        
        if selected_value2A in indicator_groups2:
            A_Indicator2['values'] = indicator_groups2[selected_value2A]
        
        elif selected_value2A == "Number":
            A_Indicator2['values'] = ["Number","OHLC"]
            A_parameters2 = None
            A_arg_list2 = None
            A_input_names2 = None
            A_output_names2 = None
        
        A_Indicator2['state'] = 'readonly'


    def A_drop2_select2(event):
        global Aentry, new_flag, AIndex
        global A_parameters2, A_arg_flag2, A_Indicator2, A_arg_list2, A_subIndicator2, A_Indicator2, A_input_names2, A_output_names2

        A_selected_value2 = A_Indicator2.get()

        print(A_selected_value2)

        if A_selected_value2 == "OHLC":
            for widget in window.grid_slaves():
                if int(widget.grid_info()["row"]) >= int(A_Indicator2.grid_info()["row"])+1  and int(widget.grid_info()["row"]) <= int(A_subIndicator2.grid_info()["row"])-1    and int(widget.grid_info()["column"]) in [0,1]:
                    widget.grid_forget()
            A_subIndicator2.set('')
            A_subIndicator2['values'] = ["Open","High","Low","Close"]
            A_subIndicator2['state'] = 'readonly'

            label = ttk.Label(window, text="Index: ")
            label.grid(row=int(A_Indicator2.grid_info()["row"]) + 1, column=0)
            AIndex = ttk.Entry(window)
            AIndex.grid(row=int(A_Indicator2.grid_info()["row"]) + 1, column=1)

            A_arg_flag2 = 0
            new_flag = 1
            Label.grid(row=int(A_Indicator2.grid_info()["row"])+1+1, column=0)
            A_subIndicator2.grid(row=int(A_Indicator2.grid_info()["row"])+1+1, column=1)

        elif A_selected_value2 == "Number":
            for widget in window.grid_slaves():
                if int(widget.grid_info()["row"]) >= int(A_Indicator2.grid_info()["row"])+1  and int(widget.grid_info()["row"]) <= int(A_subIndicator2.grid_info()["row"])-1    and int(widget.grid_info()["column"]) in [0,1]:
                    widget.grid_forget()
            A_subIndicator2.set('')
            A_subIndicator2['values'] = ()
            A_subIndicator2['state'] = 'disabled'

            label = ttk.Label(window, text="Value: ")
            label.grid(row=int(A_Indicator2.grid_info()["row"]) + 1, column=0)
            Aentry = ttk.Entry(window)
            Aentry.grid(row=int(A_Indicator2.grid_info()["row"]) + 1, column=1)

            A_arg_flag2 = 0
            new_flag = 1
            Label.grid(row=int(A_Indicator2.grid_info()["row"])+1+1, column=0)
            A_subIndicator2.grid(row=int(A_Indicator2.grid_info()["row"])+1+1, column=1)
        
        else:
            A_indicator_info2 = ta.Function(A_selected_value2).info

            print(A_indicator_info2)

            A_input_names2 = A_indicator_info2['input_names']
            A_parameters2 = A_indicator_info2['parameters']
            A_output_names2 = A_indicator_info2['output_names']
            A_num_arguments2 = len(A_parameters2) + 1


            for widget in window.grid_slaves():
                if int(widget.grid_info()["row"]) >= int(A_Indicator2.grid_info()["row"])+1  and int(widget.grid_info()["row"]) <= int(A_subIndicator2.grid_info()["row"])-1    and int(widget.grid_info()["column"]) in [0,1]:
                    widget.grid_forget()

            print("--------------------------------")
            print(A_parameters2)
            print("--------------------------------")
            print(list(A_parameters2.keys()))
            print("--------------------------------")
            print(A_output_names2)
            print("--------------------------------")
            print(f"The indicator '{A_selected_value2}' requires {A_num_arguments2} arguments.")
            print("--------------------------------")


            if len(A_parameters2) != 0:
                for i in range(0,len(A_parameters2)):
                    label = ttk.Label(window, text=list(A_parameters2.keys())[i])
                    label.grid(row=int(A_Indicator2.grid_info()["row"]) + 1+i, column=0)
                    Aentry = ttk.Entry(window)
                    Aentry.grid(row=int(A_Indicator2.grid_info()["row"]) + 1+i, column=1)
                    A_arg_list2.append(list(A_parameters2.keys())[i])
                    print(A_arg_list2)
                    if i == len(A_parameters2)-1:
                        A_arg_flag2 = i
                        new_flag = i+1
                        Label.grid(row=int(A_Indicator2.grid_info()["row"])+1+A_arg_flag2 +1, column=0)
                        A_subIndicator2.grid(row=int(A_Indicator2.grid_info()["row"])+1 +A_arg_flag2 +1, column=1)

                if len(A_input_names2) != 0:
                    label = ttk.Label(window, text="Index: ")
                    label.grid(row=int(A_Indicator2.grid_info()["row"])+ 1 + A_arg_flag2 + 1, column=0)
                    AIndex = ttk.Entry(window)
                    AIndex.grid(row=int(A_Indicator2.grid_info()["row"])+ 1 + A_arg_flag2 + 1, column=1)
                    A_arg_flag2 = A_arg_flag2+1
                    new_flag = new_flag +1
                    Label.grid(row=int(A_Indicator2.grid_info()["row"])+1+A_arg_flag2 +1, column=0)
                    A_subIndicator2.grid(row=int(A_Indicator2.grid_info()["row"])+1 +A_arg_flag2 +1, column=1)
                else:
                    AIndex = None
            
            else:
                if len(A_input_names2) != 0:
                    label = ttk.Label(window, text="Index: ")
                    label.grid(row=int(A_Indicator2.grid_info()["row"])+ 1, column=0)
                    AIndex = ttk.Entry(window)
                    AIndex.grid(row=int(A_Indicator2.grid_info()["row"])+ 1, column=1)
                    A_arg_flag2 = 1
                    new_flag = 2
                    Label.grid(row=int(A_Indicator2.grid_info()["row"])+1+1, column=0)
                    A_subIndicator2.grid(row=int(A_Indicator2.grid_info()["row"])+1 +1, column=1)
                
                else:
                    A_arg_flag2 = 0
                    new_flag = 0
                    Label.grid(row=int(A_Indicator2.grid_info()["row"])+1, column=0)
                    A_subIndicator2.grid(row=int(A_Indicator2.grid_info()["row"])+1, column=1)
                    AIndex = None

            
            


            A_subIndicator2.set('')
            A_subIndicator2['values'] = ()
            if len(A_output_names2) > 1:
                A_subIndicator2['values'] = A_output_names2
                A_subIndicator2['state'] = 'readonly'
            else:
                A_subIndicator2['state'] = 'disabled'



    def A_drop3_select2(event):
        global A_parameters2, A_arg_flag2, A_Indicator2, A_arg_list2, A_subIndicator2, A_Indicator2, A_input_names2, A_output_names2
        global Aentry
        A2_selected_value2 = A_Indicator2.get()

        print(A2_selected_value2)

                

    tk.Label(window, text="Enter values for A:").grid(row=flag_condition, column=0)
    tk.Label(window, text="Function Group:").grid(row=flag_condition+1, column=0)
    A_Function_Group2 = ttk.Combobox(window, state='readonly')
    A_Function_Group2.grid(row=flag_condition+1, column=1)
    listA = list(indicator_groups2.keys())
    listA.append("Number")
    A_Function_Group2['values'] = listA
    A_Function_Group2.bind('<<ComboboxSelected>>', A_drop1_select2)

    tk.Label(window, text="Indicator:").grid(row=int(A_Function_Group2.grid_info()["row"]) + 1, column=0)
    A_Indicator2 = ttk.Combobox(window, state='disabled')
    A_Indicator2.grid(row=int(A_Function_Group2.grid_info()["row"]) + 1, column=1)
    A_Indicator2.bind('<<ComboboxSelected>>', A_drop2_select2)


    Label = tk.Label(window, text="Sub Indicator:")
    Label.grid(row=int(A_Indicator2.grid_info()["row"]) +1, column=0)
    A_subIndicator2 = ttk.Combobox(window, state='disabled')
    A_subIndicator2.grid(row=int(A_Indicator2.grid_info()["row"]) +1, column=1)
    A_subIndicator2.bind('<<ComboboxSelected>>', A_drop3_select2)


    def B_drop1_select2(event):
        global B_parameters2, B_arg_flag2, B_Indicator2, B_arg_list2, B_subIndicator2, B_Indicator2, B_input_names2, B_output_names2
        selected_value2B = B_Function_Group2.get()

        B_Indicator2.set('')
        B_Indicator2['values'] = ()
        
        if selected_value2B in indicator_groups2:
            B_Indicator2['values'] = indicator_groups2[selected_value2B]
        
        elif selected_value2B == "Number":
            B_Indicator2['values'] = ["Number","OHLC"]
            B_parameters2 = None
            B_arg_list2 = None
            B_input_names2 = None
            B_output_names2 = None

        B_Indicator2['state'] = 'readonly'


    def B_drop2_select2(event):
        global Bentry, new_flag2, BIndex
        global B_parameters2, B_arg_flag2, B_Indicator2, B_arg_list2, B_subIndicator2, B_Indicator2, B_input_names2, B_output_names2
        B_selected_value2 = B_Indicator2.get()

        print(B_selected_value2)

        if B_selected_value2 == "OHLC":
            for widget in window.grid_slaves():
                if int(widget.grid_info()["row"]) >= int(B_Indicator2.grid_info()["row"])+1  and int(widget.grid_info()["row"]) <= int(B_subIndicator2.grid_info()["row"])-1    and int(widget.grid_info()["column"]) in [2,3]:
                    widget.grid_forget()
            B_subIndicator2.set('')
            B_subIndicator2['values'] = ["Open","High","Low","Close"]
            B_subIndicator2['state'] = 'readonly'

            label = ttk.Label(window, text="Index: ")
            label.grid(row=int(B_Indicator2.grid_info()["row"]) + 1, column=2)
            BIndex = ttk.Entry(window)
            BIndex.grid(row=int(B_Indicator2.grid_info()["row"]) + 1, column=3)


            B_arg_flag2 = 0
            new_flag2 = 0
            Label2.grid(row=int(B_Indicator2.grid_info()["row"])+1, column=2)
            B_subIndicator2.grid(row=int(B_Indicator2.grid_info()["row"])+1, column=3)

        elif B_selected_value2 == "Number":
            for widget in window.grid_slaves():
                if int(widget.grid_info()["row"]) >= int(B_Indicator2.grid_info()["row"])+1  and int(widget.grid_info()["row"]) <= int(B_subIndicator2.grid_info()["row"])-1    and int(widget.grid_info()["column"]) in [2,3]:
                    widget.grid_forget()
            B_subIndicator2.set('')
            B_subIndicator2['values'] = ()
            B_subIndicator2['state'] = 'disabled'

            label = ttk.Label(window, text="Value: ")
            label.grid(row=int(B_Indicator2.grid_info()["row"]) + 1, column=2)
            Bentry = ttk.Entry(window)
            Bentry.grid(row=int(B_Indicator2.grid_info()["row"]) + 1, column=3)

            B_arg_flag2 = 0
            new_flag2 = 1
            Label2.grid(row=int(B_Indicator2.grid_info()["row"])+1+1, column=2)
            B_subIndicator2.grid(row=int(B_Indicator2.grid_info()["row"])+1+1, column=3)

            BIndex = None
        
        else:
            B_indicator_info2 = ta.Function(B_selected_value2).info

            B_input_names2 = B_indicator_info2['input_names']
            B_parameters2 = B_indicator_info2['parameters']
            B_output_names2 = B_indicator_info2['output_names']
            B_num_arguments2 = len(B_parameters2) + 1


            for widget in window.grid_slaves():
                if int(widget.grid_info()["row"]) >= int(B_Indicator2.grid_info()["row"])+1 and int(widget.grid_info()["row"]) <= int(B_subIndicator2.grid_info()["row"])-1 and int(widget.grid_info()["column"]) in [2,3]:
                    widget.grid_forget()


            print("--------------------------------")
            print(B_input_names2)
            print("--------------------------------")
            print(B_parameters2)
            print("--------------------------------")
            print(B_output_names2)
            print("--------------------------------")
            print(f"The indicator '{B_selected_value2}' requires {B_num_arguments2} arguments.")
            print("--------------------------------")

            if len(B_parameters2) != 0:
                for i in range(0,len(B_parameters2)):
                    label = ttk.Label(window, text=list(B_parameters2.keys())[i])
                    label.grid(row=int(B_Indicator2.grid_info()["row"]) + 1+i, column=2)
                    Bentry = ttk.Entry(window)
                    Bentry.grid(row=int(B_Indicator2.grid_info()["row"]) + 1+i, column=3)
                    B_arg_list2.append(list(B_parameters2.keys())[i])
                    if i == len(B_parameters2)-1:
                        B_arg_flag2 = i
                        new_flag2 = i+1
                        Label2.grid(row=int(B_Indicator2.grid_info()["row"])+1+B_arg_flag2 +1, column=2)
                        B_subIndicator2.grid(row=int(B_Indicator2.grid_info()["row"])+1 +B_arg_flag2 +1, column=3)
                
                if len(B_input_names2) != 0:
                    label = ttk.Label(window, text="Index: ")
                    label.grid(row=int(B_Indicator2.grid_info()["row"])+ 1 + B_arg_flag2 + 1, column=2)
                    BIndex = ttk.Entry(window)
                    BIndex.grid(row=int(B_Indicator2.grid_info()["row"])+ 1 + B_arg_flag2 + 1, column=3)
                    B_arg_flag2 = B_arg_flag2+1
                    new_flag2 = new_flag2+1
                    Label2.grid(row=int(B_Indicator2.grid_info()["row"])+1+B_arg_flag2 +1, column=2)
                    B_subIndicator2.grid(row=int(B_Indicator2.grid_info()["row"])+1 +B_arg_flag2 +1, column=3)
                else:
                    BIndex = None
            
            else:
                if len(B_input_names2) != 0:
                    label = ttk.Label(window, text="Index: ")
                    label.grid(row=int(B_Indicator2.grid_info()["row"])+ 1, column=2)
                    BIndex = ttk.Entry(window)
                    BIndex.grid(row=int(B_Indicator2.grid_info()["row"])+ 1, column=3)
                    B_arg_flag2 = 1
                    new_flag2 = 2
                    Label2.grid(row=int(B_Indicator2.grid_info()["row"])+1+1, column=2)
                    B_subIndicator2.grid(row=int(B_Indicator2.grid_info()["row"])+1 +1, column=3)
                
                else:
                    B_arg_flag2 = 0
                    new_flag2 = 0
                    Label2.grid(row=int(B_Indicator2.grid_info()["row"])+1, column=2)
                    B_subIndicator2.grid(row=int(B_Indicator2.grid_info()["row"])+1, column=3)
                    BIndex = None

            B_subIndicator2.set('')
            B_subIndicator2['values'] = ()
            if len(B_output_names2) > 1:
                B_subIndicator2['values'] = B_output_names2
                B_subIndicator2['state'] = 'readonly'
            else:
                B_subIndicator2['state'] = 'disabled'


    def B_drop3_select2(event):
        global B_parameters2, B_arg_flag2, B_Indicator2, B_arg_list2, B_subIndicator2, B_Indicator2, B_input_names2, B_output_names2
        B2_selected_value2 = B_Indicator2.get()

        print(B2_selected_value2)

                
                

    tk.Label(window, text="Enter values for B:").grid(row=flag_condition, column=2)
    tk.Label(window, text="Function Group:").grid(row=flag_condition+1, column=2)
    B_Function_Group2 = ttk.Combobox(window, state='readonly')
    B_Function_Group2.grid(row=flag_condition+1, column=3)
    listB = list(indicator_groups2.keys())
    listB.append("Number")
    B_Function_Group2['values'] = listB
    B_Function_Group2.bind('<<ComboboxSelected>>', B_drop1_select2)

    tk.Label(window, text="Indicator:").grid(row=int(B_Function_Group2.grid_info()["row"])+1, column=2)
    B_Indicator2 = ttk.Combobox(window, state='disabled')
    B_Indicator2.grid(row=int(B_Function_Group2.grid_info()["row"])+1, column=3)
    B_Indicator2.bind('<<ComboboxSelected>>', B_drop2_select2)

    Label2 = tk.Label(window, text="Sub Indicator:")
    Label2.grid(row= int(B_Indicator2.grid_info()["row"]) +1, column=2)
    B_subIndicator2 = ttk.Combobox(window, state='disabled')
    B_subIndicator2.grid(row=int(B_Indicator2.grid_info()["row"])+1, column=3)
    B_subIndicator2.bind('<<ComboboxSelected>>', B_drop3_select2)





# def remove_condition():
#     global Return, flag_condition

#     Return.pop(flag_condition-1)

#     flag_condition = flag_condition-1
#     print(Return)

#     pass






start_button = tk.Button(window, text="Scan", command=scan)
start_button.grid(row=int(tf_input.grid_info()["row"]) +1, column=7)


add_condition_button = tk.Button(window, text="Click to add more Condition", command=add_condition)
add_condition_button.grid(row=int(start_button.grid_info()["row"]) +1 , column=7)

# remove_condition_button = tk.Button(window, text="Click to remove last Condition", command=remove_condition)
# remove_condition_button.grid(row=int(add_condition_button.grid_info()["row"]) +1 , column=7)


radio_var = tk.IntVar()

radio_btn1 = tk.Radiobutton(window, text="Any", variable=radio_var, value=1).grid(row=int(add_condition_button.grid_info()["row"]) +1 , column=7)
radio_btn2 = tk.Radiobutton(window, text="All", variable=radio_var, value=2).grid(row=int(add_condition_button.grid_info()["row"]) +2 , column=7)
radio_var.set(1)






if __name__ == '__main__':
	
	window.after(100, mainloop)
	window.mainloop()
