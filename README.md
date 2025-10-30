# 1. 安装

## 1.1 环境(uv)

uv installation

```bash
uv sync
cd submodules/unitree_sdk2_python
pip install . -e
```

## 1.2 (conda)

create environment

```bash
conda create -n g1-control python=3.10 pinocchio=3.1.0 numpy=1.26.4 -c conda-forge
conda install -c conda-forge hatch
```

tele install

```bash
git clone https://github.com/unitreerobotics/xr_teleoperate.git
cd xr_teleoperate
git submodule update --init --depth 1
cd teleop/televuer
pip install -e .
```

dex install

```bash
cd ../robot_control/dex-retargeting/
pip install -e .
```

xr install

```bash
cd ../../../
pip install -r requirements.txt
```

unitree_sdk2_python install

```bash
git clone https://github.com/unitreerobotics/unitree_sdk2_python.git
cd unitree_sdk2_python
pip install -e .
```



## 1.2 控制灵巧手



## 1.3 控制摄像头