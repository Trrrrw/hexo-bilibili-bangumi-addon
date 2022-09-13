import httpx
import json

def get_data(id):
    class bangumis:
        score = "-"
        des = "-"
        wish = "-"
        doing = "-"
        collect = "-"
        totalCount = "-"

    url = "https://api.bgm.tv/v0/subjects/"+id
    headers = {
        'user-agent': 'Trrrrw/hexo-bilibili-bangumi-addon(https://github.com/Trrrrw/hexo-bilibili-bangumi-addon)',
        'accept': 'application / json'
    }
    re = httpx.get(url=url, headers=headers)
    dirt_data = json.loads(re.text)

    try:
        bangumis.score = dirt_data['rating']['score']
    except:
        bangumis.score = "-"
    try:
        bangumis.des = dirt_data['summary']
    except:
        bangumis.des = "-"
    try:
        bangumis.wish = dirt_data['collection']['wish']
    except:
        bangumis.wish = "-"
    try:
        bangumis.doing = dirt_data['collection']['doing']
    except:
        bangumis.doing = "-"
    try:
        bangumis.collect = dirt_data['collection']['collect']
    except:
        bangumis.collect = "-"

    if dirt_data['infobox'][2]['key'] == "话数":
        bangumis.totalCount = dirt_data['infobox'][2]['value']
    else:
        bangumis.totalCount = "12"

    return bangumis


def read():
    print("\n读取json信息")
    with open("./source/_data/bangumis.json", "r", encoding="utf-8") as js_file:
        js_txt = js_file.read()
    py_data = json.loads(js_txt)
    watching = py_data.get("watching")
    watched = py_data.get("watched")
    for i in watching:
        i["type"] = "番剧"
        print("\n正在获取 " + i["title"] + " 的信息")
        bangumis = get_data(i["id"])
        i["score"] = bangumis.score
        i["des"] = bangumis.des
        i["wish"] = bangumis.wish
        i["doing"] = bangumis.doing
        i["collect"] = bangumis.collect
        i["totalCount"] = "全" + str(bangumis.totalCount) + "话"

    for j in watched:
        j["type"] = "番剧"
        print("\n正在获取 " + j["title"] + " 的信息")
        bangumis = get_data(j["id"])
        j["score"] = bangumis.score
        j["des"] = bangumis.des
        j["wish"] = bangumis.wish
        j["doing"] = bangumis.doing
        j["collect"] = bangumis.collect
        j["totalCount"] = "全" + str(bangumis.totalCount) + "话"

    return py_data


def write(py_data):
    print("\n写入新的json")
    with open("./source/_data/bangumis.json", "w", encoding="utf-8") as js_output:
        js_output_txt = json.dumps(py_data, ensure_ascii=False)
        js_output.write(js_output_txt)


if __name__ == "__main__":
    write(read())
    print("\n完成")
