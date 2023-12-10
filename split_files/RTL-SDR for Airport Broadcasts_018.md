---
file: /home/pedro/Documents/chatgpt_export/Markdown/RTL-SDR for Airport Broadcasts.md
heading_stack: <root> -> bb013b24-3092-439f-8959-db42f9b54bae -> System -> d927efc8-ebc0-4513-9b1a-c382f89937f7 -> System -> aaa2974b-2a43-49d9-bb4d-8d5ba31e6056 -> User -> 8ba95a48-504d-4c21-988a-9f2dd1bf1c3f -> Assistant -> Hardware and Software Requirements: -> Setup Steps: -> aaa24b05-31f8-42fc-84e2-4a44e22ebf99 -> User -> 88197d06-86d4-4db6-b492-c813068caaa4 -> Assistant -> aaa20814-5ced-4fc9-9680-5b11a506b7da -> User -> a9a2de9f-3ceb-40b6-8190-2fa426b79dd6 -> Assistant
---
# Assistant

To view the data over the network, you have multiple options. One common method is to use a web browser to view a map populated with aircraft data, using software such as Virtual Radar Server, or by connecting to the web interface provided by Dump1090 itself if it's configured to serve data over HTTP.

Here's how to access the web interface provided by Dump1090:

1. **Run Dump1090 with the `--net` and `--net-http-port` options:**
   ```bash
   dump1090 --net --net-http-port 8080
   ```

2. **Access the Web Interface:**
   - Open a web browser on the same machine and navigate to `http://localhost:8080`.
   - If you're accessing it from another machine on the same network, replace `localhost` with the IP address of the machine running Dump1090.

If you're running a version of Dump1090 that does not have a built-in web server, you may need additional software. One such software is Virtual Radar Server, which can connect to Dump1090 and provide a visual representation of the data:

1. **Install Virtual Radar Server:**
   - Download and install Virtual Radar Server from the official website.

2. **Configure Virtual Radar Server:**
   - Open Virtual Radar Server.
   - Go to `Tools` → `Options`.
   - Under `Receivers`, add a new receiver with the following settings:
     - **Data Source:** AVR or Beast Raw Feed
     - **Connection Type:** Network
     - **Address:** `localhost:30005` (or replace `localhost` with the IP address of the machine running Dump1090, if on a different machine)

3. **View the Data:**
   - Click `OK` to save the settings.
   - Open a web browser and navigate to the address shown in the Virtual Radar Server window (usually `http://localhost:8080`).

These steps should help you visualize the ADS-B data on a map over the network.

[child ⬇️](#aaa2a2f7-5aab-4a76-a75a-92a33051d9a6)

---

(main branch ⎇)
###### aaa2a2f7-5aab-4a76-a75a-92a33051d9a6
[parent ⬆️](#a9a2de9f-3ceb-40b6-8190-2fa426b79dd6)
