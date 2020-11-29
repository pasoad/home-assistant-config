#####################################################
###            Turn on or off device              ###
###                 Parameters:                   ###
### {"entity_id": "cuisine", "action": "turn_on"} ###
#####################################################


def execute(hass, device_type, action, entity_id, state):
  service_data = {'entity_id': device_type+'.'+entity_id}

  if action == "turn_on":
    if state == 'on':
      service_data = {"text":entity_id + " est allumé"}
      hass.services.call('snips', 'say', service_data)
    else:
      hass.services.call(device_type, action, service_data, False)
      service_data = {"text":"Ok, j'allume " + entity_id}
      hass.services.call('snips', 'say', service_data)
    
  elif action == "turn_off":
    if state == 'off':
      service_data = {"text":entity_id + " est éteint"}
      hass.services.call('snips', 'say', service_data)
    else:
      hass.services.call(device_type, action, service_data, False)
      service_data = {"text":"Ok, j'éteint " + entity_id}
      hass.services.call('snips', 'say', service_data)


entity_id = data.get('entity_id').replace(' ', '_').replace('é', 'e').replace('è', 'e')
action = data.get('action')

if entity_id is not None:
  switch_state = hass.states.get("switch."+entity_id)
  light_state = hass.states.get("light."+entity_id)

  if (light_state):
    execute(hass, 'light', action, entity_id, light_state.state)
    
  elif (switch_state):
    execute(hass, 'switch', action, entity_id, light_state.state)
    
  else :
    service_data = {"text":"Impossible de trouver " + data.get('entity_id') + "'"}
    hass.services.call('snips', 'say', service_data)