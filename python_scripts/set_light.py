########################################################
###         Set color and brightness                 ###
###                 Parameters:                      ###
### {"entity_id": "cuisine", "brightness_pct": "10"} ###
########################################################

entity_id = data.get('entity_id').replace(' ', '_').replace('é', 'e').replace('è', 'e')
brightness_pct = data.get('brightness_pct')

if entity_id is not None: 

  if (hass.states.get("light."+entity_id)):
    light_data = {'entity_id': 'light.' + entity_id, 'brightness_pct': brightness_pct, 'transition': 1}
    hass.services.call('light', 'turn_on', light_data, False)
    service_data = {"text":"Ok, je règle la lampe " + entity_id + " à " + brightness_pct +"%"}
    hass.services.call('snips', 'say', service_data)
    
  else :
    service_data = {"text":"Impossible de trouver la lampe" + data.get('entity_id') + "'"}
    hass.services.call('snips', 'say', service_data)

