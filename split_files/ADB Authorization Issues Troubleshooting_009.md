---
file: /home/pedro/Documents/chatgpt_export/Markdown/ADB Authorization Issues Troubleshooting.md
heading_stack: <root> -> 3e84d374-38da-4aa9-9db9-07aa1ed606d9 -> System -> 582802aa-f2cb-4b92-8e33-1e62e80857ae -> System -> aaa21cb1-e035-4e2b-8686-3f16d07889b1 -> User -> 6d1f27da-26b5-4e0d-926e-147bb01248b5 -> Assistant -> On the Computer:
---
### On the Computer:

1. **Kill the ADB Server**: You've already tried this, but just to be sure, run `adb kill-server` followed by `adb start-server`.

2. **Check Environment Variable**: Ensure the `$ADB_VENDOR_KEYS` environment variable is set properly. If it's not, set it to point to the location where your vendor keys are stored.

3. **Update ADB**: Sometimes these issues can be fixed by simply updating to the latest version of ADB.

4. **Check ADB Devices**: After starting the server, run `adb devices`. The device should initially appear as unauthorized.

