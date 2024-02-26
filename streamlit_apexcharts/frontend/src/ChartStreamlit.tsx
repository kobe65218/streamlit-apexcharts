
import React, { Component ,useState , useEffect , useRef, useCallback } from "react";
import Chart from "react-apexcharts";
import {
    Streamlit,
  } from "streamlit-component-lib"

// var t =  {

//       dataPointMouseEnter : {type : 'mouseenter'  , return : [ 'seriesIndex'  ,  'dataPointIndex' ]  } ,  


//       dataPointSelection : {type :  'mousedown' , return : ['seriesIndex' , 'dataPointIndex' ,  'selectedDataPoints']  }


//  }



  function EventCallback (event :any , chartContext :any , config :any , eventType :any  ) {

    // console.log(event)

    // // console.log(chartContext)
    // console.log(config)

      // var eventType = event.type 

      Streamlit.setComponentValue( { [eventType] :  {dataPointIndex : config.dataPointIndex  , seriesIndex : config.seriesIndex  ,selectedDataPoints :  "selectedDataPoints" in  config ?config["selectedDataPoints"] : null  } })   

      // if (eventType == "mousedown") {

      //   var dataPoint =config.selectedDataPoints
    
      //   var dataPointMap = dataPoint.map( (k :any   , i :any )=>    { 
          
      //     if ( k !== null ) {

      //         // var dataPoindexList = dataPoint[i]

      //         // dataPoindexList
  
      //         return {
      //             columns  : [index["columns"][i]],  
      //             index :  [index["index"][dataPoint[i]]]
      //         }
  
      //     }
  
      //   }  );
  
      //   dataPointMap = dataPointMap.filter((k:any) => k!= null )
  
      //   Streamlit.setComponentValue(dataPointMap)   

      // } else {


      //   var dataSeries =config.seriesIndex 

      //   var dataPoint = config.dataPointIndex

      //   Streamlit.setComponentValue([ {columns : [index["columns"][dataSeries] ] ,index : [index["index"][dataPoint] ]}])  

      // }

 

  }



const changeFormatterTofuntion = (options :any ) => {

  var Formatter = {...options}
  // var ChangeFormater = {}

   Object.keys(Formatter).map( (k , i ) => {

      if (k in {xaxis:[] , yaxis : [] }){

          if (Array.isArray(Formatter[k]) ){
             Formatter[k].map(( l : any , i :any ) => {

              if (  ("labels" in Formatter[k][i])   &&  ( "formatter" in Formatter[k][i]["labels"])  ) {

                  Formatter[k][i]["labels"]["formatter"] = eval(Formatter[k][i]["labels"]["formatter"])

              }

             })

          }else{

            if ( "labels" in Formatter[k] && "formatter" in Formatter[k]["labels"] ) {

                Formatter[k]["labels"]["formatter"] = eval(Formatter[k]["labels"]["formatter"])
            
            };
          };





        };

      if (k in {tooltip : []} ) {

        Object.keys(Formatter[k]).map( (l :any ) => {

          if (l  in {x : [] , y : [] , z  : [] }){

            if (  "formatter" in  Formatter[k][l]) {
              Formatter[k][l]["formatter"] = eval(Formatter[k][l]["formatter"] )

              }
            

            if ( (l == "y")  &&  ("title" in  Formatter[k][l]) && ( "formatter" in   Formatter[k][l]["title"] ) ) {

              Formatter[k][l]["title"]["formatter" ] =   eval(Formatter[k][l]["title"]["formatter" ])


            }



          }
        })
      }



      if (k in {dataLabels : []} ) {
        
        if ( "formatter" in Formatter[k] ){
          Formatter[k]["formatter"] = eval(Formatter[k]["formatter"]  )
        }
      }


      } )

    return Formatter

} 


const changeEvents = (options : any ) => {


      var newEvents = {...options.chart.events}

      Object.keys(newEvents).forEach((k) => {
        newEvents[k]  = newEvents[k] ?  (event :any , chartContext :any , config :any ) =>  {     EventCallback(event , chartContext , config   , k ) }   : null
       })

       var newOptions = {...options , chart  : { ...options.chart , events : newEvents} }

       return newOptions
}


const changeOption = (options : any ) => {

    return changeFormatterTofuntion(changeEvents(options))

}







function StreamlitCharts(props:any) {

    const [options, setOptions] = useState( changeOption(props.chart_dict.options )  )

    const chart = useRef<Chart>(null)

    

    useEffect(  () => {

      console.log("effect")
      var newOptions = changeOption(props.chart_dict.options)


      // chart.hideSeries('Cricket')

      // chart.current.hideSeries('Cricket')

      // console.log(chart.current.chart)

      setOptions(newOptions)

    } , [JSON.stringify(props.chart_dict.options) ]
    )

    console.log("rerender")


    return (
        <div className="app"  >
        <div className="row">
          <div className="mixed-chart">

            <Chart
              options={ options}
              series={props.chart_dict.series} 
              type= { options.chart.type}
              width= {props.width}
              height= { options.chart.height}
              ref={ chart  }

              
            />
          </div>
        </div>
      </div>
    );
  }
  
export default StreamlitCharts;