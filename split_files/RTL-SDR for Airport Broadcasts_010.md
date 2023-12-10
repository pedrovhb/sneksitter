---
file: /home/pedro/Documents/chatgpt_export/Markdown/RTL-SDR for Airport Broadcasts.md
heading_stack: <root> -> bb013b24-3092-439f-8959-db42f9b54bae -> System -> d927efc8-ebc0-4513-9b1a-c382f89937f7 -> System -> aaa2974b-2a43-49d9-bb4d-8d5ba31e6056 -> User -> 8ba95a48-504d-4c21-988a-9f2dd1bf1c3f -> Assistant -> Hardware and Software Requirements: -> Setup Steps:
---
### Setup Steps:

1. **Install SDR Software:**
   - Download and install SDR# or GQRX depending on your operating system. SDR# is popular on Windows, while GQRX is popular on Linux.
  
2. **Configure RTL-SDR:**
   - Plug in your RTL-SDR dongle and antenna.
   - Open your SDR software and select the RTL-SDR dongle as your input device.
   - Configure the sample rate, gain, and other settings as necessary.

3. **Tune to Aviation Frequencies:**
   - Aviation communications typically occur in the frequency range of 118-136 MHz (AM).
   - Tune your SDR software to a known frequency of a nearby airport or a common air traffic control frequency.

4. **Install and Configure Decoding Software (For ADS-B):**
   - ADS-B (Automatic Dependent Surveillance–Broadcast) signals are broadcast on 1090 MHz.
   - Install Dump1090 or a similar ADS-B decoding software.
   - Configure the software to use your RTL-SDR dongle, or use a Virtual Audio Cable to route audio from your SDR software to the decoding software.

5. **Monitor and Decode:**
   - With everything set up, you should now be able to listen to aviation communications or monitor ADS-B signals.
   - You can use additional software like Virtual Radar Server to visualize the ADS-B data on a map.

6. **Respect Legal Boundaries:**
   - Ensure you are adhering to the legal guidelines and regulations regarding radio scanning and decoding in your country.

This setup should provide a comprehensive environment to listen to and decode aviation communications from a nearby airport using your RTL-SDR dongle.

[child ⬇️](#aaa24b05-31f8-42fc-84e2-4a44e22ebf99)

---

(main branch ⎇)
###### aaa24b05-31f8-42fc-84e2-4a44e22ebf99
[parent ⬆️](#8ba95a48-504d-4c21-988a-9f2dd1bf1c3f)
