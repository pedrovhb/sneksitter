---
file: /home/pedro/Documents/chatgpt_export/Markdown/Asyncio Android am Integration.md
heading_stack: <root> -> 33028313-468b-4c7d-8352-6d2d1720ddca -> System -> 39ea25d0-5f9f-45ba-bf86-c730d4173350 -> System -> aaa27bdf-0126-4efe-993d-35b4823801e1 -> User -> 19604108-672c-4d31-99ac-0799fd1fd233 -> Assistant -> aaa200cc-93ac-4ba9-b80c-7d42d885a647 -> User -> 0d1d5bd6-4a44-44c5-8225-253c1660498c -> Assistant -> aaa2d7a8-e627-444c-b642-0016cca0ec5f -> User -> 3ff55b5a-274c-478b-bd3e-9258a0279985 -> Assistant -> d51f6070-5ab7-45c2-acb6-f9c08b10328e -> Tool -> 91701092-7042-4065-a8d7-a509c447eb3f -> Assistant -> aaa24469-77e2-4cdb-8441-095efd8c0028 -> User -> ff41365e-622d-4876-896c-c0268d92ef5c -> Assistant -> aaa2f81d-45e4-4750-a979-5e63e8e1749e -> User -> 3054417f-6229-48a0-92a9-205d0bef556d -> Assistant -> Open a URL in the Default Web Browser -> Open a Song on Spotify -> Dial a Phone Number -> Send an SMS -> Start/Stop Playback (Media Control) -> Open Google Maps with Directions -> Open Email App -> aaa253e3-d7eb-4862-a9d7-bc0435cea38e -> User -> ccbe7c0d-d938-46ac-beab-7eb6ff38bd09 -> Assistant
---
# Assistant

```python
from urllib.parse import urlencode

async def open_url(url: str) -> Tuple[str, str]:
    return await launch_activity("android.intent.action.VIEW", url)

async def open_spotify_track(track_id: str) -> Tuple[str, str]:
    spotify_uri = f"spotify:track:{track_id}"
    return await launch_activity("android.intent.action.VIEW", spotify_uri)

async def dial_phone_number(number: str) -> Tuple[str, str]:
    tel_uri = f"tel:{number}"
    return await launch_activity("android.intent.action.DIAL", tel_uri)

async def send_sms(number: str, body: str) -> Tuple[str, str]:
    sms_uri = f"sms:{number}"
    return await launch_activity("android.intent.action.SENDTO", sms_uri, ["--es", f"sms_body {body}"])

async def media_control(event: str) -> Tuple[str, str]:
    return await run_am_command(["broadcast", "-a", "android.intent.action.MEDIA_BUTTON", "--es", f"android.intent.extra.KEY_EVENT {event}"])

async def open_google_maps(latitude: float, longitude: float) -> Tuple[str, str]:
    maps_uri = f"google.navigation:q={latitude},{longitude}"
    return await launch_activity("android.intent.action.VIEW", maps_uri)

async def send_email(to: str, subject: str, body: str) -> Tuple[str, str]:
    email_data = {
        "android.intent.extra.EMAIL": to,
        "android.intent.extra.SUBJECT": subject,
        "android.intent.extra.TEXT": body
    }
    email_extras = [f"--es {key} {value}" for key, value in email_data.items()]
    return await launch_activity("android.intent.action.SEND", "text/plain", email_extras)

# Example usage
async def main():
    stdout, stderr = await open_url("http://www.google.com")
    print(f"Open URL stdout: {stdout}, stderr: {stderr}")

    stdout, stderr = await open_spotify_track("TRACK_ID")
    print(f"Open Spotify Track stdout: {stdout}, stderr: {stderr}")

    stdout, stderr = await dial_phone_number("+1234567890")
    print(f"Dial Phone Number stdout: {stdout}, stderr: {stderr}")

    stdout, stderr = await send_sms("+1234567890", "Hello")
    print(f"Send SMS stdout: {stdout}, stderr: {stderr}")

    stdout, stderr = await media_control("KEYCODE_MEDIA_PLAY_PAUSE")
    print(f"Media Control stdout: {stdout}, stderr: {stderr}")

    stdout, stderr = await open_google_maps(37.7749, -122.4194)
    print(f"Open Google Maps stdout: {stdout}, stderr: {stderr}")

    stdout, stderr = await send_email("email@example.com", "Subject", "Body")
    print(f"Send Email stdout: {stdout}, stderr: {stderr}")

# Uncomment to run the example
# asyncio.run(main())
```

[child ⬇️](#bb7b0174-b681-40e2-808e-7a9d4186509b)

---

(main branch ⎇)
###### bb7b0174-b681-40e2-808e-7a9d4186509b
[parent ⬆️](#ccbe7c0d-d938-46ac-beab-7eb6ff38bd09)
