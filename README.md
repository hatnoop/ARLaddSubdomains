## 工具说明

通过灯塔ARL的自定义"域名查询插件"功能，将其他渠道收集到的子域名添加至项目

## 使用方法

修改配置文件，在config-docker.yaml中添加

```
QUERY_PLUGIN:
	sortSubdomain:
    api_key: "http://192.168.5.247:9988/"
    enable: true
```

sortSubdomain.py

放置在docker-compose.yml同目录下，启动项目后执行

```
docker-compose up -d

docker-compose cp sortSubdomain.py worker:/code/app/services/dns_query_plugin/

#重启容器
docker-compose restart worker
```

server.py

同目录下保存的内容：[domain].txt，如：tophant.com.txt，存放子域名信息，一行一个

```
python3 server.py
```

