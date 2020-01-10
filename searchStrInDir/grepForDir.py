import os
import subprocess

cmd = "grep -r FileObserver C:\\Users\\Administrator\\Desktop\\NativeSubprocess"


def GETAPI(cmd, api):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                         stdin=subprocess.PIPE, shell=True)
    (output, err) = p.communicate()
    info =str(output,'utf8')
    if info !='':
        return api+"===》》》[" + info + "]"
        # return 'result'


if __name__ == "__main__":
    dir = input("请输入下载目录:")
    apis = ['getInstalledPackages', "getContentResolver", "sendTextMessage", "sendMultipartTextMessage",
            "abortBroadcast", "content://sms/inbox", "getLine1Number", "pm install", "getSubscriberId",
            "Browser.BOOKMARKS_URI", "TelephonyManager.CALL_STATE_RINGING", "DevicePolicyManager.ACTION_ADD_DEVICE_ADMIN",
            "android.intent.action.CALL", "MediaRecorder", "getNetworkOperator", "getDeviceId", "getSubscriberId", "getRunningAppProcesses",
            "getSimOperator", "getCellLocation"]

    for a in apis:
        cmd = 'grep -r "'+ a +'" '+ dir
        # print(cmd)
        result = GETAPI(cmd, a)
        if result is not None:
            print(result)
