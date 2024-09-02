# Beyond Compare 5 Keygen
用于生成 Beyond Compare 5.x 版本注册密钥
## 前置工作
使用 010Editor 等二进制工具，修改 Beyond Compare 可执行文件中内置的 RSA 密钥

修改前：
```
++11Ik:7EFlNLs6Yqc3p-LtUOXBElimekQm8e3BTSeGhxhlpmVDeVVrrUAkLTXpZ7mK6jAPAOhyHiokPtYfmokklPELfOxt1s5HJmAnl-5r8YEvsQXY8-dm6EFwYJlXgWOCutNn2+FsvA7EXvM-2xZ1MW8LiGeYuXCA6Yt2wTuU4YWM+ZUBkIGEs1QRNRYIeGB9GB9YsS8U2-Z3uunZPgnA5pF+E8BRwYz9ZE--VFeKCPamspG7tdvjA3AJNRNrCVmJvwq5SqgEQwINdcmwwjmc4JetVK76og5A5sPOIXSwOjlYK+Sm8rvlJZoxh0XFfyioHz48JV3vXbBKjgAlPAc7Np1+wk
```
修改后（修改字符串末尾的 `p1+wk` 为 `pn+wk` ）：
```
++11Ik:7EFlNLs6Yqc3p-LtUOXBElimekQm8e3BTSeGhxhlpmVDeVVrrUAkLTXpZ7mK6jAPAOhyHiokPtYfmokklPELfOxt1s5HJmAnl-5r8YEvsQXY8-dm6EFwYJlXgWOCutNn2+FsvA7EXvM-2xZ1MW8LiGeYuXCA6Yt2wTuU4YWM+ZUBkIGEs1QRNRYIeGB9GB9YsS8U2-Z3uunZPgnA5pF+E8BRwYz9ZE--VFeKCPamspG7tdvjA3AJNRNrCVmJvwq5SqgEQwINdcmwwjmc4JetVK76og5A5sPOIXSwOjlYK+Sm8rvlJZoxh0XFfyioHz48JV3vXbBKjgAlPAc7Npn+wk
```
<img src="asserts/01.png" alt="image-20240902170702727" style="zoom:50%;" /> 

## 生成注册密钥

```shell
git clone https://github.com/garfield-ts/BCompare_Keygen.git
cd BCompare_Keygen
pip3 install -r requirements.txt
python3 keygen.py
```
得到可用的注册密钥：
```
--- BEGIN LICENSE KEY ---
3vnA64wCZXBWEmcf56tJXEQSeKhxALVrQrgJBucpS58gQsjXWY7AdKV2bsdaDrDbrwgrD5gZQu4dKiCwCNEbjBGeW7GDpmY4hA78mBGGnqzzprnB4C4Zx716W3GDfmJxkVHdnTREHoApZ4qLCRFuibsQTRfYkaiqJR25p8E2s54vZ2eWz23JPmX8mUAfR3LB6QpYUy9HDMLnRDrQEur123PxDfjWLgFsE3e2YGnqfTXispRFkcYhGAdT6ZztV1fA35SAnoh8CaQr3ff55eddYgeUmE2MDqD5QVSa7aYEsBnc7JqHeG7xppGZPCuCgPpyizqe7hvZNnWsErupC8qe4t6A6unptF
--- END LICENSE KEY -----
```
默认生成的注册密钥使用以下信息：
```
Version: 0x3d
Serial: 0666-8888
Username: Garfield
Company: SZTS
Max users: 1
```
可以修改 `keygen.py` 中的相关参数，自定义注册密钥的信息

<img src="asserts/02.png" alt="image-20240902171032478" style="zoom:50%;" /> 

## 使用密钥进行注册
打开 Beyond Compare 5，此时会弹出 `评估模式错误` 的提示，点击 `输入密钥` 按钮进入注册页面：

<img src="asserts/03.png" alt="image-20240902172200651" style="zoom:50%;" /> 

将脚本生成的注册密钥粘贴到输入框中，点击 `确定` 即可激活。

<img src="/Users/charles/Documents/GitHub/BCompare_Keygen/asserts/04.png" alt="image-20240902172404873" style="zoom:40%;" /> 

<img src="asserts/05.png" alt="image-20240902172829613" style="zoom:50%;" /> 

## TODO

- 命令行方式支持参数传入
- 集成二进制文件 patch 功能
- ……
