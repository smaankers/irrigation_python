import traceback
import logging

from flask import Flask, render_template, redirect, url_for

import hal.io_irrigation
import hal.Timed_io


app = Flask(__name__)
io = hal.io_irrigation.IO_irrigation()
pump = hal.Timed_io.Timed_pump(io)
valve_left = hal.Timed_io.Timed_valve_left(io)
valve_right = hal.Timed_io.Timed_valve_right(io)

@app.route("/")
def home():
   templateData = {
        'pump'        : pump.is_running(),
        'valve_left'  : valve_left.is_running(),
        'valve_right'  : valve_right.is_running()
      }
   
   return render_template('main.html', **templateData)

@app.route("/<group>/<status>")
def action(group, status):
    
    message = ""
    time_in_seconds = 10 * 60

    if group == "left":
        if status == "on":
            valve_left.start(time_in_seconds)
            pump.start(time_in_seconds)

            message = "Turned " + group + " to on"

        elif status ==  "off":
            valve_left.stop()
            pump.stop()
            
            message = "Turned " + group + " to off"

    elif group == "right":
        if status == "on":
            valve_right.start(time_in_seconds)
            pump.start(time_in_seconds)
            
            message = "Turned " + group + " to on"

        elif status ==  "off":
            valve_right.stop()
            pump.stop()
            
            message = "Turned " + group + " to off"

    return redirect(url_for('home'))


def main():
    
    io.start()
    
    try:
        app.run(host='0.0.0.0', port=8080, debug=True)
        
        
    except Exception as e:
        logging.error(traceback.format_exc())
    
    io.stop()
    
main()
