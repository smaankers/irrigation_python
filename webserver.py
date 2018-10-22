import traceback
import logging

from flask import Flask, render_template, redirect, url_for

import io_relays.io_irrigation
import io_relays.Timed_io


app          = Flask(__name__)
io           = io_relays.io_irrigation.IO_irrigation()
pump         = io_relays.Timed_io.Timed_pump(io)
sensors      = io_relays.Timed_io.Timed_sensors(io)
valve_left   = io_relays.Timed_io.Timed_valve_left(io)
valve_right  = io_relays.Timed_io.Timed_valve_right(io)
valve_drip   = io_relays.Timed_io.Timed_valve_drip(io)
valve_refill = io_relays.Timed_io.Timed_valve_refill(io)
valve_filter = io_relays.Timed_io.Timed_valve_filter(io)
valve_sewage = io_relays.Timed_io.Timed_valve_sewage(io)

irrigate_in_seconds =  9 * 60
refill_in_seconds   = 90 * 60
drip_in_seconds     = 90 * 60
filter_in_seconds   =  2 * 60
sewage_in_seconds   = 15 * 60

@app.route("/")
def home():
   templateData = {
        'pump'                : pump.is_running(),
        'sensors'             : sensors.is_running(),
        'valve_left'          : valve_left.is_running(),
        'valve_right'         : valve_right.is_running(),
        'valve_drip'          : valve_drip.is_running(),
        'valve_refill'        : valve_refill.is_running(),
        'valve_filter'        : valve_filter.is_running(),
        'valve_sewage'        : valve_sewage.is_running(),
        'irrigate_in_minutes' : int(irrigate_in_seconds / 60),
        'refill_in_minutes'   : int(refill_in_seconds / 60),
        'drip_in_minutes'     : int(drip_in_seconds / 60),
        'filter_in_minutes'   : int(filter_in_seconds / 60),
        'sewage_in_minutes'   : int(sewage_in_seconds / 60),
      }
   
   return render_template('main.html', **templateData)

@app.route("/<group>/<status>")
def action(group, status):



    if group == "left":
        if status == "on":
            valve_left.start(irrigate_in_seconds)
            pump.start(irrigate_in_seconds)

        elif status ==  "off":
            valve_left.stop()
            pump.stop()

    elif group == "right":
        if status == "on":
            valve_right.start(irrigate_in_seconds)
            pump.start(irrigate_in_seconds)

        elif status ==  "off":
            valve_right.stop()
            pump.stop()

    elif group == "drip":
        if status == "on":
            valve_drip.start(drip_in_seconds)
            pump.start(irrigate_in_seconds)

        elif status == "off":
            valve_drip.stop()
            pump.stop()

    elif group == "refill":
        if status == "on":
            valve_refill.start(refill_in_seconds)
            sensors.start(refill_in_seconds)

        elif status == "off":
            sensors.stop()
            valve_refill.stop()

    elif group == "filter":
        if status == "on":
            valve_filter.start(filter_in_seconds)
            pump.start(irrigate_in_seconds)

        elif status == "off":
            valve_filter.stop()
            pump.stop()

    elif group == "sewage":
        if status == "on":
            valve_sewage.start(sewage_in_seconds)
            pump.start(sewage_in_seconds)

        elif status == "off":
            valve_sewage.stop()
            pump.stop()

    return redirect(url_for('home'))


def main():
    
    io.start()
    
    try:
        app.run(host='0.0.0.0', port=8080, debug=True)
        
        
    except Exception as e:
        logging.error(traceback.format_exc())
    
    io.stop()
    
main()
