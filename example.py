import streamlit as st
from streamlit_apexcharts import streamlit_apexcharts
import pandas as pd 
import numpy as np 






df = pd.DataFrame({"test" : np.arange(10 ,20) , "test2" : [ f"c_{i}" for i in np.arange(10 ,20)]  }   )

df["test2"]  =  df["test2"].astype(pd.CategoricalDtype([ f"c_{i}" for i in np.arange(10 ,20)]))

df.set_index("test2" , inplace= True)

df["test3"] = np.arange(100 ,110)

# df["test4"] = np.arange(110 ,120)


# df = pd.read_csv("~/.qlib/csv_data/tw_data/2330.csv")

# df["date"] = pd.to_datetime(df["date"])

# df.set_index("date" , inplace= True ) 

# df = df[["open" , "high" , "low" , "close" , "volume"]]
# # # dataPointMouseEnter


dataPointMouseEnter_on = st.toggle('dataPointMouseEnter funtion')

click_on = st.toggle('click funtion')

append_new = st.toggle("append new data")



options = {
    
     "chart": {
              
            # "id": "basic-bar" , 
            
            "type" : "heatmap" , 
            
            "group" : "test" , 
            
            # "width" : 500 , 
            
            "height" :'500'   , 

            "events" : {
                
                "dataPointMouseEnter" : dataPointMouseEnter_on  , 
                
                "click" : click_on , 
                
            }

          }, 
     
     
     "tooltip": {
       
        "enabled": True,
       
      #   "x": {
      #     "show": True,
      #     "formatter": undefined,
      # },
      
      
      "y": {
          "formatter": "(v) => `${parseFloat(v).toFixed(0)} %`",
          "title": {
              "formatter": "(v) => `${v} foamter`",
          },
      },
      "z": {
          "formatter":  "(v) => `${parseFloat(v).toFixed(0)} %`",
          # title: 'Size: '
      },
       
       
       
       
       
       
      } , 
     
     
     "dataLabels" : {
       
       "formatter": "(v) => `${parseFloat(v).toFixed(0)} %`",
       
       
      },
     
     
     "plotOptions" : {
       
       "heatmap" : {
         
         "colorScale" : {
           
           "ranges"  : [
             
             {
               
               "from" : -100 , 
               
               "to" : 0   , 
               
               "color" : "#00A100" ,
               
               "name" :  "neg return"
            
             } , 
             
              {
               
               "from" : 1 , 
               
               "to" : 100   , 
               
               "color" : "#FFB200" , 
               
                "name" :  "pos return"
            
             } , 
             
             
             
             
             
           ]
           
           
           
         }
         
         
         
       }
       
       
       
     } , 
       

       
       
       
    #  } 
     
     
          "xaxis" : {
               
              #  "min" : 0 , 
               
              #  "max" : 100 , 
               
              #  "range" : 50  , 
          
             "labels" : {
            
               "formatter" :  '(v) => `${v}%` '
          
          }
          
          } , 
             
             
               
          "yaxis" : {
          
             "labels" : {
            
               "formatter" :  '(v) => `v ?` '
          
          }  , 
             
             
             
             }  ,
     
        # "xaxis" : {
            
        #     "type": 'datetime'
            
            
        # } ,
    
     
      #  "yaxis": [
           
      #           {
      #              "seriesName": 'candlestick',
                   
      #              "axisTicks": {
      #                "show": True
      #              },
      #              "axisBorder": {
      #                "show": True ,
      #              },
      #              "title": {
      #                "text": "candlestick"
      #              } ,
                   
      #              "labels" :{
                   
      #               "formatter" :  '(v) => `${parseFloat(v).toFixed(0)}` ' , 
                    
      #                "minWidth": 40
                    
      #               } 
                   
      #            },
            
                
      #           {
                    
      #              "opposite": True ,
                   
      #               # "logarithmic": True,
      #               "title": {
      #                "text": "volume"
      #              } , 
                  
      #           #     "axisTicks": {
      #           #      "show": True
      #           #    },
                    
      #           #    "axisBorder": {
      #           #      "show": True ,
      #           #    },
                
      #             "labels" :{
                   
      #               "formatter" :  '(v) => `${parseFloat(v).toFixed(0)}` ' , 
                    
      #               "minWidth": 40
                    
      #               } 
                   
      #            ,
                   
                   
      #             "seriesName": 'volume',
      #             "show": True
      #           }, 

      #   ] , 

     }


# if append_new : 
  
#   if options.setdefault("yaxis" ) == None : 
    
#     options["yaxis"] = {
      
#       "labels"  : {
#         "formatter" : '(v) => `${parseFloat(v).toFixed(2)} %` '
        
#       }
    
#     }
  
  
  # options.setdefault("yaxis" ) = {"label" }
  
  
  # '(v) => `${parseFloat(v).toFixed(2)} %` '
  #  options["yaxis"]["labels"]["formatter"] = '(v) => `${parseFloat(v).toFixed(2)} %` '
    
#     df[f"test_5"] = 10
# m = st.number_input("mouth" , 1 , 12 )

# st.write(value_return)



col1  , col2   =  st.columns(2)

value_return  = streamlit_apexcharts( df  , options= options   , columns_types= { "test2" : "bar" } ,   key ="ttt"  )


# value_return  = streamlit_apexcharts( df.loc["2017"] , options= options   , columns_types= { "volume" : "bar" } ,   key ="ttt2"  )

# print(options)

# with col1  : 

  


# with col2 : 
  
#   st.write(df)
  
  
# with col2 : 
  
st.write(value_return)