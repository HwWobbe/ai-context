#Requires AutoHotkey v2.0
#SingleInstance Force
#v1.0.0 (host mode may need local syncs)

; ── RnHw: Win+R — Register current browser URL ─────────────────────────────
; HwWvWT260302

PYTHON := "C:\Users\hwobb\.env\Scripts\python.exe"

#F12:: {
    ; 1. Focus address bar and copy URL
    SendInput "^l"
    Sleep 120
    SendInput "^c"
    Sleep 80
    SendInput "{Escape}"

    url := Trim(A_Clipboard)

    if (url = "") {
        MsgBox "No URL found in clipboard.`nFocus a browser tab first.", "RnHw Register", 48
        return
    }

    ; 2. Optional: prompt for category
    ib1 := InputBox("Category (leave blank for auto):", "RnHw Register", "w300 h120")
    if (ib1.Result = "Cancel")
        return
    category := ib1.Value

    ; 3. Optional: prompt for title override
    ib2 := InputBox("Title (leave blank to auto-detect):", "RnHw Register", "w400 h120")
    if (ib2.Result = "Cancel")
        return
    titleOverride := ib2.Value

    ; 4. Write args to temp file
    tmpIn  := A_Temp "\rnhw_in.txt"
    tmpOut := A_Temp "\rnhw_out.txt"
    try FileDelete(tmpIn)
    try FileDelete(tmpOut)
    content := url . "`n" . category . "`n" . titleOverride
    FileAppend(content, tmpIn, "UTF-8")

    ; 5. Call wrapper script
    cmd := 'set PYTHONIOENCODING=utf-8 && ' PYTHON ' "C:\Users\hwobb\RnHw\reg_url.py" "' tmpIn '"'
    RunWait(A_ComSpec ' /c ' cmd ' > "' tmpOut '" 2>&1',, "Hide")
    result := FileRead(tmpOut)

    ; 6. Show result
    MsgBox(result, "RnHw Register", 64)
}
