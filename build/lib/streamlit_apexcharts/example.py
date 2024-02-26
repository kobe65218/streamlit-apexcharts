import streamlit as st
from streamlit_apexcharts import streamlit_apexcharts
import pandas as pd 
import numpy as np 






df = pd.DataFrame({"test" : np.arange(10 ,20) , "test2" : [ f"c_{i}" for i in np.arange(10 ,20)]  }   )

df["test2"]  =  df["test2"].astype(pd.CategoricalDtype([ f"c_{i}" for i in np.arange(10 ,20)]))

df.set_index("test2" , inplace= True)

df["test3"] = np.arange(100 ,110)

df["test4"] = np.arange(110 ,120)


# df = pd.read_csv("~/.qlib/csv_data/tw_data/2330.csv")

# df["date"] = pd.to_datetime(df["date"])

# df.set_index("date" , inplace= True ) 

# df = df[["open" , "high" , "low" , "close" , "volume"]]
# # dataPointMouseEnter




dataPointMouseEnter_on = st.toggle('dataPointMouseEnter funtion')

click_on = st.toggle('click funtion')

append_new = st.toggle("append new data")



options = {
    
     "chart": {
              
            "id": "basic-bar" , 
            
            "type" : "heatmap" , 
            
            "width" : 500 , 
            
            "height" : 400  , 

            "events" : {
                
                "dataPointMouseEnter" : dataPointMouseEnter_on  , 
                
                "click" : click_on , 
                
            }

          }, 
     
        # "xaxis" : {
            
        #     "type": 'datetime'
            
            
        # } ,
        


        }
    
     
    #    "yaxis": [
           
                # {
                #    "seriesName": 'candlestick',
                   
                #    "axisTicks": {
                #      "show": True
                #    },
                #    "axisBorder": {
                #      "show": True ,
                #    },
                #    "title": {
                #      "text": "candlestick"
                #    }
                #  },
            
                
        #         {
                    
        #            "opposite": True ,
                   
        #             # "logarithmic": True,
        #             "title": {
        #              "text": "volume"
        #            } , 
                  
        #         #     "axisTicks": {
        #         #      "show": True
        #         #    },
                    
        #         #    "axisBorder": {
        #         #      "show": True ,
        #         #    },
                   
                   
        #           "seriesName": 'volume',
        #           "show": True
        #         }, 

        # ] , 

     }


# if append_new : 
    
#     df[f"test_5"] = 10
# m = st.number_input("mouth" , 1 , 12 )

# st.write(value_return)


value_return  = streamlit_apexcharts( df , options= options   ,     key ="ttt"  )

# st.write(on)
st.write(value_return)




# st.write(c[0]["columns"])

# st.write(df.loc[ value_return[0]["index"] , value_return[0]["columns"]])


