@echo off
title ����ǿ�Ƽ���data_V1.03      һ��7T / 7TProͨ�ð�      PowerBy�����JOJO������
echo.
echo.
echo �뽫�ֻ�������bootloader
echo.
echo.
:choice
set /P c=�Ƿ�ȷ��������ݣ��״�ȡ��ǿ�Ƽ��ܱ�����գ�[Y/N]?
if /I "%c%" EQU "Y" goto :wipe
if /I "%c%" EQU "N" goto :continue
goto :wipe
:wipe
platform\fastboot.exe -w
goto :continue
:continue
platform\fastboot.exe flash boot_a img\boot.img
platform\fastboot.exe flash boot_b img\boot.img
platform\fastboot.exe flash dsp_a img\dsp.img
platform\fastboot.exe flash dsp_b img\dsp.img
platform\fastboot.exe flash dtbo_a img\dtbo.img
platform\fastboot.exe flash dtbo_b img\dtbo.img
platform\fastboot.exe flash qupfw_a img\qupfw.img
platform\fastboot.exe flash qupfw_b img\qupfw.img
platform\fastboot.exe flash multiimgoem_a img\multiimgoem.img
platform\fastboot.exe flash multiimgoem_b img\multiimgoem.img
platform\fastboot.exe flash uefisecapp_a img\uefisecapp.img
platform\fastboot.exe flash uefisecapp_b img\uefisecapp.img
platform\fastboot.exe flash recovery_a img\recovery.img
platform\fastboot.exe flash recovery_b img\recovery.img
platform\fastboot.exe --disable-verity flash vbmeta_a img\vbmeta.img
platform\fastboot.exe --disable-verity flash vbmeta_b img\vbmeta.img
platform\fastboot.exe --disable-verity flash vbmeta_system_a img\vbmeta_system.img
platform\fastboot.exe --disable-verity flash vbmeta_system_b img\vbmeta_system.img
platform\fastboot.exe flash opproduct_a img\opproduct.img
platform\fastboot.exe flash opproduct_b img\opproduct.img
platform\fastboot.exe reboot fastboot
platform\fastboot.exe flash system_a img\system.img
platform\fastboot.exe flash system_b img\system.img
platform\fastboot.exe flash vendor_a img\vendor.img
platform\fastboot.exe flash vendor_b img\vendor.img
platform\fastboot.exe flash product_a img\product.img
platform\fastboot.exe flash product_b img\product.img
:choice
set /P c=�Ƿ�ˢ��TWRP��Ŀǰ�ǹٷ�rec��[Y/N]?      
if /I "%c%" EQU "Y" goto :flash-TWRP
if /I "%c%" EQU "N" goto :ok
goto :flash_TWRP
:flash-TWRP
@echo 1.7T
@echo 2.7TPro
set /P c=��ѡ���ֻ��ͺ� [1/2]?      
if /I "%c%" EQU "1" goto :flash-TWRP_7T
if /I "%c%" EQU "2" goto :flash-TWRP_7TP
platform\fastboot.exe reboot bootloader
goto :flash_TWRP_7T
:flash-TWRP_7T
platform\fastboot.exe devices
platform\fastboot.exe flash recovery_a img\twrp_7t.img
platform\fastboot.exe flash recovery_b img\twrp_7t.img
goto :ok
goto :flash_TWRP_7T
:flash-TWRP_7TP
platform\fastboot.exe devices
platform\fastboot.exe flash recovery_a img\twrp_7tp.img
platform\fastboot.exe flash recovery_b img\twrp_7tp.img
goto :ok
:ok
platform\fastboot.exe reboot 
pause