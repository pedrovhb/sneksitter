---
file: /home/pedro/Documents/chatgpt_export/Markdown/Asyncio Android am Integration.md
heading_stack: <root> -> 33028313-468b-4c7d-8352-6d2d1720ddca -> System -> 39ea25d0-5f9f-45ba-bf86-c730d4173350 -> System -> aaa27bdf-0126-4efe-993d-35b4823801e1 -> User -> 19604108-672c-4d31-99ac-0799fd1fd233 -> Assistant -> aaa200cc-93ac-4ba9-b80c-7d42d885a647 -> User -> 0d1d5bd6-4a44-44c5-8225-253c1660498c -> Assistant -> aaa2d7a8-e627-444c-b642-0016cca0ec5f -> User -> 3ff55b5a-274c-478b-bd3e-9258a0279985 -> Assistant -> d51f6070-5ab7-45c2-acb6-f9c08b10328e -> Tool -> 91701092-7042-4065-a8d7-a509c447eb3f -> Assistant -> aaa24469-77e2-4cdb-8441-095efd8c0028 -> User -> ff41365e-622d-4876-896c-c0268d92ef5c -> Assistant -> aaa2f81d-45e4-4750-a979-5e63e8e1749e -> User -> 3054417f-6229-48a0-92a9-205d0bef556d -> Assistant
---
# Assistant

Certainly, the `am` tool can be used for various tasks, although it's worth mentioning that these are mostly documented for debugging and development purposes. However, here are some examples:

### Open a URL in the Default Web Browser
```bash
am start -a "android.intent.action.VIEW" -d "http://www.google.com"
```

### Open a Song on Spotify
```bash
am start -a "android.intent.action.VIEW" -d "spotify:track:TRACK_ID"
```

### Dial a Phone Number
```bash
am start -a "android.intent.action.DIAL" -d "tel:+1234567890"
```

### Send an SMS
```bash
am start -a "android.intent.action.SENDTO" -d "sms:+1234567890" --es "sms_body" "Hello"
```

### Start/Stop Playback (Media Control)
For media controls, the commands would vary depending on the media player. Here's a generic example using media button events:
```bash
# Play/Pause
am broadcast -a "android.intent.action.MEDIA_BUTTON" --es "android.intent.extra.KEY_EVENT" "KEYCODE_MEDIA_PLAY_PAUSE"

# Stop
am broadcast -a "android.intent.action.MEDIA_BUTTON" --es "android.intent.extra.KEY_EVENT" "KEYCODE_MEDIA_STOP"
```

### Open Google Maps with Directions
```bash
am start -a "android.intent.action.VIEW" -d "google.navigation:q=latitude,longitude"
```

### Open Email App
```bash
am start -a "android.intent.action.SEND" -t "text/plain" --es "android.intent.extra.EMAIL" "email@example.com" --es "android.intent.extra.SUBJECT" "Subject" --es "android.intent.extra.TEXT" "Body"
```

These commands can be programmatically executed using the `run_am_command` and `launch_activity` functions we discussed earlier. Keep in mind that not all apps will respond to these intents as expected, especially if they have not been explicitly set up to do so.

Would you like to incorporate any of these into the existing Python code?

[child ⬇️](#aaa253e3-d7eb-4862-a9d7-bc0435cea38e)

---

(main branch ⎇)
###### aaa253e3-d7eb-4862-a9d7-bc0435cea38e
[parent ⬆️](#3054417f-6229-48a0-92a9-205d0bef556d)
