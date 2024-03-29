import {
  Streamlit,
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode , Component } from "react"
import StreamlitCharts from "./ChartStreamlit"

interface State {
  numClicks: number
  isFocused: boolean
}


/**
 * This is a React-based component template. The `render()` function is called
 * automatically when your component should be re-rendered.
 */
class Streamlit_apexcharts extends StreamlitComponentBase<State> {
  public state = { numClicks: 0, isFocused: false }

  public render = (): ReactNode => {
    // Arguments that are passed to the plugin in Python are accessible
    // via `this.props.args`. Here, we access the "name" arg.
    var chart_dict = this.props.args["chart_dict"]

    
    // var ChangeFormater = {...chart_dict.options }

    // // var ChangeFormater = {}

    //  Object.keys(ChangeFormater).map( (k , i ) => {

    //     if (k in {xaxis:[] , yaxis : [] }){

    //         if ( "labels" in ChangeFormater[k] ) {

    //           if ( "formatter" in ChangeFormater[k]["labels"] ) {

    //             ChangeFormater[k]["labels"]["formatter"] = eval(ChangeFormater[k]["labels"]["formatter"])

    //             // console.log("change to funtion ")
    //           }
    //         }

    //       }
    //   } )
    

    // Streamlit sends us a theme object via props that we can use to ensure
    // that our component has visuals that match the active theme in a
    // streamlit app.
    const { theme } = this.props
    const style: React.CSSProperties = {}

    // Maintain compatibility with older versions of Streamlit that don't send
    // a theme object.
    if (theme) {
      // Use the theme object to style our button border. Alternatively, the
      // theme style is defined in CSS vars.
      const borderStyling = `1px solid ${
        this.state.isFocused ? theme.primaryColor : "gray"
      }`
      style.border = borderStyling
      style.outline = borderStyling
    }

    // chart_dict.options.theme = this.props.theme 


    // console.log(this.props)

    // Show a button and some text.
    // When the button is clicked, we'll increment our "numClicks" state
    // variable, and send its new value back to Streamlit, where it'll
    // be available to the Python program.
    return (
      <span>
        <StreamlitCharts chart_dict = {chart_dict}  width = {this.props.width}    ></StreamlitCharts>
      </span>
    )
  }

}

// "withStreamlitConnection" is a wrapper function. It bootstraps the
// connection between your component and the Streamlit app, and handles
// passing arguments from Python -> Component.
//
// You don't need to edit withStreamlitConnection (but you're welcome to!).
export default withStreamlitConnection(Streamlit_apexcharts)
