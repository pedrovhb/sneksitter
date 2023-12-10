---
file: /home/pedro/Documents/chatgpt_export/Markdown/RTL-SDR for Airport Broadcasts.md
heading_stack: <root> -> bb013b24-3092-439f-8959-db42f9b54bae -> System -> d927efc8-ebc0-4513-9b1a-c382f89937f7 -> System -> aaa2974b-2a43-49d9-bb4d-8d5ba31e6056 -> User -> 8ba95a48-504d-4c21-988a-9f2dd1bf1c3f -> Assistant -> Hardware and Software Requirements: -> Setup Steps: -> aaa24b05-31f8-42fc-84e2-4a44e22ebf99 -> User -> 88197d06-86d4-4db6-b492-c813068caaa4 -> Assistant -> aaa20814-5ced-4fc9-9680-5b11a506b7da -> User -> a9a2de9f-3ceb-40b6-8190-2fa426b79dd6 -> Assistant -> aaa2a2f7-5aab-4a76-a75a-92a33051d9a6 -> User -> 311e3bf3-a96c-411b-9bab-5d337b24791f -> Assistant
---
# Assistant

The data obtained from ADS-B transmissions typically include information about the aircraft's identity, position, altitude, velocity, and other flight-related data. Here's a breakdown of some key data fields you might encounter:

1. **ICAO Address:** A unique identifier for the aircraft, assigned by the International Civil Aviation Organization.
2. **Flight ID:** The flight number or callsign of the aircraft.
3. **Altitude:** The current altitude of the aircraft, usually in feet.
4. **Ground Speed:** The speed of the aircraft over the ground, usually in knots.
5. **Track:** The direction the aircraft is currently heading in, usually in degrees from North.
6. **Latitude and Longitude:** The geographical coordinates of the aircraft.
7. **Vertical Rate:** The rate at which the aircraft is climbing or descending, usually in feet per minute.
8. **Squawk:** A four-digit code entered by the pilot, used by air traffic control to identify aircraft on radar displays.
9. **Emergency:** Indicates whether the aircraft has set an emergency code on its transponder.
10. **Category:** Provides information about the type and mission of the aircraft.

When using tools like Dump1090, this data can be viewed in a text-based format in the terminal, or in a more user-friendly graphical format if using a web interface or additional software like Virtual Radar Server.

In a networked setup, the raw data is often sent in a format like AVR or Beast binary format, which can then be decoded by software on the receiving end to extract and display the above information.

[child ⬇️](#aaa28afc-9c52-4f75-bf73-9a09d5e34a9f)

---

(main branch ⎇)
###### aaa28afc-9c52-4f75-bf73-9a09d5e34a9f
[parent ⬆️](#311e3bf3-a96c-411b-9bab-5d337b24791f)
