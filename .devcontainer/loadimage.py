import os
import subprocess
import time
from datetime import datetime
import logging

# 198 和 云桌面， 每过一个小时，自动从 github 上拉取镜像：docker pull ghcr.io/eviljoker/codespace_kubernets_devcontainer:latest

# 配置日志
log_file = 'output.log'
logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')


ip_desktop = "10.90.253.79"
ip_198 = "10.90.30.198"
image_name = "ghcr.io/eviljoker/product_imagemagic_devcontainer:latest"


# 198环境：直接 docker pull ghcr.io/eviljoker/codespace_kubernets_devcontainer:lates
def load_image_in_198():
    logging.info("Loading image in 198 environment...")
    try:
        result = subprocess.run(
            ["docker", "pull", image_name], capture_output=True, text=True, check=True)
        logging.info(result.stdout)
        logging.info("Image loaded successfully in 198 environment.")
    except subprocess.CalledProcessError as e:
        logging.info(f"Error loading image in 198 environment: {e.stderr}")


# 云桌面：不能直连，只能离线下载。 从 198 环境 docker save 和 docker load 下来即可。
def load_image_in_desktop():
    logging.info("Loading image in desktop environment...")
    try:
        if compare_image_id(image_name) is True:
            logging.info("image  is latested")
            return
        
        
        # 登录到 198环境，执行 docker save 命令
        save_command = ["ssh", "sunqiyuan@" + ip_198,
                        f"docker save -o image.tar {image_name}"]
        result = subprocess.run(
            save_command, capture_output=True, text=True, check=True)
        logging.info(result.stdout)

        # 从 198 环境拷贝到 desktop 环境
        result = subprocess.run(["scp", "sunqiyuan@" + ip_198 + ":image.tar",
                                "."], capture_output=True, text=True, check=True)
        logging.info(result.stdout)

        # 在 desktop 环境执行 docker load 命令
        load_command = ["docker", "load", "-i", "image.tar"]
        result = subprocess.run(
            load_command, capture_output=True, text=True, check=True)
        logging.info(result.stdout)

        # 清理临时文件
        os.remove("image.tar")

        logging.info("Image loaded successfully in desktop environment.")
    except subprocess.CalledProcessError as e:
        logging.info(f"Error loading image in desktop environment: {e.stderr}")


def compare_image_id(image_name):
    local_result = subprocess.run(
        ["docker", "images", "-q", image_name], capture_output=True, text=True)
    local_id = local_result.stdout.strip()

    remote_result = subprocess.run(
        ["ssh", "sunqiyuan@" + ip_198, f"docker images -q {image_name}"],
        capture_output=True, text=True)
    remote_id = remote_result.stdout.strip()

    return local_id == remote_id

# 在 load_image_in_desktop 函数中，比较两个环境的镜像ID是否一致
def compare_image_ids(local_id, remote_id):
    return local_id == remote_id



if __name__ == "__main__":
# 主函数
    while True:
        # nohup python3.7 loadimage.py > /dev/null 2>&1 &

        current_date = datetime.now().strftime("%Y-%m-%d")
        start_time = time.time()
        # 获取当前IP地址
        hostname = os.popen("hostname").read()
        print(f"Current Date: {current_date}")
        # 198
        if hostname.startswith("XA-AT"):
            load_image_in_198()

        # 云桌面
        elif hostname.startswith("LIN-F57BA0762A6.zte.intra"):
            load_image_in_desktop()
        end_time = time.time()
        elapsed_time = end_time - start_time
        #每小时拉取最新的Docker镜像
        time.sleep(3600)




