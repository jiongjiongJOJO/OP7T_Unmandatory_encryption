import os
import shutil
os.system('title 禁用强制加密data_V1.02      一加7T / 7TPro通用版      PowerBy：囧囧JOJO、卿诉')
root = os.getcwd()

password = ''
password += 'One'
password += 'Plus'
password += 'ADT'

while True:
    while True:
        psw = input('请输入密码（加群305769183获取）：')
        if (psw == password):
            break


    #解压卡刷包zip文件,提取出payload.bin文件到\temp文件夹中
    os.system('cls')
    print('\n\n')
    print('      正在解压zip文件')
    print('\n\n')
    try:
        os.system('md temp 2>nul')
    except:
        print('创建文件夹temp失败，工具停止工作！')
        os.system('pause')
        break
    zip_path = input('请将完整的zip刷机包拖入本窗口，并按下回车键：')
    extract_path = root + '\\temp'
    try:
        cmd = os.system('tools\\7z.exe e %s -o%s *.bin'%(zip_path,extract_path))
    except:
        print('解压zip刷机包失败，工具停止工作！')
        os.system('pause')
        break
    else:
        if(cmd != 0):
            print('解压zip刷机包失败，工具停止工作！')
            os.system('pause')
            break


    #解压payload.bin文件，生成img镜像文件到temp文件夹中
    os.system('cls')
    print('\n\n')
    print('      正在拆payload.bin文件')
    print('      过程比较漫长，请耐心等待')
    print('\n\n')
    try:
        os.chdir(extract_path)
    except:
        print('temp文件夹出现异常，工具停止工作！')
        os.system('pause')
        break
    try:
        cmd = os.system(root+'\\tools\\python\\python.exe '+root+'\\tools\\payload_dumper.py '+root+'\\temp\\payload.bin')
    except:
        print('解payload.bin文件失败，工具停止工作！')
        os.system('pause')
        break
    else:
        if(cmd != 0):
            print('解payload.bin文件失败，工具停止工作！')
            os.system('pause')
            break
    files_list = os.listdir(os.getcwd())
    try:
        for file in files_list:
            if('.img' in file):
                if('vendor.img' in file):
                    continue
                else:
                    cmd = os.system('move /Y '+os.getcwd()+'\\'+file+' '+root+'\\flash\\img')
                    if(cmd != 0):
                        print('移动temp内文件失败，请尝试手动移动后再继续！\n请将temp文件夹下除“vendor.img”文件外的所有文件移动到“flash\\img”文件夹内\n如无法手动移动，请重启或咨询群内其他成员。')
                        os.system('pause')
    except:
        print('移动temp内文件失败，请尝试手动移动后再继续！\n请将temp文件夹下除“vendor.img”文件外的所有文件移动到“flash\\img”文件夹内\n如无法手动移动，请重启或咨询群内其他成员。')
        os.system('pause')
    else:
        print('文件移动完成!')
    try:
        cmd = os.system('del payload.bin')
    except:
        print('删除payload.bin文件失败，不影响程序运行，但占用系统空间，可尝试手动删除！')
        os.system('pause')
    else:
        if(cmd != 0):
            print('删除payload.bin文件失败，不影响程序运行，但占用系统空间，可尝试手动删除！')
            os.system('pause')


    #解包vendor.img
    os.system('cls')
    print('\n\n')
    print('      正在转换固件')
    print('      过程比较漫长，请耐心等待')
    print('\n\n')
    try:
        cmd = os.system(root+'\\tools\\python\\python.exe '+root+'\\tools\\imgextractor.py '+root+'\\temp\\vendor.img')
    except:
        print('解包vendor出错，工具停止工作！')
        os.system('pause')
        break
    else:
        if(cmd != 0):
            print('解包vendor出错，工具停止工作！')
            os.system('pause')
            break

        

    #修改并打包vendor.img
    os.system('cls')
    print('\n\n')
    print('      正在修改并打包固件')
    print('      过程比较漫长，请耐心等待')
    print('\n\n')
    os.system('ping 127.1 -n 5 >nul')
    try:
        os.chdir(os.getcwd()+'\\vendor\\etc')
    except:
        print('vendor目录异常，工具停止工作！')
        os.system('pause')
        break
    try:
        file = open('fstab.qcom',mode='r')
        content = file.read()
        file.close()
        file = open('fstab.qcom',mode='w')
        content = content.replace('fileencryption=ice,','')
        file.write(content)
        file.close()
        newline = '\n'
        with open('fstab.qcom', newline=None, encoding='utf-8') as infile:
            content = infile.read()
            content = content.replace('\r\n','\n')
            with open('fstab.qcom', 'w', newline=newline, encoding='utf-8') as outfile:
                outfile.writelines(content)
    except:
        print('读或修改vendor内文件失败，工具停止工作！')
        os.system('pause')
        break
    print('文件修改完毕，开始打包文件！')
    try:
        file = open(root + '\\temp\\vendor_size.txt','r')
        vendor_size = str(int(file.read())+104857600)
        file.close()
    except:
        print('读原vendor.img镜像大小错误，已启用备用方案,占用空间可能略微增加，后续会删除！')
        try:
            os.chdir(root+'\\temp')
        except:
            print('temp文件夹出错，工具停止工作！')
            os.system('pause')
            break
        try:
            cmd = os.system(root+'\\tools\\make_ext4fs.exe -l 2048000000 -L vendor -a vendor -S vendor_file_contexts -C vendor_fs_config -T 2009110000 vendor.img vendor')
        except:
            print('文件打包错误，工具停止工作！')
            os.system('pause')
            break
        else:
            if(cmd != 0):
                print('文件打包错误，工具停止工作！')
                os.system('pause')
                break
    try:
        os.chdir(root+'\\temp')
    except:
        print('temp文件夹出错，工具停止工作！')
        os.system('pause')
        break
    try:
        cmd = os.system(root+'\\tools\\make_ext4fs.exe -l '+vendor_size+' -L vendor -a vendor -S vendor_file_contexts -C vendor_fs_config -T 2009110000 vendor.img vendor')
    except:
        print('文件打包错误，工具停止工作！')
        os.system('pause')
        break
    else:
        if(cmd != 0):
            print('文件打包错误，工具停止工作！')
            os.system('pause')
            break

    #清理垃圾
    try:
        os.chdir(root)
    except:
        print('进入工具目录失败，停止运行')
        os.system('pause')
        break
    os.system('cls')
    print('\n\n')
    print('      清理缓存文件')
    print('      准备刷入已修改的文件')
    print('\n\n')
    try:
        cmd = os.system('move /Y temp\\vendor.img flash\\img')
    except:
        print('移动temp内文件失败，请尝试手动移动后再继续！\n请将temp文件夹下“vendor.img”文件移动到“flash\\img”文件夹内\n如无法手动移动，请重启或咨询群内其他成员。')
        os.system('pause')
    else:
        if(cmd != 0):
            print('移动temp内文件失败，请尝试手动移动后再继续！\n请将temp文件夹下“vendor.img”文件移动到“flash\\img”文件夹内\n如无法手动移动，请重启或咨询群内其他成员。')
            os.system('pause')
    try:
        shutil.rmtree('temp')
    except:
        print('删除文件夹temp失败，文件夹可能被占用\n跳过删除文件夹，请手动删除temp文件夹后继续操作！')
        os.system('pause')


    #flash-all
    os.system('cls')
    print('\n\n')
    print('      请将手机重启到bootloader再选择Y或N')
    print('      BootLoader进入方法：')
    print('            完全关机状态下，音量与电源【三键】同时按住')
    print('            等待屏幕出现【Fastboot】松手即可')
    print('      进入BootLoader之后，用数据线连接手机和电脑！')
    print('\n\n')
    try:
        install = input('是否需要安装驱动(如果不知道是什么的话直接选择Y，接着安装弹出的窗口就行。)[Y/N]?')
        if(install == 'Y' or install == 'y'):
            os.system(root+'\\tools\\drive\\DPInst_x64.exe')
    except:
        print('安装驱动失败，请尝试手动安装\n打开本目录下的“tools”下的“drive”文件夹\n手动打开“install.bat”文件\n安装完成后继续\n如果不能手动安装完成，请咨询群内成员！')
        os.system('pause')
    try:
        os.chdir(root+'\\flash')
    except:
        print('进入flash文件夹失败，工具停止工作\n请手动打开“flash”文件夹下的“flash-all.bat”文件，并按照提示刷入。')
        os.system('pause')
        break
    try:
        erase = input('是否确认清除数据【首次解除Data强制加密 必须选Y】[Y/N]? ')
        if(erase == 'Y' or erase == 'y'):
            os.system(os.getcwd() + '\\platform\\fastboot.exe -w')
    except:
        print('清空数据失败，可选择继续运行，后续手动格式化手机！')
        erase_continue = input('是否继续运行？【Y/N】')
        if(erase_continue != 'Y' and erase_continue != 'y'):
            print('停止格式化手机，工具停止工作！')
            os.system('pause')
            break


    try:
        image = ['boot.img','dsp.img','dtbo.img','qupfw.img','multiimgoem.img','uefisecapp.img','recovery.img']
        flash_error = False
        for i in image:
            cmd = os.system(os.getcwd() + '\\platform\\fastboot.exe flash '+i[:-4]+'_a img\\'+i)
            if(cmd != 0):
                print('刷入'+i+'失败，后续工作无法进行\n请尝试手动运行“flash”文件夹下的“flash-all.bat”文件，并按照提示刷入。')
                os.system('pause')
                break
            cmd = os.system(os.getcwd() + '\\platform\\fastboot.exe flash '+i[:-4]+'_b img\\'+i)
            if(cmd != 0):
                print('刷入'+i+'失败，后续工作无法进行\n请尝试手动运行“flash”文件夹下的“flash-all.bat”文件，并按照提示刷入。')
                os.system('pause')
                flash_error = True
                break
        if(flash_error):
            break
        cmd = os.system(os.getcwd() + '\\platform\\fastboot.exe --disable-verity flash vbmeta_a img\\vbmeta.img')
        cmd += os.system(os.getcwd() + '\\platform\\fastboot.exe --disable-verity flash vbmeta_b img\\vbmeta.img')
        cmd += os.system(os.getcwd() + '\\platform\\fastboot.exe --disable-verity flash vbmeta_system_a img\\vbmeta_system.img')
        cmd += os.system(os.getcwd() + '\\platform\\fastboot.exe --disable-verity flash vbmeta_system_b img\\vbmeta_system.img')
        cmd += os.system(os.getcwd() + '\\platform\\fastboot.exe flash opproduct_a img\\opproduct.img')
        cmd += os.system(os.getcwd() + '\\platform\\fastboot.exe flash opproduct_b img\\opproduct.img')
    except:
        print('刷入基础镜像失败，后续工作无法进行\n请尝试手动运行“flash”文件夹下的“flash-all.bat”文件，并按照提示刷入。')
        os.system('pause')
        break
    
    else:
        if(cmd != 0):
            print('刷入基础镜像失败，后续工作无法进行\n请尝试手动运行“flash”文件夹下的“flash-all.bat”文件，并按照提示刷入。')
            os.system('pause')
            break
        
    try:
        cmd = os.system(os.getcwd() + '\\platform\\fastboot.exe reboot fastboot')
        cmd += os.system(os.getcwd() + '\\platform\\fastboot.exe flash system_a img\\system.img')
        cmd += os.system(os.getcwd() + '\\platform\\fastboot.exe flash system_b img\\system.img')
        cmd += os.system(os.getcwd() + '\\platform\\fastboot.exe flash vendor_a img\\vendor.img')
        cmd += os.system(os.getcwd() + '\\platform\\fastboot.exe flash vendor_b img\\vendor.img')
        cmd += os.system(os.getcwd() + '\\platform\\fastboot.exe flash product_a img\\product.img')
        cmd += os.system(os.getcwd() + '\\platform\\fastboot.exe flash product_b img\\product.img')
    except:
        print('刷入系统核心镜像失败\n请尝试手动运行“flash”文件夹下的“flash-all.bat”文件，并按照提示刷入。')
        os.system('pause')
        break
    else:
        if(cmd != 0):
            print('刷入系统核心镜像失败\n请尝试手动运行“flash”文件夹下的“flash-all.bat”文件，并按照提示刷入。')            
            os.system('pause')
            break
    try:
        TWRP = input('是否刷入TWRP（目前是官方rec）[Y/N]?')
        if(TWRP == 'Y' or TWRP == 'y'):
            os.system(os.getcwd() + '\\platform\\fastboot.exe reboot bootloader')
            while True:
                print('请选择您的手机型号：\n1.7T\n2.7T Pro\n')
                device = input()
                if(device == '1'):
                    os.system(os.getcwd() + '\\platform\\fastboot.exe devices')
                    os.system(os.getcwd() + '\\platform\\fastboot.exe flash recovery_a img\\twrp_7t.img')
                    os.system(os.getcwd() + '\\platform\\fastboot.exe flash recovery_b img\\twrp_7t.img')
                    break
                elif(device == '2'):
                    os.system(os.getcwd() + '\\platform\\fastboot.exe devices')
                    os.system(os.getcwd() + '\\platform\\fastboot.exe flash recovery_a img\\twrp_7tp.img')
                    os.system(os.getcwd() + '\\platform\\fastboot.exe flash recovery_b img\\twrp_7tp.img')
                    break
                else:
                    print('您的输入有误，请重新输入！\n')
    except:
        print('刷入TWRP失败，跳过刷入，后续想要刷入请自己刷')
        os.system('pause')
    print('所有文件已经成功刷入，请选择要重启进哪个模式？')
    reboot = input('    1.系统\n    2.recovery或TWRP(主要在于是否已刷入TWRP)\n    3.BootLoader\n')
    if(reboot == '1'):
        os.system(os.getcwd() + '\\platform\\fastboot.exe reboot')
        print('重启中……')
    elif(reboot == '2'):
        os.system(os.getcwd() + '\\platform\\fastboot.exe reboot recovery')
        print('重启中……')
    elif(reboot == '3'):
        os.system(os.getcwd() + '\\platform\\fastboot.exe reboot bootloader')
        print('重启中……')
    else:
        print('输入错误，请自行重启手机！')
    delete_img = input('是否要清空刷机过程中产生的img文件（大约占8G）[Y/N]？')
    if(delete_img == 'Y' or delete_img == 'y'):
        try:
            os.chdir(root+'\\flash\\img')
        except:
            print('进入img文件夹失败，跳过删除文件，请自行删除！')
            os.system('pause')
            print('恭喜你，全部完成！')
            os.system('pause')
            break
        try:
            files_list = os.listdir()
            for file in files_list:
                if('twrp' in file):
                    continue
                else:
                    cmd = os.system('del '+file)
                    if(cmd != 0):
                        print('删除'+file+'失败，请手动删除')
        except:
            print('删除img文件失败，请手动删除(注意保留twrp_*.img)，以免后续无法刷入twrp')
    print('恭喜你，全部完成！')
    os.system('pause')
    break

