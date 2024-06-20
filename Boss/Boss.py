import datetime
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import pymysql


def boss(conn, cursor):
    browser = webdriver.Edge()
    city_map = {

        "北京": ["北京"],
        "天津": ["天津"],
        "河北": ["石家庄", "唐山", "秦皇岛", "邯郸", "邢台", "保定", "张家口", "承德", "沧州", "廊坊", "衡水"],
        "山西": ["太原", "大同", "阳泉", "长治", "晋城", "朔州", "晋中", "运城", "忻州", "临汾", "吕梁"],
        "内蒙古": ["呼和浩特", "包头", "乌海", "赤峰", "通辽", "鄂尔多斯", "呼伦贝尔", "巴彦淖尔", "乌兰察布", "兴安盟",
                   "锡林郭勒盟", "阿拉善盟"],
        "辽宁": ["沈阳", "大连", "鞍山", "抚顺", "本溪", "丹东", "锦州", "营口", "阜新", "辽阳", "盘锦", "铁岭", "朝阳",
                 "葫芦岛"],
        "吉林": ["长春", "吉林", "四平", "辽源", "通化", "白山", "松原", "白城", "延边"],
        "黑龙江": ["哈尔滨", "齐齐哈尔", "鸡西", "鹤岗", "双鸭山", "大庆", "伊春", "佳木斯", "七台河", "牡丹江", "黑河",
                   "绥化", "大兴安岭"],
        "上海": ["上海"],
        "江苏": ["南京", "苏州", "无锡", "常州", "镇江", "南通", "扬州", "盐城", "徐州", "淮安", "连云港", "常熟",
                 "张家港", "太仓", "昆山", "江阴", "宿迁"],
        "浙江": ["杭州", "宁波", "温州", "嘉兴", "湖州", "绍兴", "金华", "衢州", "舟山", "台州", "丽水"],
        "安徽": ["合肥", "芜湖", "蚌埠", "淮南", "马鞍山", "淮北", "铜陵", "安庆", "黄山", "滁州", "阜阳", "宿州",
                 "六安", "亳州", "池州", "宣城"],
        "福建": ["福州", "厦门", "漳州", "泉州", "三明", "莆田", "南平", "龙岩", "宁德"],
        "江西": ["南昌", "景德镇", "萍乡", "九江", "新余", "鹰潭", "赣州", "吉安", "宜春", "抚州", "上饶"],
        "山东": ["济南", "青岛", "淄博", "枣庄", "东营", "烟台", "潍坊", "济宁", "泰安", "威海", "日照", "莱芜", "临沂",
                 "德州", "聊城", "滨州", "菏泽"],
        "河南": ["郑州", "开封", "洛阳", "平顶山", "安阳", "鹤壁", "新乡", "焦作", "濮阳", "许昌", "漯河", "三门峡",
                 "南阳", "商丘", "信阳", "周口", "驻马店"],
        "湖北": ["武汉", "黄石", "十堰", "宜昌", "襄阳", "鄂州", "荆门", "孝感", "荆州", "黄冈", "咸宁", "随州", "恩施",
                 "仙桃", "天门", "潜江", "神农架"],
        "湖南": ["长沙", "株洲", "湘潭", "衡阳", "邵阳", "岳阳", "常德", "张家界", "益阳", "娄底", "郴州", "永州",
                 "怀化", "湘西"],
        "广东": ["广州", "深圳", "珠海", "汕头", "韶关", "佛山", "江门", "湛江", "茂名", "肇庆", "惠州", "梅州", "汕尾",
                 "河源", "阳江", "清远", "东莞", "中山", "潮州", "揭阳", "云浮"],
        "广西": ["南宁", "柳州", "桂林", "梧州", "北海", "防城港", "钦州", "贵港", "玉林", "百色", "贺州", "河池",
                 "来宾", "崇左"],
        "海南": ["海口", "三亚", "三沙", "儋州", "五指山", "琼海", "文昌", "万宁", "东方", "定安", "屯昌", "澄迈",
                 "临高", "白沙", "昌江", "乐东", "陵水"],
        "重庆": ["重庆"],
        "四川": ["成都", "自贡", "攀枝花", "泸州", "德阳", "绵阳", "广元", "遂宁", "内江", "乐山", "南充", "眉山",
                 "宜宾", "广安", "达州", "雅安", "巴中", "资阳", "阿坝", "甘孜", "凉山"],
        "贵州": ["贵阳", "六盘水", "遵义", "安顺", "毕节", "铜仁", "黔西南", "黔东南", "黔南"],
        "云南": ["昆明", "曲靖", "玉溪", "保山", "昭通", "丽江", "普洱", "临沧", "德宏", "怒江", "迪庆", "大理", "楚雄",
                 "红河", "文山", "西双版纳"],
        "西藏": ["拉萨", "日喀则", "昌都", "林芝", "山南", "那曲", "阿里"],
        "陕西": ["西安", "铜川", "宝鸡", "咸阳", "渭南", "延安", "汉中", "榆林", "安康", "商洛"],
        "甘肃": ["兰州", "嘉峪关", "金昌", "白银", "天水", "武威", "张掖", "平凉", "酒泉", "庆阳", "定西", "陇南",
                 "临夏", "甘南"],
        "青海": ["西宁", "海东", "海北", "黄南", "海南", "果洛", "玉树", "海西"],
        "宁夏": ["银川", "石嘴山", "吴忠", "固原", "中卫"],
        "新疆": ["乌鲁木齐", "克拉玛依", "吐鲁番", "哈密", "昌吉", "博尔塔拉", "巴音郭楞", "阿克苏", "克孜勒苏", "喀什",
                 "和田", "伊犁", "塔城", "阿勒泰", "石河子", "阿拉尔", "图木舒克", "五家渠", "北屯", "铁门关"],
        "台湾": ["台北", "高雄", "台中", "花莲", "基隆", "嘉义", "金门", "连江", "苗栗", "南投", "澎湖", "屏东", "台东",
                 "台南", "桃园", "新竹", "宜兰", "彰化"],
        "香港": ["香港"],
        "澳门": ["澳门"]

    }

    # 打开 boss 首页
    index_url = 'https://www.zhipin.com/?city=100010000&ka=city-sites-100010000'
    browser.get(index_url)

    # 模拟点击 互联网/AI 展示出岗位分类
    # XPATH表达式找到 互联网
    show_ele = browser.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div[1]/dl[1]/dd/b')
    show_ele.click()

    today = datetime.date.today().strftime('%Y-%m-%d')

    for i in range(14):
        current_a = browser.find_elements(by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div[1]/dl[1]/div/ul/li['
                                                             '1]/div/a')[
            i]
        current_category = current_a.find_element(by=By.XPATH, value='../../h4').text
        sub_category = current_a.text
        print("{}正在抓取{}--{}".format(today, current_category, sub_category))
        # 模拟点击
        browser.find_elements(by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div[1]/dl[1]/div/ul/li/div/a')[
            i].click()
        # 模拟滑动页面
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(10)
        # 模拟滑动页面
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        job_detail = browser.find_elements(by=By.XPATH,
                                           value='//*[@id="wrap"]/div[2]/div[2]/div/div[1]/div[2]/ul/li')
        for job in job_detail:

            # 岗位名称
            try:
                job_title = job.find_element(by=By.XPATH, value="./div[1]/a/div[1]/span[1]").text.strip()
            except:
                continue
            # 工作地址
            job_location = job.find_element(by=By.XPATH, value="./div[1]/a/div[1]/span[2]/span").text.strip()
            # 企业名称
            job_company = job.find_element(by=By.XPATH, value="./div[1]/div/div[2]/h3/a").text.strip()
            # 行业类型
            job_industry = job.find_element(by=By.XPATH, value="./div[1]/div/div[2]/ul/li[1]").text.strip()
            # 融资情况
            job_finance = job.find_element(by=By.XPATH, value="./div[1]/div/div[2]/ul/li[2]").text.strip()
            try:
                # 企业规模
                job_scale = job.find_element(by=By.XPATH, value="./div[1]/div/div[2]/ul/li[3]").text.strip()
            except:
                job_scale = "无"
            try:
                # 企业福利
                job_welfare = job.find_element(by=By.XPATH, value="./div[2]/div").text.strip()
            except:
                job_welfare = '无'
            # 薪资范围
            job_salary_range = job.find_element(by=By.XPATH, value="./div[1]/a/div[2]/span[1]").text.strip()
            # 工作年限
            job_experience = job.find_element(by=By.XPATH, value="./div[1]/a/div[2]/ul/li[1]").text.strip()
            # 学历要求
            job_education = job.find_element(by=By.XPATH, value="./div[1]/a/div[2]/ul/li[2]").text.strip()
            # 技能要求
            try:
                job_skills = ','.join(
                    [skill.text.strip() for skill in job.find_elements(by=By.XPATH, value="./div[2]/ul/li")])
            except:
                job_skills = '无'
            province = ''
            city = job_location.split('·')[0]
            for p, cities in city_map.items():
                if city in cities:
                    province = p
                    break
            # 保存到 MySQL 数据库
            # 获取数据库连接
            sql = '''insert into post(category, sub_category,job_title,province,job_location,job_company,job_industry,job_finance,job_scale,job_welfare,job_salary_range,job_experience,job_education,job_skills,create_time) values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
            cursor.execute(sql,
                           [current_category, sub_category, job_title, province, job_location, job_company,
                            job_industry,
                            job_finance,
                            job_scale, job_welfare, job_salary_range, job_experience, job_education, job_skills, today])
            conn.commit()
        try:
            # 退回到首页
            browser.back()
            # 模拟点击 互联网/AI 展示出岗位分类
            show_ele = browser.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div[1]/dl[1]/dd/b')
            show_ele.click()
        except:
            browser.get(index_url)
            # 模拟点击 互联网/AI 展示出岗位分类
            show_ele = browser.find_element(by=By.XPATH, value='//*[@id="main"]/div/div[1]/div/div[1]/dl[1]/dd/b')
            show_ele.click()
    time.sleep(10)


def main():
    # 数据库连接
    conn = pymysql.connect(host='127.0.0.1', user='root', password='798lhh', database='BossDB')
    cursor = conn.cursor()
    boss(conn, cursor)
    cursor.close()
    conn.close()


if __name__ == '__main__':
    main()