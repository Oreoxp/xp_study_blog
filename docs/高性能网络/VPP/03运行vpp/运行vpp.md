### **运行与交互 (Running VPP)**

#### 0. 运行前的配置

在启动 VPP 实例之前，我们需要先为其准备好启动配置文件。

通常情况下，VPP 的主配置文件位于 /etc/vpp/startup.conf。但在生产环境中，我们通常只修改这一个文件来运行单个 VPP 实例。

为了本教程的学习，我们将创建并使用多个独立的 VPP 实例来构建网络拓扑。为了让它们能在一台主机上同时运行而不互相干扰，我们需要为每个实例创建专属的配置文件。

##### **关键配置项解析**

当同时运行多个 VPP 实例时，必须为每个实例指定一个唯一的“名称”或“前缀 (prefix)”，以避免资源冲突。我们的配置文件主要关注以下三个部分：

1. **unix { cli-listen ... }**
   - **作用:** 指定 vppctl 命令行工具连接到此 VPP 实例所使用的 Unix Socket 文件。
   - **为什么需要独立:** 这就像是为每个 VPP 实例安装一个专属的“门铃”（例如 /run/vpp/cli-vpp1.sock）。当我们想控制第一个 VPP 实例时，就去按第一个门铃；想控制第二个时，就去按第二个。这样可以精确地管理不同的实例。
2. **api-segment { prefix ... }**
   - **作用:** 为 VPP 实例在共享内存 (/dev/shm/) 中创建的文件指定一个独特的前缀。
   - **为什么需要独立:** VPP 实例之间通过共享内存进行通信和状态管理。如果不指定不同的前缀（如 vpp1, vpp2），两个实例就会尝试使用和修改相同的文件，导致严重冲突和崩溃。
3. **plugins { plugin dpdk_plugin.so { disable } }**
   - **作用:** 禁用 DPDK 插件。
   - **为什么需要禁用:** DPDK 插件在初始化时会尝试获取文件锁以直接控制物理硬件。在一台主机上，通常只有一个进程可以这样做。由于我们的教程环境不需要直接操作物理网卡，并且要运行多个实例，因此直接禁用它可以避免冲突并简化设置。

##### **创建启动文件**

现在，请创建 startup1.conf 和 startup2.conf 这两个文件。你可以将它们放置在任何目录下，因为我们稍后会在启动 VPP 时明确指定它们的路径。

**文件 1: startup1.conf**

codeCode

```
unix {
  cli-listen /run/vpp/cli-vpp1.sock
}

api-segment {
  prefix vpp1
}

plugins {
  plugin dpdk_plugin.so { disable }
}
```

**文件 2: startup2.conf**

codeCode

```
unix {
  cli-listen /run/vpp/cli-vpp2.sock
}

api-segment {
  prefix vpp2
}

plugins {
  plugin dpdk_plugin.so { disable }
}
```

------





#### **1. VPP 的运行模式**

VPP 是一个用户态 (userspace) 程序。

*   **生产环境 (Production):** 在生产环境中，VPP 通常与 DPDK（用于连接物理网卡）或 Vhost-user（用于连接虚拟机）一起运行。在这些场景下，通常只会运行**单个 VPP 实例**。
*   **学习/教程环境 (Tutorial):** 为了学习和实验，我们会频繁地运行**多个 VPP 实例**，并将它们相互连接以构建出不同的网络拓扑。VPP 对此提供了很好的支持。

这篇笔记将重点关注如何在教程环境中启动和管理 VPP 实例。

---

#### **2. 启动一个 VPP 实例**

我们将使用之前在环境设置中创建的配置文件来启动 VPP。

**启动命令:**
```bash
sudo /usr/bin/vpp -c startup1.conf
```
*   `sudo`: VPP 需要 root 权限来创建网络接口和管理内存。
*   `/usr/bin/vpp`: VPP 的主程序可执行文件。
*   `-c startup1.conf`: `-c` 参数用于指定启动时使用的配置文件。

成功启动后，你会看到 VPP 加载各个插件的日志信息：

```
vlib_plugin_early_init:361: plugin path /usr/lib/vpp_plugins:/usr/lib/vpp_plugins
load_one_plugin:189: Loaded plugin: abf_plugin.so (ACL based Forwarding)
load_one_plugin:189: Loaded plugin: acl_plugin.so (Access Control Lists)
load_one_plugin:189: Loaded plugin: avf_plugin.so (Intel Adaptive Virtual Function (AVF) Device Plugin)
... ...
```

---



#### **4. 使用 `vppctl` 与 VPP 交互**

`vppctl` 是与 VPP 实例进行交互的命令行工具。

**连接到 VPP Shell:**

```bash
sudo vppctl -s /run/vpp/cli-vpp1.sock
```
*   `-s /run/vpp/cli-vpp1.sock`: `-s` 参数指定了要连接的 VPP 实例的 socket 文件，这个路径必须与目标 VPP 实例`startup.conf` 文件中 `cli-listen` 的路径完全一致。

连接成功后，你会看到 VPP 的欢迎界面和命令提示符 `vpp#`：

```
    _______    _        _   _____  ___
 __/ __/ _ \  (_)__    | | / / _ \/ _ \
 _/ _// // / / / _ \   | |/ / ___/ ___/
 /_/ /____(_)_/\___/   |___/_/  /_/

vpp#
```

现在你可以在这个 Shell 中执行 VPP 命令了。例如，查看 VPP 的版本：
```
vpp# show version
vpp v25.06-release built by dxp on dxp-server at 2025-08-26T03:50:15
vpp#
```

> **提示:** 使用 `Ctrl+D` 或者输入 `q` (quit) 可以退出 VPP shell。

---

#### **5. 管理 VPP 进程**

当你完成了实验，尤其是在运行了多个 VPP 实例之后，**确保要将它们彻底关闭**。

你可以使用标准的 Linux 命令来查找和终止 VPP 进程：

1.  **查找 VPP 进程的 PID (进程ID):**
    ```bash
    ps -eaf | grep vpp
    ```
    输出示例：
    ```
    root      2067     1  2 05:12 ?        00:00:00 /usr/bin/vpp -c startup1.conf
    vagrant   2070   903  0 05:12 pts/0    00:00:00 grep --color=auto vpp
    ```
    在上面的例子中，VPP 进程的 PID 是 `2067`。

2.  **终止进程:**
    ```bash
    kill -9 2067
    ```
    * `kill -9` 会强制终止该进程。

3.  **再次检查以确认进程已被终止:**
    ```bash
    ps -eaf | grep vpp
    ```
    如果只剩下 `grep` 自己的进程，说明 VPP 已经被成功关闭了。
