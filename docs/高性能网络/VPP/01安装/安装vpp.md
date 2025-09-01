# Ubuntu

直接从官方目录克隆：

```bash
git clone https://github.com/FDio/vpp.git

#选择你想要的版本，也就是分支名   我们这里选择 stable/2506
git checkout stable/2506
```





编译：

```bash
cd vpp/

#执行编译脚本
./extras/vagrant/build.sh

#编译完成后应该可以看到deb安装文件
ls build-root/

cd build-root/

#安装所有的deb文件
sudo apt install ./*.deb

#可以看到vpp的启动文件
ls /etc/vpp
```

