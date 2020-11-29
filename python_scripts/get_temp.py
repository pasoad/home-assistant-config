########################################################
###      get temp for a room (default: home)         ###
###                 Parameters:                      ###
###          {"entity_id": "cuisine"}                ###
########################################################

entity_id = data.get('entity_id').replace(' ', '_').replace('é', 'e').replace('è', 'e')
logger.error("entity_id " + entity_id)

if entity_id: 
  
  if entity_id == "dehors":
    temp  = hass.states.get("sensor.outdoor_temperature").state
    service_data = {"text":"Il fait " + temp + " dehors"}
    hass.services.call('snips', 'say', service_data)

  elif (hass.states.get("sensor."+entity_id) and hass.states.get("sensor."+entity_id).state):
    temp  = hass.states.get("sensor."+entity_id).state
    service_data = {"text":"Il fait " + temp + " dans " + entity_id}
    hass.services.call('snips', 'say', service_data)
    
  else:
    service_data = {"text":"Impossible de trouver la température de " + data.get('entity_id') + "'"}
    hass.services.call('snips', 'say', service_data)

else:
  temp  = hass.states.get("sensor.current_temperature").state
  service_data = {"text":"Il fait " + temp + " degrès dans la maison"}
  hass.services.call('snips', 'say', service_data)