; Система мониторинга реакторов и учёта доз
; NSIS Installer Script
; Кобелев Д.Д., 2026

Unicode True

!define APP_NAME      "ReactorMonitor"
!define APP_VERSION   "1.0.0"
!define APP_PUBLISHER "Кобелев Д.Д."
!define APP_DIR       "$PROGRAMFILES64\ReactorMonitor"
!define HELP_FILE     "$INSTDIR\help\index.html"
!define UNINSTALLER   "Uninstall.exe"

Name "${APP_NAME} ${APP_VERSION}"
OutFile "..\setup.exe"
InstallDir "${APP_DIR}"
InstallDirRegKey HKLM "Software\${APP_NAME}" "InstallDir"
RequestExecutionLevel admin
SetCompressor /SOLID lzma

!include "MUI2.nsh"

!define MUI_ABORTWARNING
!define MUI_ICON "${NSISDIR}\Contrib\Graphics\Icons\modern-install.ico"
!define MUI_UNICON "${NSISDIR}\Contrib\Graphics\Icons\modern-uninstall.ico"

!insertmacro MUI_PAGE_WELCOME
!insertmacro MUI_PAGE_LICENSE "files\README.txt"
!insertmacro MUI_PAGE_DIRECTORY
!insertmacro MUI_PAGE_INSTFILES
!define MUI_FINISHPAGE_RUN_TEXT "Открыть справочную систему"
!define MUI_FINISHPAGE_RUN "$INSTDIR\help\index.html"
!insertmacro MUI_PAGE_FINISH

!insertmacro MUI_UNPAGE_CONFIRM
!insertmacro MUI_UNPAGE_INSTFILES

!insertmacro MUI_LANGUAGE "Russian"

Section "Основные файлы" SecMain
  SectionIn RO
  SetOutPath "$INSTDIR"

  File "files\README.txt"

  SetOutPath "$INSTDIR\help"
  File /r "files\help\*.*"

  ; Запись в реестр для деинсталляции
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" \
    "DisplayName" "${APP_NAME} ${APP_VERSION}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" \
    "UninstallString" "$INSTDIR\${UNINSTALLER}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" \
    "DisplayVersion" "${APP_VERSION}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" \
    "Publisher" "${APP_PUBLISHER}"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" \
    "InstallLocation" "$INSTDIR"

  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" \
    "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}" \
    "NoRepair" 1

  WriteUninstaller "$INSTDIR\${UNINSTALLER}"
SectionEnd

Section "Ярлыки" SecShortcuts
  CreateDirectory "$SMPROGRAMS\${APP_NAME}"
  CreateShortcut "$SMPROGRAMS\${APP_NAME}\Справочная система.lnk" \
    "$INSTDIR\help\index.html"
  CreateShortcut "$SMPROGRAMS\${APP_NAME}\Удалить ${APP_NAME}.lnk" \
    "$INSTDIR\${UNINSTALLER}"
SectionEnd

Section "Uninstall"
  Delete "$INSTDIR\README.txt"
  Delete "$INSTDIR\${UNINSTALLER}"
  RMDir /r "$INSTDIR\help"
  RMDir "$INSTDIR"

  Delete "$SMPROGRAMS\${APP_NAME}\Справочная система.lnk"
  Delete "$SMPROGRAMS\${APP_NAME}\Удалить ${APP_NAME}.lnk"
  RMDir "$SMPROGRAMS\${APP_NAME}"

  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\${APP_NAME}"
  DeleteRegKey HKLM "Software\${APP_NAME}"
SectionEnd
