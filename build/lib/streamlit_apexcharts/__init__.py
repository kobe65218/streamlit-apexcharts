import os
import streamlit.components.v1 as components
import streamlit as st 
import pandas as pd 
import numpy as np 


# Create a _RELEASE constant. We'll set this to False while we're developing
# the component, and True when we're ready to package and distribute it.
# the component, and True when we're ready to package and distribute it.
# (This is, of course, optional - there are innumerable ways to manage your
# release process.)
_RELEASE = True 

# Declare a Streamlit component. `declare_component` returns a function
# that is used to create instances of the component. We're naming this
# function "_component_func", with an underscore prefix, because we don't want
# to expose it directly to users. Instead, we will create a custom wrapper
# function, below, that will serve as our component's public API.

# It's worth noting that this call to `declare_component` is the
# *only thing* you need to do to create the binding between Streamlit and
# your component frontend. Everything else we do in this file is simply a
# best practice.

if not _RELEASE:
    _component_func = components.declare_component(
        # We give the component a simple, descriptive name ("my_component"
        # does not fit this bill, so please choose something better for your
        # own component :)
        "streamlit_apexcharts",
        # Pass `url` here to tell Streamlit that the component will be served
        # by the local dev server that you run via `npm run start`.
        # (This is useful while your component is in development.)
        url="http://localhost:3001",
    )
else:
    # When we're distributing a production version of the component, we'll
    # replace the `url` param with `path`, and point it to the component's
    # build directory:
    parent_dir = os.path.dirname(os.path.abspath(__file__))
    build_dir = os.path.join(parent_dir, "frontend/build")
    _component_func = components.declare_component("streamlit_apexcharts", path=build_dir)


# Create a wrapper function for the component. This is an optional
# best practice - we could simply expose the component function returned by
# `declare_component` and call it done. The wrapper allows us to customize
# our component's API: we can pre-process its input args, post-process its
# output value, and add a docstring for users.


@st.cache_data
def get_series( df  , chart_type  , columns_types ):
    
    # print("re caculate data")
    
    data_columns = df.columns 
    
    if chart_type  in [  "bar" , "line" , "area"  ,    ]  : 

        data_list = df.to_dict(orient = "index")
        
        # ,  "type" : columns_types[i]  if i in columns_types else  chart_type 

        series = [  {"name" : i   ,  "type" :   columns_types[i]  if i in columns_types else  chart_type ,  "data" :  [  {"x":  d_k   , "y":  data_list[d_k][i] } for d_k  in data_list  ] }   for i in  data_columns ] 
        
    elif chart_type in ["heatmap"] : 
        
        data_list = df.to_dict(orient = "index")
        
        series = [  {"name" : i   ,  "data" :  [  {"x":  d_k   , "y":  data_list[d_k][i] } for d_k  in data_list  ] }   for i in  data_columns ] 
        

        # print(series)

    elif chart_type in ["candlestick"] : 
        
        series = []
        
        df_ = df.copy()
        
        

        price = df_[["open" , "high" , "low" , "close"]].copy()
        
        # price.index = list(price.index.astype(int)/ 1E+06)
        
        price.insert( loc = 0 , column =  "time" , value =  price.index )

        series  += [ { "data" :  [  { "x" :  str(i[0]).replace(" 00:00:00" , "") , "y" : i[1:]  }  for i in price.values.tolist()]  , "type" : "candlestick"  , "name" : "candlestick" }  ] 
        
        
        df_ = df_.drop(["open" , "high" , "low" , "close"] , axis = 1)
        
        if df_.shape[1] != 0 :
    
            data_columns = df_.columns
        
            data_list = df_.to_dict(orient = "index")

            series += [  {"name" : i ,  "type" : columns_types[i]  if i in columns_types else  chart_type ,  "data" :  [  {"x":  str(d_k).replace(" 00:00:00" , "")  , "y":  data_list[d_k][i] } for d_k  in data_list  ] }   for i in  data_columns ] 
        
 
    
    elif chart_type in ["donut"] :

        series  = df.values.flatten().tolist() 
        
    return series


# @st.cache_data
# def get_options( options ): 
    
#     pre_dcit = {"xaxis" : {"labels"  : {"formatter" : {} } }  , "yaxis" : {"labels"  : {"formatter" : {} } }  }
    
    
#     options["xaxis"]["labels"]["formatter"]
    
    # if options.setdefault("xaxis" , None ).
    
    # for i in check :
        
    #     if  options.setdefault(i , None ).setdefault(i , None ) == None : 
            
            
    
    


def streamlit_apexcharts(  df   , options = {} ,  columns_types = {} ,   key=None  , default ={"dataPointIndex" : []  , "seriesIndex" : []  , "selectedDataPoints" : [] } ):
    
    
    '''
    columns_types only support "line" "bar" "area" 
    
    
    
    '''
    
    
    chart_dict = {}
    
    # data_columns = list(df.columns)
    
    # data_index = list(df.index)
    
    chart_type_base = options["chart"]["type"]
    
    series = get_series(df ,chart_type_base , columns_types )
    
    options["chart"]["id"] = key 
    
    chart_dict['options']  = options
    
    chart_dict["series"] = series
    
    # chart_dict["index"] = {
        
    #     "columns" : data_columns , 
        
    #     "index" : data_index    
    # }
    
    component_value = _component_func(chart_dict=chart_dict, key=key, default=default)

    return component_value



