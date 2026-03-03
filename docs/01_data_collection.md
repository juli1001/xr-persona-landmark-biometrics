# Data Collection (Persona Capture on visionOS)

This project starts with data collection in XR.

On Apple Vision Pro, PolySpatial + `WebCamTexture` can provide a feed of the user’s Spatial Persona. Unity does not enable WebCamTexture support by default, so it requires additional configuration.

I used Unity’s PolySpatial WebCamTexture support as the base reference for building my internal Unity app. The important concept is that WebCamTextures are not automatically updated (or “dirtied”) when the camera updates the texture. Because of that, PolySpatial will not refresh the texture on the host platform unless it is manually marked as dirty.

## Why the texture must be marked dirty

WebCamTextures are not auto-dirtied when the camera updates the texture. This means PolySpatial will not know that it needs to update the texture on the target platform unless explicitly told to do so.

Below is the helper script (from the Unity PolySpatial workflow) that I used as the base logic to ensure the Persona texture is refreshed while recording:

```csharp
using UnityEngine;
using Unity.PolySpatial;

public class SetWebCamDirty : MonoBehaviour
{
#if POLYSPATIAL_ENABLE_WEBCAM
    public WebCamTexture texture;
#endif

    void Update()
    {
#if POLYSPATIAL_ENABLE_WEBCAM
        // Texture may be null if the web camera isn't actively recording into it.
        if (texture != null && texture.isPlaying)
            Unity.PolySpatial.PolySpatialObjectUtils.MarkDirty(texture);
#endif
    }
}
```
This dirtying API is only available when `POLYSPATIAL_ENABLE_WEBCAM` is defined.

---

## What my Unity app does (high-level)

Using this as a foundation, I built a small internal Unity application that:

- Accesses the Persona feed through `WebCamTexture`
- Captures Persona frames at a fixed interval (every N seconds)
- Saves the images locally on the device
- After recording, transfers the images to my computer for offline processing

The Unity source code for the app is not included in this public repository. This document describes the workflow at a high level to make the data pipeline clear.

---

## Required setup notes

To enable Persona capture on visionOS:

- Create the scripting define: `POLYSPATIAL_ENABLE_WEBCAM`
- Fill in the Camera Usage Description field in Unity Player Settings
- Be aware that capturing large textures or multiple `WebCamTextures` may incur performance costs

Reference: Unity PolySpatial WebCamTexture Support documentation.
