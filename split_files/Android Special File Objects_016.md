---
file: /home/pedro/Documents/chatgpt_export/Markdown/Android Special File Objects.md
heading_stack: <root> -> 0ad6fd5f-6810-4e02-9554-815224320034 -> System -> 5813abb3-bc8f-4116-a4aa-0e0986508a91 -> System -> aaa2b7d1-41d5-4e04-9a47-4d88c4e6cc50 -> User -> 69acab58-9f38-48e0-83b1-285e483e7e67 -> Assistant -> aaa21991-06a5-4043-9e92-42d41a412bcf -> User -> f19b7b82-fd63-4dab-a860-43a7e82b037e -> Assistant -> aaa27689-13bb-4ff1-bc11-84a1945c2c3b -> User -> 33611eda-9054-4307-b422-d65d8490252e -> Assistant
---
# Assistant

In a typical Android environment, you'll find several UNIX domain sockets that are used for various inter-process communication tasks. However, access to these sockets is usually restricted by permissions and SELinux policies. Here's a breakdown of some commonly found UNIX sockets:

1. **`/dev/socket/property_service`**: Used by the Android property service for setting and getting system properties.

2. **`/dev/socket/zygote`**: Used for communication with the Zygote process to fork new app processes.

3. **`/dev/socket/logd`**: Used for logging data; interacts with the Android logging system.

4. **`/dev/socket/adb`**: If the Android Debug Bridge (ADB) is enabled, this socket is used for communication.

5. **`/dev/socket/rild`**: Radio Interface Layer Daemon socket, used for communication with the modem or radio hardware.

6. **`/dev/socket/qmux_radio/`**: Qualcomm's IPC router interface for radio communication.

7. **`/dev/socket/netd`**: Socket for the Network Daemon, which handles network-related tasks like firewall rules and routing.

8. **`/dev/socket/keystore`**: Used for accessing the Android Keystore system.

9. **`/dev/socket/statsd`**: Used for collecting statistics and analytics data.

10. **`/dev/socket/wpa_wlan0`**: If the device is using WPA for WiFi, this socket may be used for WPA supplicant communication.

11. **`/dev/socket/vold`**: Used for volume and disk management tasks.

The above list is not exhaustive and can vary between Android versions and vendors. Also, many of these sockets are not accessible without root access or special permissions. Would you like to know more about any of these in particular?

---
