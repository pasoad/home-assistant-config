
[![Discord francophone][discord-shield-fr]][discord-fr]
[![Forum francophone][forum-shield-fr]][forum-fr]
[![Awesome francophone][awesome-shield]][awesome-fr]


[![Official Discord][discord-shield]][discord]
[![Official community Forum][forum-shield]][forum]

Welcome to my humble Home Assistant configuration! / Bienvenue dans mon humble configuration Home Assistant!

[Here](#my-home-assistant-config-in-english) to continue in English

[Ici](#ma-configuration-home-assistant) pour continuer en Français

# My Home Assistant config

First of all, i'm not a dev. So i'm prety sure they are a lot of mistakes but maybe it can help someone one day :). I began to document my config recently, work in progress...

## Screenshots

<div alt="centered image">
<img src="https://github.com/pasoad/home-assistant-config/blob/main/screenshots/2020-11-29%2022_08_45-Home%20Assistant.png" width="450" hspace="5">
<img src="https://github.com/pasoad/home-assistant-config/blob/main/screenshots/2020-11-29%2022_08_59-Home%20Assistant.png" width="450" hspace="5">
</div>

<div alt="centered image">
<img src="https://github.com/pasoad/home-assistant-config/blob/main/screenshots/2020-11-29%2022_09_14-Home%20Assistant.png" width="450" hspace="5">
<img src="https://github.com/pasoad/home-assistant-config/blob/main/screenshots/2020-11-29%2022_09_34-Home%20Assistant.png" width="450" hspace="5">
</div>

<div alt="centered image">
<img src="https://github.com/pasoad/home-assistant-config/blob/main/screenshots/2020-11-29%2022_09_53-Home%20Assistant.png" width="450" hspace="5">
</div>

## Structure of my HA's config

I learned a lot by watching [Franck Nijhof on youtube](https://www.youtube.com/user/Frenck) and his [GitHub repo](https://github.com/frenck/home-assistant-config). I splitted my config in differents .yaml files so it's easier to navigate between every integratgions and automations with VS Code.

## Devices used

- HassOS on a RPi 4 2GB.
- ConBee II for Zigbee (deconz).
- Logitech Harmony.
- Netatmo Thermostat (+ 3 valves).
- Volumio (on 3 RPi for multi-room audio).
- Lights (Hue, Tradfri, Xiaomi, Mueller Licht).
- doors sensors (xiaomi)
- motion sensors (tradfri)
- Switches and remotes (Hue, Tradfri).
- Fan/Air cleaner Dyson.
- FireStick TV
- UnRaid Server
- Emby server
- Linky electrcity monitoring system
- Family phones (iOS and Android)

## Integrations configured thru Home Assistant GUI

The following integrations are not configured in YAML files. So you won't see it in this repository:

- deCONZ to manage Zigbee devices.
- Glances to have informations about my unRaid server.
- Google Cast if i want to stream audio directly to my Onkio receiver.
- HACS for installing custom elements.
- Home Assistant IOS to connect with an iPhone.
- Internet Printing Protocol (IPP) to see my cartridges ink level.
- Kodi for controling kodi media player.
- Logitech Harmony Hub for my Harmony remote control.
- Mobile App for android devices.
- Netatmo for my thermostat/valves
- Speedtest.net to check my ridiculously fast ADSL speed.
- Spotify to stream 2 spotify accounts thru volumio clients 
- UPnp a second way to monitor my internet ADSL speed.
- Météo-France to have weather alerts and rain forecast within the hour.
- Volumio to control my 3 volumio devices.

## Addons used

- SSH & Web Terminal to run some commands when it's necessary
- Samba share to acces to my config from my computer.
- Visual Studio Code if I need to change something in my config when i'm not at home.
- deCONZ to manage my differents light, remotes, switches, door sensors and moiton sensors.
- Duck DNS to access to my system from outside
- NGINX SSL proxy.


## Contributing

If you see something who needs to be improve or have suggestions, feel free to contribute.

# Ma configuration Home Assistant

Premierement, je ne suis pas dev. J'imagine qu'il y a énorméments d'erreurs mais peut-être que ma config peut aider quelqu'un un jour :). J'ai commencé à documenter ma config récemment, il y a encore du boulot...

## Screenshots

<div alt="centered image">
<img src="https://github.com/pasoad/home-assistant-config/blob/main/screenshots/2020-11-29%2022_08_45-Home%20Assistant.png" width="450" hspace="5">
<img src="https://github.com/pasoad/home-assistant-config/blob/main/screenshots/2020-11-29%2022_08_59-Home%20Assistant.png" width="450" hspace="5">
</div>

<div alt="centered image">
<img src="https://github.com/pasoad/home-assistant-config/blob/main/screenshots/2020-11-29%2022_09_14-Home%20Assistant.png" width="450" hspace="5">
<img src="https://github.com/pasoad/home-assistant-config/blob/main/screenshots/2020-11-29%2022_09_34-Home%20Assistant.png" width="450" hspace="5">
</div>

<div alt="centered image">
<img src="https://github.com/pasoad/home-assistant-config/blob/main/screenshots/2020-11-29%2022_09_53-Home%20Assistant.png" width="450" hspace="5">
</div>

## Structure de ma configuration Home Assistant

j'ai beaucoup appris en regardant les vidéos de [Franck Nijhof sur youtube](https://www.youtube.com/user/Frenck) et son [repo GitHub](https://github.com/frenck/home-assistant-config). J'ai séparé ma configuration en plusieurs fichiers .yaml pour aue ce soit plus facile de naviguer entre les différentes intégrations et automatisations via VS Code.

## Appareils utilisés

- HassOS sur un RPi 4 2GB.
- ConBee II pour le Zigbee (Deconz).
- Logitech Harmony.
- Netatmo Thermostat (+ 3 vannes).
- Volumio (sur 3 RPi pour l'audio multi-room).
- Ampoules (Hue, Tradfri, Xiaomi, Mueller Licht).
- Détection ouverture de porte (xiaomi)
- Détection de mouvements (tradfri)
- Interrupteurs et télécommandes (Hue, Tradfri).
- Ventilateur/Purificateur d'air Dyson.
- FireStick TV
- Serveur UnRaid
- Serveur Emby
- Compteur électrique Linky
- Smartphones de la famille (iOS et Android)

## Integrations configurées à partir de l'interface graphique de Home Assisatnt

Les intégrations ci-dessous ne sont pas configurées avec des fichiers YAML. Donc vous ne pourrez pas le voir de ce repo:

- deCONZ pour gérer les appareils Zigbee.
- Glances pour avoir des informations à propos de mon serveur unRaid.
- Google Cast si je veux caster de l'audio directemnt sur mon amli Onkyo.
- HACS pour gérer les intégrations/éléments custom.
- Home Assistant IOS pour la connection avec un iPhone.
- Internet Printing Protocol (IPP) pour voir le niveau des encres de mon imprimante.
- Kodi pour contrôler mon lecteur Kodi.
- Logitech Harmony Hub pour la connection avec ma télécommande harmony.
- Mobile App pour les appareils Android.
- Netatmo pour mon Thermostat/vannes
- Speedtest.net pour voir la rapidité légendaire de ma connection ADSL.
- Spotify pour srteamer de la musique sur les RPi avec volumio. 
- UPnp une deuxième manière de tester ma connection internet.
- Météo-France pour avoir les alertes météos dans l'heure.
- Volumio pour contrôler les 3 RPi avec volumio.

## Addons used

- SSH & Web Terminal pour exécuter quelques commandes si nécessaire.
- Samba share pour accéder à ma config depuis mon ordinateur.
- Visual Studio Code si j'ai besoin de changer quelque chose à ma config depuis l'exterieur.
- deCONZ to manage my differents light, remotes, switches, door sensors and moiton sensors.
- deCONZ pour gérer le diférentes ampoules, télécommandes, interrupteurs, détecions d'ouvertures de portes et détection de mouvements.
- Duck DNS pour accéder à mon Home Assistant de l'extérieur.
- NGINX SSL proxy.

## Contributions

Si vous voyez quelque chose à améliorer ou avez des suggestions, n'hésitez pas à contribuer.