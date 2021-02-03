https://wd7.ir/there-are-no-remote-desktop-license-servers-available.html

اگر از ویندوز سرور استفاده می کنید و بعد از مدتها کار با خطای زیر مواجه شدین پس این مطلب رو بخونید:
```
---------------------------
Remote Desktop Connection
—-------------------------
The remote session was disconnected because there are no Remote Desktop License Servers available to provide a license.
Please contact the server administrator.
—-------------------------
OK   Help   
—-------------------------
```
اگر دسترسی فیزیکی و یا VNC به سیستم ندارید این راه کار کارگشای شما نیست.اما اگر این دسترسی ها رو دارید ادامه مطلب رو بخونید.

کلید start+R رو بزنید تا صفحه اجرای دستورات ویندوز باشه بشه و بعد بنویسین: regedit تا صفحه ویرایش رجیستری ویندوز باز شه.

نکته :  دستکاری این رجیستری کمی حساسه /تو کارهایی که انجام میدین حتما دقت کنید.

در رجیستری به مسیر زیر برید:
```
hkey_local_machine\system\CurrentControlSet\Control\Terminal Server\RCM\GracePeriod
```
تو این مسیر یه reg binary هست که اگر حذف بشه مشکل این خطا حل میشه.اما برای حذفش خطا میده ویندوز و باید پرمیژن پوشه رو به یوزر خودتون تغییر بدین تا بتونین این کار رو انجام بدین.

پس روی پوشه GracePeriod کلیک راست کرده و Permissions رو بزنید.

بعد روی گزینه Advanced

و بعد از اون در پنجره باز شده جلوی قسمت Owner روی دکمه change کلیک کنید و اونو روی یوزر خودتون (administrator معمولا ) بذارید.تمام دسترسی ها رو هم بهش بدید و تمام پنجره ها رو اکی کنید.

حالا توی همین پوشه اون reg binary رو کلیک راست کنید و حذفش کنید.

حالا سیستم رو ری استارت کنید تا مشکل بالا حل بشه.

این مشکل ظاهرا هر ۱۲۰ روز یه بار رخ میده و برای همین شاید مایل باشین کاری کنین که خودکار این مورد انجام بشه و بعدها باز دردسر ساز نشه.

برای این مورد میتونید یه فایل bat بسازین و توی schedule ویندوز ست کنین تا دوره ای ، مثلا هر ۳ ماه یه بار اجرا بشه.

محتوای فایل بت:
```
@echo off
REG DELETE \\ServerName\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Terminal Server\RCM\GracePeriod /v L$RTMTIMEBOMB_1320153D-8DA3-4e8e-B27B-0D888223A588
net stop termservice
timeout 30
net start termservice
```
دوتا نکته قبل از استفاده از کد بالا:

۱- ServerName رو با اسم سرور خودتون عوض کنید.

۲- کلید L$RTMTIMEBOMB_1320153D-8DA3-4e8e-B27B-0D888223A588 رو طبق کلید موجود در رجیستری خودتون ست کنید.

۳- مجوز اجرای این دستور رو در قسمت زمان بندی ویندوز بر روی یوزری که دسترسی دادید بذارید.

۴- صحت عملکرد این فایل bat تضمین نمیشه،اما میتونین تست کنید

